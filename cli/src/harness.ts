import { existsSync } from "node:fs";
import { homedir } from "node:os";
import { delimiter, join } from "node:path";

export interface Harness {
  id: string;
  label: string;
  /** Global skills directory (absolute). */
  global: string;
  /** Project-relative skills directory. */
  project: string;
  /** Paths or binaries whose presence means the harness is installed. */
  detect: { paths: string[]; bins: string[] };
}

export function harnesses(home: string = homedir()): Harness[] {
  const h = (p: string) => join(home, p);
  return [
    { id: "claude-code", label: "Claude Code", global: h(".claude/skills"), project: ".claude/skills",
      detect: { paths: [h(".claude")], bins: ["claude"] } },
    { id: "codex", label: "OpenAI Codex", global: h(".codex/skills"), project: ".agents/skills",
      detect: { paths: [h(".codex")], bins: ["codex"] } },
    { id: "cursor", label: "Cursor", global: h(".cursor/skills"), project: ".agents/skills",
      detect: { paths: [h(".cursor")], bins: ["cursor", "cursor-agent"] } },
    { id: "gemini-cli", label: "Gemini CLI", global: h(".gemini/skills"), project: ".agents/skills",
      detect: { paths: [h(".gemini")], bins: ["gemini"] } },
    { id: "copilot", label: "GitHub Copilot", global: h(".copilot/skills"), project: ".agents/skills",
      detect: { paths: [h(".copilot")], bins: ["copilot"] } },
    { id: "opencode", label: "OpenCode", global: h(".config/opencode/skills"), project: ".agents/skills",
      detect: { paths: [h(".config/opencode")], bins: ["opencode"] } },
    { id: "windsurf", label: "Windsurf", global: h(".codeium/windsurf/skills"), project: ".windsurf/skills",
      detect: { paths: [h(".codeium/windsurf")], bins: ["windsurf"] } },
    { id: "agents", label: "Generic (.agents/skills: Cline, Amp, Goose, ...)", global: h(".agents/skills"),
      project: ".agents/skills", detect: { paths: [h(".agents")], bins: [] } },
  ];
}

export function onPath(bin: string, env: NodeJS.ProcessEnv = process.env): boolean {
  const exts = process.platform === "win32" ? (env.PATHEXT ?? ".EXE;.CMD;.BAT").split(";") : [""];
  return (env.PATH ?? "").split(delimiter).some((dir) =>
    dir && exts.some((ext) => existsSync(join(dir, bin + ext.toLowerCase())) || existsSync(join(dir, bin + ext))));
}

export function detectHarnesses(all: Harness[] = harnesses()): Harness[] {
  return all.filter((h) => h.id !== "agents" &&
    (h.detect.paths.some((p) => existsSync(p)) || h.detect.bins.some((b) => onPath(b))));
}

export function resolveHarnesses(spec: string | undefined, all: Harness[] = harnesses()): Harness[] {
  if (!spec || spec === "auto") {
    const found = detectHarnesses(all);
    return found.length ? found : all.filter((h) => h.id === "claude-code");
  }
  if (spec === "all") return all;
  return spec.split(",").map((id) => {
    const h = all.find((x) => x.id === id.trim());
    if (!h) throw new Error(`unknown harness '${id}'. Known: ${all.map((x) => x.id).join(", ")}`);
    return h;
  });
}

/** Distinct target directories for the chosen harnesses (several share .agents/skills). */
export function targetDirs(chosen: Harness[], scope: "global" | "project", cwd: string = process.cwd()): string[] {
  const dirs = chosen.map((h) => (scope === "global" ? h.global : join(cwd, h.project)));
  return [...new Set(dirs)];
}
