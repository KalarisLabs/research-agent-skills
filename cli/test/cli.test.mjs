import assert from "node:assert/strict";
import { existsSync, mkdirSync, mkdtempSync, readFileSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { test } from "node:test";
import { gzipSync } from "node:zlib";

import { parseArgs } from "../dist/cli.js";
import { updateTaggedSection, configureHarness, autoConfigureAll } from "../dist/configure.js";
import { harnesses, resolveHarnesses, targetDirs } from "../dist/harness.js";
import { installSkills, readLock, selectSkills, uninstallSkills, verifyInstall } from "../dist/install.js";
import { TOOLS } from "../dist/mcp.js";
import { parseSums, sha256 } from "../dist/source.js";
import { extractEntries, readTar, safeJoin } from "../dist/tar.js";

/** Build a ustar archive in memory: entries = [{ name, data, type }] */
function tar(entries) {
  const blocks = [];
  for (const { name, data = "", type = "0" } of entries) {
    const body = Buffer.from(data);
    const h = Buffer.alloc(512);
    h.write(name, 0, 100);
    h.write("0000644\0", 100);
    h.write("0000000\0", 108);
    h.write("0000000\0", 116);
    h.write(body.length.toString(8).padStart(11, "0") + "\0", 124);
    h.write("00000000000\0", 136);
    h.write("        ", 148);
    h.write(type, 156);
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

test("tar: extracts regular files with strip-components", () => {
  const dir = mkdtempSync(join(tmpdir(), "ras-"));
  const n = extractEntries(readTar(tar([{ name: "repo-1.0/skills/a/SKILL.md", data: "hi" }])), dir, 1);
  assert.equal(n, 1);
  assert.equal(readFileSync(join(dir, "skills/a/SKILL.md"), "utf8"), "hi");
});

test("tar: rejects path traversal and absolute paths", () => {
  const dir = mkdtempSync(join(tmpdir(), "ras-"));
  assert.throws(() => extractEntries(readTar(tar([{ name: "repo/../../evil", data: "x" }])), dir, 1), /unsafe path/);
  assert.throws(() => safeJoin(dir, "/etc/passwd"), /unsafe path/);
  assert.throws(() => safeJoin(dir, "C:/Windows/x"), /unsafe path/);
  assert.throws(() => safeJoin(dir, "a/../../b"), /unsafe path/);
});

test("tar: rejects symlink and hardlink entries", () => {
  assert.throws(() => readTar(tar([{ name: "repo/link", type: "2" }])), /only regular files/);
  assert.throws(() => readTar(tar([{ name: "repo/hard", type: "1" }])), /only regular files/);
});

test("checksums: parseSums and sha256", () => {
  const h = sha256(Buffer.from("abc"));
  assert.equal(h, "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad");
  assert.deepEqual(parseSums(`${h}  file.tar.gz\n${h} *other.txt\n`), { "file.tar.gz": h, "other.txt": h });
});

test("args: flags, values and positionals", () => {
  const a = parseArgs(["install", "peer-review", "--harness", "codex", "--dry-run", "--category=a,b", "-y"]);
  assert.equal(a.cmd, "install");
  assert.deepEqual(a.positional, ["peer-review"]);
  assert.equal(a.flags.harness, "codex");
  assert.equal(a.flags["dry-run"], true);
  assert.equal(a.flags.category, "a,b");
  assert.equal(a.flags.yes, true);
  assert.throws(() => parseArgs(["install", "--harness"]), /needs a value/);
});

test("harness: resolution and shared target dirs", () => {
  const all = harnesses("/home/u");
  assert.throws(() => resolveHarnesses("nope", all), /unknown harness/);
  const chosen = resolveHarnesses("codex,cursor,gemini-cli", all);
  assert.equal(targetDirs(chosen, "project", "/proj").length, 1); // all share .agents/skills
  assert.equal(targetDirs(chosen, "global").length, 3);
});

const catalog = {
  name: "t", version: "9.9.9",
  categories: [{ id: "writing", description: "", count: 2 }, { id: "bio", description: "", count: 1 }],
  bundles: { essentials: { description: "", categories: ["writing"] }, bio: { description: "", categories: [], skills: ["c-skill"] } },
  skills: [
    { name: "a-skill", category: "writing", path: "skills/a-skill", version: "1", description: "", tags: [] },
    { name: "b-skill", category: "writing", path: "skills/b-skill", version: "1", description: "", tags: [] },
    { name: "c-skill", category: "bio", path: "skills/c-skill", version: "1", description: "", tags: [] },
  ],
};

test("selection: names, categories, bundles, errors", () => {
  assert.deepEqual(selectSkills(catalog, { bundles: ["essentials"] }).map((s) => s.name), ["a-skill", "b-skill"]);
  assert.deepEqual(selectSkills(catalog, { bundles: ["bio"] }).map((s) => s.name), ["c-skill"]);
  assert.deepEqual(selectSkills(catalog, { names: ["c-skill"], categories: ["writing"] }).length, 3);
  assert.equal(selectSkills(catalog, { all: true }).length, 3);
  assert.throws(() => selectSkills(catalog, { names: ["zzz"] }), /unknown skill/);
  assert.throws(() => selectSkills(catalog, { categories: ["zzz"] }), /unknown category/);
});

test("install/verify/uninstall roundtrip never touches unmanaged skills", () => {
  const root = mkdtempSync(join(tmpdir(), "ras-src-"));
  for (const s of catalog.skills) {
    mkdirSync(join(root, s.path), { recursive: true });
    writeFileSync(join(root, s.path, "SKILL.md"), `---\nname: ${s.name}\n---\n`);
  }
  const src = { root, version: "9.9.9", catalog, origin: "test" };
  const target = mkdtempSync(join(tmpdir(), "ras-dst-"));
  mkdirSync(join(target, "user-own-skill"));
  mkdirSync(join(target, "b-skill")); // pre-existing, unmanaged folder with the same name
  const log = () => {};
  const r = installSkills(src, catalog.skills, target, { mode: "copy", force: false, dryRun: false, log });
  assert.deepEqual(r.installed.sort(), ["a-skill", "c-skill"]);
  assert.deepEqual(r.skipped, ["b-skill"]);
  assert.deepEqual(Object.keys(readLock(target).skills).sort(), ["a-skill", "c-skill"]);
  assert.deepEqual(verifyInstall(target), []);
  writeFileSync(join(target, "a-skill", "SKILL.md"), "tampered");
  assert.equal(verifyInstall(target)[0].problem, "file modified: SKILL.md");
  assert.deepEqual(uninstallSkills(target, "all", false).sort(), ["a-skill", "c-skill"]);
  assert.ok(existsSync(join(target, "user-own-skill")) && existsSync(join(target, "b-skill")));
  assert.equal(readLock(target), undefined);
});

test("harness: scientific, control plane, and expanded catalog", () => {
  const all = harnesses("/home/u");
  assert.equal(all.length, 20);
  const ids = all.map((h) => h.id);
  assert.ok(ids.includes("claude-science"));
  assert.ok(ids.includes("openscience"));
  assert.ok(ids.includes("t3-code"));
  assert.ok(ids.includes("antigravity"));
  assert.ok(ids.includes("hermes"));
  assert.ok(ids.includes("openhands"));
  assert.ok(ids.includes("goose"));
  assert.ok(ids.includes("aider"));
  assert.ok(ids.includes("roo-code"));

  const sci = all.filter((h) => h.category === "science");
  assert.equal(sci.length, 2);
  const cp = all.filter((h) => h.category === "control-plane");
  assert.equal(cp.length, 1);
});

test("configure: updates tagged sections non-destructively", () => {
  const initial = "# My Project\n\nCustom instructions.\n";
  const updated = updateTaggedSection(initial, "Injected research block");
  assert.ok(updated.includes("# My Project"));
  assert.ok(updated.includes("Injected research block"));
  assert.ok(updated.includes("<!-- research-agent-skills:start -->"));

  const replaced = updateTaggedSection(updated, "New replacement block");
  assert.ok(replaced.includes("New replacement block"));
  assert.ok(!replaced.includes("Injected research block"));
  assert.ok(replaced.includes("Custom instructions."));
});

test("configure: auto-configures project anchors for multiple harnesses", () => {
  const target = mkdtempSync(join(tmpdir(), "ras-cfg-"));
  const all = harnesses(target);
  const chosen = resolveHarnesses("claude-science,t3-code,aider,antigravity", all);
  const res = autoConfigureAll(chosen, target);
  assert.ok(res.length >= 4);
  assert.ok(existsSync(join(target, "CLAUDE.md")));
  assert.ok(existsSync(join(target, ".claude-science", "specialists.json")));
  assert.ok(existsSync(join(target, ".t3", "config.json")));
  assert.ok(existsSync(join(target, "CONVENTIONS.md")));
  assert.ok(existsSync(join(target, "AGENTS.md")));
});

test("mcp: defines expected tools with valid json schemas", () => {
  assert.ok(Array.isArray(TOOLS));
  const toolNames = TOOLS.map((t) => t.name);
  assert.ok(toolNames.includes("search_skills"));
  assert.ok(toolNames.includes("get_skill"));
  assert.ok(toolNames.includes("list_bundles"));
  assert.ok(toolNames.includes("list_skills"));
  assert.ok(toolNames.includes("install_skills"));
  assert.ok(toolNames.includes("run_skill_script"));
  for (const t of TOOLS) {
    assert.equal(t.inputSchema.type, "object");
    assert.ok(t.description.length > 0);
  }
});


