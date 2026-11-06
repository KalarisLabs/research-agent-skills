import { existsSync } from "node:fs";
import { homedir } from "node:os";
import { delimiter, join } from "node:path";

export type HarnessCategory = "science" | "control-plane" | "coding-ide" | "cli-agent" | "generic";

export interface Harness {
  id: string;
  label: string;
  category?: HarnessCategory;
  /** Global skills directory (absolute). */
  global: string;
  /** Project-relative skills directory. */
  project: string;
  /** Paths or binaries whose presence means the harness is installed. */
  detect: { paths: string[]; bins: string[] };
}

export function harnesses(home: string = homedir()): Harness[] {
  const h = (p: string) => join(home, p);
  const localAppData = process.env.LOCALAPPDATA;
  const appData = process.env.APPDATA;

  return [
    // --- Scientific Research Workbenches ---
    {
      id: "claude-science",
      label: "Claude Science",
      category: "science",
      global: h(".claude-science/skills"),
      project: ".claude-science/skills",
      detect: {
        paths: [
          h(".claude-science"),
          h(".config/claude-science"),
          "/Applications/Claude Science.app",
          h("Library/Application Support/Claude Science"),
          ...(localAppData ? [join(localAppData, "ClaudeScience")] : []),
        ],
        bins: ["claude-science"],
      },
    },
    {
      id: "openscience",
      label: "Open Science (openscience.sh)",
      category: "science",
      global: h(".openscience/skills"),
      project: ".openscience/skills",
      detect: {
        paths: [h(".openscience"), h(".synsci")],
        bins: ["openscience", "synsci"],
      },
    },

    // --- Control Planes & Multi-Agent Surfaces ---
    {
      id: "t3-code",
      label: "T3 Code",
      category: "control-plane",
      global: h(".t3/skills"),
      project: ".t3/skills",
      detect: {
        paths: [
          h(".t3"),
          h(".config/t3"),
          ...(appData ? [join(appData, "T3Code")] : []),
        ],
        bins: ["t3", "t3code", "t3-code"],
      },
    },
    {
      id: "antigravity",
      label: "Google Antigravity",
      category: "coding-ide",
      global: h(".gemini/config/skills"),
      project: ".gemini/config/skills",
      detect: {
        paths: [h(".gemini/antigravity"), h(".gemini/config"), h(".gemini")],
        bins: ["agy", "antigravity"],
      },
    },
    {
      id: "hermes",
      label: "Nous Hermes Agent",
      category: "cli-agent",
      global: h(".hermes/skills"),
      project: ".hermes/skills",
      detect: {
        paths: [h(".hermes"), h(".config/hermes")],
        bins: ["hermes"],
      },
    },

    // --- Developer & CLI Agent Harnesses ---
    {
      id: "claude-code",
      label: "Claude Code",
      category: "cli-agent",
      global: h(".claude/skills"),
      project: ".claude/skills",
      detect: { paths: [h(".claude")], bins: ["claude"] },
    },
    {
      id: "codex",
      label: "OpenAI Codex",
      category: "cli-agent",
      global: h(".codex/skills"),
      project: ".agents/skills",
      detect: { paths: [h(".codex")], bins: ["codex"] },
    },
    {
      id: "cursor",
      label: "Cursor",
      category: "coding-ide",
      global: h(".cursor/skills"),
      project: ".agents/skills",
      detect: { paths: [h(".cursor")], bins: ["cursor", "cursor-agent"] },
    },
    {
      id: "gemini-cli",
      label: "Gemini CLI",
      category: "cli-agent",
      global: h(".gemini/skills"),
      project: ".agents/skills",
      detect: { paths: [h(".gemini")], bins: ["gemini"] },
    },
    {
      id: "copilot",
      label: "GitHub Copilot",
      category: "coding-ide",
      global: h(".copilot/skills"),
      project: ".agents/skills",
      detect: { paths: [h(".copilot")], bins: ["copilot"] },
    },
    {
      id: "openhands",
      label: "OpenHands (OpenDevin)",
      category: "cli-agent",
      global: h(".openhands/skills"),
      project: ".openhands/microagents",
      detect: { paths: [h(".openhands")], bins: ["openhands"] },
    },
    {
      id: "goose",
      label: "Goose",
      category: "cli-agent",
      global: h(".config/goose/skills"),
      project: ".goose/skills",
      detect: { paths: [h(".config/goose"), h(".goose")], bins: ["goose"] },
    },
    {
      id: "aider",
      label: "Aider",
      category: "cli-agent",
      global: h(".aider/skills"),
      project: ".aider/skills",
      detect: { paths: [h(".aider")], bins: ["aider"] },
    },
    {
      id: "opencode",
      label: "OpenCode",
      category: "cli-agent",
      global: h(".config/opencode/skills"),
      project: ".agents/skills",
      detect: { paths: [h(".config/opencode")], bins: ["opencode"] },
    },
    {
      id: "windsurf",
      label: "Windsurf",
      category: "coding-ide",
      global: h(".codeium/windsurf/skills"),
      project: ".windsurf/skills",
      detect: { paths: [h(".codeium/windsurf")], bins: ["windsurf"] },
    },
    {
      id: "roo-code",
      label: "Roo Code / Cline",
      category: "coding-ide",
      global: h(".roo/skills"),
      project: ".roo/skills",
      detect: { paths: [h(".roo"), h(".cline")], bins: ["roo", "cline"] },
    },
    {
      id: "zed",
      label: "Zed Assistant",
      category: "coding-ide",
      global: h(".config/zed/skills"),
      project: ".zed/prompts",
      detect: { paths: [h(".config/zed")], bins: ["zed"] },
    },
    {
      id: "trae",
      label: "Trae",
      category: "coding-ide",
      global: h(".trae/skills"),
      project: ".trae/rules",
      detect: { paths: [h(".trae")], bins: ["trae"] },
    },
    {
      id: "continue",
      label: "Continue.dev",
      category: "coding-ide",
      global: h(".continue/skills"),
      project: ".continue/prompts",
      detect: { paths: [h(".continue")], bins: ["continue"] },
    },
    {
      id: "agents",
      label: "Generic (.agents/skills: Cline, Amp, Goose, ...)",
      category: "generic",
      global: h(".agents/skills"),
      project: ".agents/skills",
      detect: { paths: [h(".agents")], bins: [] },
    },
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
