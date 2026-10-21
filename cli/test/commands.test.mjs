// End-to-end tests for the command layer and release download, against a fixture checkout and a local HTTP
// server. Nothing leaves the machine: HOME, the cache and the release URL are all redirected to temp dirs.
import assert from "node:assert/strict";
import { createServer } from "node:http";
import { existsSync, mkdirSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { after, before, test } from "node:test";
import { gzipSync } from "node:zlib";

import { main } from "../dist/cli.js";
import { cacheRoot, loadCatalog, resolveSource, sha256 } from "../dist/source.js";

const catalog = {
  name: "fixture", version: "9.9.9",
  categories: [{ id: "writing", description: "Writing skills", count: 2 }],
  bundles: { "research-essentials": { description: "core", categories: ["writing"] } },
  skills: [
    { name: "alpha-skill", category: "writing", path: "skills/alpha-skill", version: "1", license: "MIT",
      description: "Drafts abstracts for journals", tags: ["abstract", "journal"], has_scripts: true },
    { name: "beta-skill", category: "writing", path: "skills/beta-skill", version: "1", license: "MIT",
      description: "Checks citations", tags: ["citation"], has_scripts: false },
  ],
};

function writeCheckout(root) {
  mkdirSync(join(root, "catalog"), { recursive: true });
  writeFileSync(join(root, "catalog", "skills.json"), JSON.stringify(catalog));
  for (const s of catalog.skills) {
    mkdirSync(join(root, s.path), { recursive: true });
    writeFileSync(join(root, s.path, "SKILL.md"), `---\nname: ${s.name}\ndescription: ${s.description}\n---\n# ${s.name}\n`);
  }
}

/** Run the CLI with HOME, cwd and stdout redirected; returns { code, out }. */
async function run(home, argv, cwd = home) {
  const saved = { write: process.stdout.write, home: process.env.HOME, profile: process.env.USERPROFILE, cwd: process.cwd() };
  let out = "";
  process.stdout.write = (chunk) => { out += chunk; return true; };
  process.env.HOME = home;
  process.env.USERPROFILE = home;
  process.chdir(cwd);
  try {
    return { code: await main(argv), out };
  } finally {
    process.stdout.write = saved.write;
    process.env.HOME = saved.home;
    if (saved.profile === undefined) delete process.env.USERPROFILE; else process.env.USERPROFILE = saved.profile;
    process.chdir(saved.cwd);
  }
}

const base = mkdtempSync(join(tmpdir(), "ras-cmd-"));
const checkout = join(base, "checkout");
writeCheckout(checkout);
let n = 0;
const freshHome = () => { const h = join(base, `home${n++}`); mkdirSync(h, { recursive: true }); return h; };

test("help, version and unknown commands", async () => {
  const home = freshHome();
  assert.match((await run(home, ["--help"])).out, /Usage:/);
  assert.match((await run(home, ["help"])).out, /research-agent-skills v/);
  const v = await run(home, ["--version"]);
  assert.equal(v.code, 0);
  assert.match(v.out, /^\d+\.\d+\.\d+/);
  const bad = await run(home, ["frobnicate"]);
  assert.equal(bad.code, 2);
  assert.match(bad.out, /unknown command 'frobnicate'/);
});

test("list, search and categories read the catalog", async () => {
  const home = freshHome();
  const src = ["--source", checkout];
  const list = await run(home, ["list", ...src]);
  assert.match(list.out, /alpha-skill/);
  assert.match(list.out, /2 skills/);
  assert.match((await run(home, ["list", "--categories", ...src])).out, /writing\s+2\s+Writing skills/);
  assert.equal(JSON.parse((await run(home, ["list", "--json", "--category", "writing", ...src])).out).length, 2);
  assert.match((await run(home, ["search", "citation", ...src])).out, /beta-skill/);
  assert.match((await run(home, ["search", "zzzz", ...src])).out, /no matches/);
  await assert.rejects(run(home, ["search", ...src]), /usage: research-agent-skills search/);
});

test("install, installed, doctor, update and uninstall for a project", async () => {
  const home = freshHome();
  const proj = join(home, "proj");
  mkdirSync(proj);
  const flags = ["--source", checkout, "--harness", "claude-code", "--project"];

  const dry = await run(home, ["install", "alpha-skill", "--dry-run", ...flags], proj);
  assert.match(dry.out, /Dry run: nothing was written/);
  assert.ok(!existsSync(join(proj, ".claude", "skills", "alpha-skill")));

  const inst = await run(home, ["install", "alpha-skill", ...flags], proj);
  assert.equal(inst.code, 0);
  assert.match(inst.out, /1 installed/);
  assert.match(inst.out, /1 of these skills include Python scripts/);
  assert.ok(existsSync(join(proj, ".claude", "skills", "alpha-skill", "SKILL.md")));

  const bundle = await run(home, ["install", "--yes", ...flags], proj); // default bundle
  assert.match(bundle.out, /Installing 2 skill\(s\)/);

  assert.match((await run(home, ["installed", "--harness", "claude-code", "--project"], proj)).out, /alpha-skill, beta-skill/);

  const ok = await run(home, ["doctor", "--harness", "claude-code", "--project"], proj);
  assert.equal(ok.code, 0);
  assert.match(ok.out, /integrity OK/);

  writeFileSync(join(proj, ".claude", "skills", "alpha-skill", "SKILL.md"), "tampered\n");
  const bad = await run(home, ["doctor", "--harness", "claude-code", "--project"], proj);
  assert.equal(bad.code, 1);
  assert.match(bad.out, /integrity issue/);

  const upd = await run(home, ["update", ...flags], proj);
  assert.match(upd.out, /updated to v9\.9\.9/);
  assert.equal((await run(home, ["doctor", "--harness", "claude-code", "--project"], proj)).code, 0);

  await assert.rejects(run(home, ["uninstall", "--harness", "claude-code", "--project"], proj), /name the skills to remove/);
  const rm = await run(home, ["uninstall", "alpha-skill", "--harness", "claude-code", "--project"], proj);
  assert.match(rm.out, /removed alpha-skill/);
  assert.ok(!existsSync(join(proj, ".claude", "skills", "alpha-skill")));
  await run(home, ["remove", "--all", "--harness", "claude-code", "--project"], proj);
  assert.match((await run(home, ["installed", "--harness", "claude-code", "--project"], proj)).out, /No skills installed/);
});

test("loadCatalog rejects a directory that is not a checkout", () => {
  assert.throws(() => loadCatalog(base), /not a research-agent-skills checkout/);
});

// --- release download: checksum verified before anything is extracted ----------------------------------------------

function tarball(files) {
  const blocks = [];
  for (const [name, data] of Object.entries(files)) {
    const body = Buffer.from(data);
    const h = Buffer.alloc(512);
    h.write(name, 0, 100);
    h.write("0000644\0", 100);
    h.write("0000000\0", 108);
    h.write("0000000\0", 116);
    h.write(body.length.toString(8).padStart(11, "0") + "\0", 124);
    h.write("00000000000\0", 136);
    h.write("        ", 148);
    h.write("0", 156);
    h.write("ustar\0", 257);
    h.write("00", 263);
    let sum = 0;
    for (const b of h) sum += b;
    h.write(sum.toString(8).padStart(6, "0") + "\0 ", 148);
    blocks.push(h, body, Buffer.alloc((512 - (body.length % 512)) % 512));
  }
  blocks.push(Buffer.alloc(1024));
  return gzipSync(Buffer.concat(blocks));
}

const goodTar = tarball({
  "repo-9.9.9/catalog/skills.json": JSON.stringify(catalog),
  "repo-9.9.9/skills/alpha-skill/SKILL.md": "# alpha\n",
  "repo-9.9.9/.github/workflows/ci.yml": "should not be extracted\n",
});
const asset = "research-agent-skills-9.9.9.tar.gz";
let server;
let baseUrl;
let sums = `${sha256(goodTar)}  ${asset}\n`;

before(async () => {
  server = createServer((req, res) => {
    const body = req.url.endsWith("SHA256SUMS") ? Buffer.from(sums) : req.url.endsWith(asset) ? goodTar : undefined;
    res.statusCode = body ? 200 : 404;
    res.end(body);
  });
  await new Promise((r) => server.listen(0, "127.0.0.1", r));
  baseUrl = `http://127.0.0.1:${server.address().port}`;
});
after(() => {
  server.close();
  rmSync(base, { recursive: true, force: true }); // fixture checkout, fake homes and caches
});

test("cacheRoot honours its overrides", () => {
  assert.equal(cacheRoot({ RESEARCH_AGENT_SKILLS_CACHE: "/c" }), "/c");
  assert.match(cacheRoot({ XDG_CACHE_HOME: "/x" }), /research-agent-skills$/);
});

test("resolveSource downloads, verifies, extracts only allowed paths, then reuses the cache", async () => {
  process.env.RESEARCH_AGENT_SKILLS_CACHE = join(base, "cache-good");
  process.env.RAS_BASE_URL = baseUrl;
  const logs = [];
  const src = await resolveSource({ version: "v9.9.9", log: (m) => logs.push(m) });
  assert.equal(src.version, "9.9.9");
  assert.ok(logs.some((l) => /Verified SHA-256/.test(l)));
  assert.ok(existsSync(join(src.root, "skills", "alpha-skill", "SKILL.md")));
  assert.ok(!existsSync(join(src.root, ".github")), "paths outside the allow-list are not extracted");
  assert.match(readFileSync(join(src.root, ".verified"), "utf8"), /^[0-9a-f]{64}\n$/);
  const again = await resolveSource({ version: "9.9.9", log: (m) => logs.push(m) });
  assert.match(again.origin, /^cache:/);
});

test("resolveSource refuses a checksum mismatch, a missing entry and a failed download", async () => {
  process.env.RAS_BASE_URL = baseUrl;
  const log = () => {};
  process.env.RESEARCH_AGENT_SKILLS_CACHE = join(base, "cache-mismatch");
  sums = `${"0".repeat(64)}  ${asset}\n`;
  await assert.rejects(resolveSource({ version: "9.9.9", log }), /checksum mismatch/);
  assert.ok(!existsSync(join(base, "cache-mismatch", "9.9.9")), "nothing is extracted after a mismatch");
  sums = `${sha256(goodTar)}  other.tar.gz\n`;
  await assert.rejects(resolveSource({ version: "9.9.9", log }), /has no entry for/);
  await assert.rejects(resolveSource({ version: "1.2.3", log }), /download failed \(404/);
  sums = `${sha256(goodTar)}  ${asset}\n`;
});
