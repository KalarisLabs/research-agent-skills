// Drives the real MCP stdio server over JSON-RPC against a fixture checkout. The server runs as a child process
// (NODE_V8_COVERAGE is inherited, so it counts toward the coverage gate); HOME is redirected to a temp dir.
import assert from "node:assert/strict";
import { spawn, spawnSync } from "node:child_process";
import { existsSync, mkdirSync, mkdtempSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { dirname, join } from "node:path";
import { test } from "node:test";
import { fileURLToPath } from "node:url";

const bin = join(dirname(fileURLToPath(import.meta.url)), "..", "dist", "bin.js");

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

const base = mkdtempSync(join(tmpdir(), "ras-mcp-"));
const checkout = join(base, "checkout");
mkdirSync(join(checkout, "catalog"), { recursive: true });
writeFileSync(join(checkout, "catalog", "skills.json"), JSON.stringify(catalog));
for (const s of catalog.skills) {
  mkdirSync(join(checkout, s.path), { recursive: true });
  writeFileSync(join(checkout, s.path, "SKILL.md"), `---\nname: ${s.name}\ndescription: ${s.description}\n---\n# ${s.name}\n`);
}
mkdirSync(join(checkout, "skills/alpha-skill/scripts"));
mkdirSync(join(checkout, "skills/alpha-skill/references"));
writeFileSync(join(checkout, "skills/alpha-skill/scripts/echo.py"), "import sys\nprint('ARGS=' + ','.join(sys.argv[1:]))\n");
writeFileSync(join(checkout, "skills/alpha-skill/references/ref.md"), "# ref\n");

const pythonAvailable = ["python3", "python", "uv"].some((b) => spawnSync(b, ["--version"], { stdio: "ignore" }).status === 0);

/** Send newline-delimited JSON-RPC messages (strings are sent raw), close stdin, return parsed responses. */
function session(messages, { home = join(base, "home") } = {}) {
  mkdirSync(home, { recursive: true });
  return new Promise((resolve, reject) => {
    const child = spawn(process.execPath, [bin, "mcp", "--source", checkout], {
      env: { ...process.env, HOME: home, USERPROFILE: home },
      stdio: ["pipe", "pipe", "pipe"],
    });
    let out = "";
    let err = "";
    child.stdout.on("data", (d) => { out += d; });
    child.stderr.on("data", (d) => { err += d; });
    child.on("error", reject);
    child.on("close", () => {
      resolve({
        responses: out.split("\n").filter(Boolean).map((l) => JSON.parse(l)),
        stderr: err,
      });
    });
    for (const m of messages) child.stdin.write((typeof m === "string" ? m : JSON.stringify(m)) + "\n");
    child.stdin.end();
  });
}

const rpc = (id, method, params) => ({ jsonrpc: "2.0", id, method, params });
const call = (id, name, args) => rpc(id, "tools/call", { name, arguments: args });
const textOf = (res) => JSON.parse(res.result.content[0].text);

test("protocol: initialize, ping, tools/list, notifications and malformed input", async () => {
  const { responses, stderr } = await session([
    rpc(1, "initialize", {}),
    { jsonrpc: "2.0", method: "notifications/initialized" },
    rpc(2, "ping"),
    rpc(3, "tools/list"),
    rpc(4, "nope/method"),
    "{ not json",
    "",
    { jsonrpc: "2.0", id: 5 },
    { jsonrpc: "2.0" },
  ]);
  const byId = new Map(responses.map((r) => [r.id, r]));
  assert.equal(byId.get(1).result.serverInfo.name, "research-agent-skills-mcp");
  assert.deepEqual(byId.get(2).result, {});
  assert.deepEqual(
    byId.get(3).result.tools.map((t) => t.name).sort(),
    ["get_skill", "install_skills", "list_bundles", "list_skills", "run_skill_script", "search_skills"],
  );
  assert.equal(byId.get(4).error.code, -32601);
  assert.equal(byId.get(5).error.code, -32600);
  assert.ok(responses.some((r) => r.error?.code === -32700), "parse error is reported");
  assert.match(stderr, /Client initialized session/);
});

test("search_skills, list_skills, list_bundles and get_skill read the catalog", async () => {
  const { responses } = await session([
    call(1, "search_skills", { query: "citation" }),
    call(2, "search_skills", { query: "abstract journal", category: "Writing" }),
    call(3, "search_skills", { query: "zzzz" }),
    call(4, "list_skills", {}),
    call(5, "list_skills", { category: "writing", bundle: "research-essentials" }),
    call(6, "list_bundles", {}),
    call(7, "get_skill", { name: "alpha-skill" }),
    call(8, "get_skill", { name: "beta-skill" }),
    call(9, "get_skill", { name: "missing" }),
  ]);
  const r = new Map(responses.map((x) => [x.id, x]));
  assert.deepEqual(textOf(r.get(1)).skills.map((s) => s.name), ["beta-skill"]);
  assert.deepEqual(textOf(r.get(2)).skills.map((s) => s.name), ["alpha-skill"]);
  assert.equal(textOf(r.get(3)).matches_count, 0);
  assert.equal(textOf(r.get(4)).count, 2);
  assert.equal(textOf(r.get(5)).count, 2);
  assert.ok("research-essentials" in textOf(r.get(6)).bundles);
  const alpha = textOf(r.get(7));
  assert.deepEqual(alpha.scripts, ["echo.py"]);
  assert.deepEqual(alpha.references, ["ref.md"]);
  assert.match(alpha.skill_markdown, /# alpha-skill/);
  assert.deepEqual(textOf(r.get(8)).scripts, []);
  assert.match(r.get(9).error.message, /not found/);
});

test("resources/list and resources/read", async () => {
  const { responses } = await session([
    rpc(1, "resources/list"),
    rpc(2, "resources/read", { uri: "skill://alpha-skill" }),
    rpc(3, "resources/read", { uri: "skill://missing" }),
    rpc(4, "resources/read", { uri: "https://example.com/x" }),
    rpc(5, "resources/read", {}),
  ]);
  const r = new Map(responses.map((x) => [x.id, x]));
  assert.equal(r.get(1).result.resources.length, 2);
  assert.match(r.get(2).result.contents[0].text, /alpha-skill/);
  assert.match(r.get(3).error.message, /not found/);
  assert.match(r.get(4).error.message, /Unsupported URI/);
  assert.match(r.get(5).error.message, /Unsupported URI/);
});

test("install_skills copies into a throwaway project and rejects bad input", async () => {
  const home = join(base, "install-home");
  const { responses } = await session([
    call(1, "install_skills", { skills: ["alpha-skill"], harness: "claude-code" }),
    call(2, "install_skills", { skills: [] }),
    call(3, "install_skills", { skills: ["missing-skill"], harness: "claude-code" }),
  ], { home });
  const r = new Map(responses.map((x) => [x.id, x]));
  assert.equal(textOf(r.get(1)).installed_count, 1);
  assert.ok(existsSync(join(home, ".claude", "skills", "alpha-skill", "SKILL.md")));
  assert.match(r.get(2).error.message, /No skills specified/);
  assert.ok(r.get(3).error, "unknown skill is an error");
});

test("run_skill_script validates input and refuses path traversal", async () => {
  const { responses } = await session([
    call(1, "run_skill_script", { script: "echo.py" }),
    call(2, "run_skill_script", { skill: "alpha-skill" }),
    call(3, "run_skill_script", { skill: "alpha-skill", script: "../SKILL.md" }),
    call(4, "run_skill_script", { skill: "alpha-skill", script: "a/b.py" }),
    call(5, "run_skill_script", { skill: "alpha-skill", script: "a\\b.py" }),
    call(6, "run_skill_script", { skill: "missing", script: "echo.py" }),
    call(7, "run_skill_script", { skill: "alpha-skill", script: "absent.py" }),
    call(8, "unknown_tool", {}),
  ]);
  const r = new Map(responses.map((x) => [x.id, x]));
  assert.match(r.get(1).error.message, /'skill' is required/);
  assert.match(r.get(2).error.message, /'script' is required/);
  for (const id of [3, 4, 5]) assert.match(r.get(id).error.message, /path traversal/);
  assert.match(r.get(6).error.message, /not found/);
  assert.match(r.get(7).error.message, /does not exist/);
  assert.match(r.get(8).error.message, /Unknown tool/);
});

test("run_skill_script runs a bundled script and passes args without a shell", { skip: !pythonAvailable }, async () => {
  const tricky = "a&echo INJECTED";
  const { responses } = await session([call(1, "run_skill_script", { skill: "alpha-skill", script: "echo.py", args: ["x", tricky], timeout_seconds: 60 })]);
  const out = textOf(responses[0]);
  assert.equal(out.exit_code, 0, out.stderr);
  assert.equal(out.timed_out, false);
  // The metacharacter reaches the script verbatim instead of being interpreted by a shell.
  assert.match(out.stdout, /ARGS=x,a&echo INJECTED/);
});
