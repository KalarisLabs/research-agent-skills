// Unit tests for harness configuration: anchors are written once, updated in place, and never clobber user content.
import assert from "node:assert/strict";
import { existsSync, mkdirSync, mkdtempSync, readFileSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { test } from "node:test";

import { autoConfigureAll, configureHarness, END_TAG, START_TAG, updateTaggedSection } from "../dist/configure.js";
import { harnesses } from "../dist/harness.js";

const base = mkdtempSync(join(tmpdir(), "ras-cfg-"));
let n = 0;
const fresh = () => { const d = join(base, `p${n++}`); mkdirSync(d, { recursive: true }); return d; };
const skills = Array.from({ length: 17 }, (_, i) => ({
  name: `skill-${i}`, description: "d".repeat(100), category: "writing", path: `skills/skill-${i}`,
  version: "1", license: "MIT", tags: [], has_scripts: false,
}));
const all = harnesses(join(base, "home"));
const byId = (id) => all.find((h) => h.id === id);

test("updateTaggedSection appends, replaces in place and preserves user content", () => {
  const first = updateTaggedSection("", "hello");
  assert.equal(first, `${START_TAG}\nhello\n${END_TAG}\n`);
  const appended = updateTaggedSection("# Mine", "hello");
  assert.ok(appended.startsWith("# Mine\n\n"));
  const replaced = updateTaggedSection(`before\n${START_TAG}\nold\n${END_TAG}\nafter\n`, "new");
  assert.match(replaced, /before\n<!-- research-agent-skills:start -->\nnew\n<!-- research-agent-skills:end -->\nafter/);
  assert.ok(!replaced.includes("old"));
  // Tags out of order: treated as absent, so the block is appended instead of corrupting the file.
  assert.ok(updateTaggedSection(`${END_TAG}\n${START_TAG}`, "x").endsWith(`${END_TAG}\n`));
});

test("markdown-anchor harnesses create, then report unchanged on a second run", () => {
  const files = {
    "claude-code": "CLAUDE.md", aider: "CONVENTIONS.md", cursor: ".cursorrules", windsurf: ".windsurfrules",
    goose: ".goosehints", codex: "AGENTS.md", openhands: join(".openhands", "microagents", "repo.md"),
  };
  for (const [id, file] of Object.entries(files)) {
    const cwd = fresh();
    const h = byId(id) ?? { id, label: id, global: "", project: `.${id}/skills`, detect: { paths: [], bins: [] } };
    const [first] = configureHarness(h, cwd, skills);
    assert.equal(first.action, "created", id);
    assert.ok(existsSync(join(cwd, file)), id);
    const text = readFileSync(join(cwd, file), "utf8");
    assert.match(text, /and 2 more\./, "skill list is truncated to 15");
    assert.equal(configureHarness(h, cwd, skills)[0].action, "unchanged", id);
    writeFileSync(join(cwd, file), `# keep me\n${text}`);
    assert.equal(configureHarness(h, cwd, skills.slice(0, 2))[0].action, "updated", id);
    assert.match(readFileSync(join(cwd, file), "utf8"), /# keep me/);
  }
});

test("a skill-less configure still writes the anchor", () => {
  const cwd = fresh();
  configureHarness(byId("claude-code"), cwd);
  assert.doesNotMatch(readFileSync(join(cwd, "CLAUDE.md"), "utf8"), /Key installed skills/);
});

test("manifest harnesses write JSON once and never overwrite an existing one", () => {
  const cwd = fresh();
  const r = configureHarness(byId("claude-science"), cwd, skills);
  assert.deepEqual(r.map((x) => x.file).sort(), [".claude-science/specialists.json", "CLAUDE.md"]);
  const spec = join(cwd, ".claude-science", "specialists.json");
  writeFileSync(spec, '{"custom":true}');
  assert.equal(configureHarness(byId("claude-science"), cwd, skills).length, 1, "existing manifest is left alone");
  assert.equal(readFileSync(spec, "utf8"), '{"custom":true}');

  for (const [id, file] of [["t3-code", ".t3/config.json"], ["roo-code", ".roomodes"]]) {
    const dir = fresh();
    const h = byId(id) ?? { id, label: id, global: "", project: `.${id}/skills`, detect: { paths: [], bins: [] } };
    assert.equal(configureHarness(h, dir, skills)[0].file, file);
    assert.deepEqual(configureHarness(h, dir, skills), [], `${id} does not rewrite an existing config`);
  }

  const dir = fresh();
  const h = byId("openscience");
  assert.equal(configureHarness(h, dir, skills)[0].action, "created");
  assert.equal(JSON.parse(readFileSync(join(dir, ".openscience", "skills.json"), "utf8")).skills.length, 17);
  assert.equal(configureHarness(h, dir)[0].action, "updated", "no skills: list is empty and the file changes");
});

test("autoConfigureAll de-duplicates by harness and file", () => {
  const cwd = fresh();
  const hs = ["codex", "gemini-cli", "claude-code"].map((id) => byId(id)).filter(Boolean);
  const results = autoConfigureAll([...hs, ...hs], cwd, skills);
  const keys = results.map((r) => `${r.harness}:${r.file}`);
  assert.equal(new Set(keys).size, keys.length);
  assert.ok(results.length >= 1);
});
