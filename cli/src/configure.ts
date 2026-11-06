import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import type { Harness } from "./harness.js";
import type { SkillEntry } from "./source.js";

export const START_TAG = "<!-- research-agent-skills:start -->";
export const END_TAG = "<!-- research-agent-skills:end -->";

export interface ConfigureResult {
  file: string;
  action: "created" | "updated" | "unchanged";
  harness: string;
}

function readFileSafe(filePath: string): string | null {
  try {
    return readFileSync(filePath, "utf8");
  } catch (err: unknown) {
    if (err && typeof err === "object" && "code" in err && (err as { code: string }).code === "ENOENT") {
      return null;
    }
    throw err;
  }
}

/**
 * Replace or append a tagged block in a file without disturbing user content outside the tags.
 */
export function updateTaggedSection(
  content: string,
  section: string,
  startTag: string = START_TAG,
  endTag: string = END_TAG,
): string {
  const block = `${startTag}\n${section.trim()}\n${endTag}`;
  const start = content.indexOf(startTag);
  const end = content.indexOf(endTag);
  if (start !== -1 && end !== -1 && end >= start) {
    return content.slice(0, start) + block + content.slice(end + endTag.length);
  }
  return content.trim() ? `${content.trim()}\n\n${block}\n` : `${block}\n`;
}

function writeOrUpdate(filePath: string, newContent: string): "created" | "updated" | "unchanged" {
  mkdirSync(dirname(filePath), { recursive: true });
  const existing = readFileSafe(filePath);
  if (existing === null) {
    writeFileSync(filePath, newContent, "utf8");
    return "created";
  }
  if (existing === newContent) return "unchanged";
  writeFileSync(filePath, newContent, "utf8");
  return "updated";
}

function writeIfMissing(filePath: string, content: string): "created" | "unchanged" {
  mkdirSync(dirname(filePath), { recursive: true });
  const existing = readFileSafe(filePath);
  if (existing !== null) return "unchanged";
  writeFileSync(filePath, content, "utf8");
  return "created";
}

function updateMarkdownAnchor(
  filePath: string,
  header: string,
  targetDir: string,
  skills?: SkillEntry[],
): "created" | "updated" | "unchanged" {
  mkdirSync(dirname(filePath), { recursive: true });
  const existing = readFileSafe(filePath);
  const content = existing ?? "";
  const skillList = skills && skills.length
    ? `\nKey installed skills (${skills.length} total):\n` +
      skills.slice(0, 15).map((s) => `- \`${s.name}\`: ${s.description.slice(0, 80)}`).join("\n") +
      (skills.length > 15 ? `\n... and ${skills.length - 15} more.` : "")
    : "";

  const section = `## ${header}
Domain scientific research skills are available in \`${targetDir}\`.
Consult the corresponding \`SKILL.md\` before generating code, running simulations, or querying scientific APIs.${skillList}`;

  const updated = updateTaggedSection(content, section);
  if (existing !== null && content === updated) return "unchanged";
  writeFileSync(filePath, updated, "utf8");
  return existing !== null ? "updated" : "created";
}

/**
 * Automatically configure harness integration files in the project workspace.
 */
export function configureHarness(harness: Harness, cwd: string = process.cwd(), skills?: SkillEntry[]): ConfigureResult[] {
  const results: ConfigureResult[] = [];

  switch (harness.id) {
    case "claude-code": {
      const file = join(cwd, "CLAUDE.md");
      const action = updateMarkdownAnchor(file, "Research Agent Skills", harness.project, skills);
      results.push({ file: "CLAUDE.md", action, harness: harness.id });
      break;
    }

    case "claude-science": {
      const claudeMd = join(cwd, "CLAUDE.md");
      const a1 = updateMarkdownAnchor(claudeMd, "Claude Science Research Skills", harness.project, skills);
      results.push({ file: "CLAUDE.md", action: a1, harness: harness.id });

      const specFile = join(cwd, ".claude-science", "specialists.json");
      const specConfig = {
        $schema: "https://claude.ai/schemas/science-specialists.json",
        version: "1.0",
        specialists: {
          genomics: { skillsRoot: harness.project, categories: ["genetics", "biology-research"] },
          cheminformatics: { skillsRoot: harness.project, categories: ["chemistry-research"] },
          literature: { skillsRoot: harness.project, categories: ["literature-review", "research-writing"] },
        },
      };
      const action = writeIfMissing(specFile, JSON.stringify(specConfig, null, 2) + "\n");
      if (action === "created") {
        results.push({ file: ".claude-science/specialists.json", action, harness: harness.id });
      }
      break;
    }

    case "openscience": {
      const file = join(cwd, ".openscience", "skills.json");
      const config = {
        skillsDirectory: harness.project,
        catalogVersion: "1.1.0",
        updatedAt: new Date().toISOString(),
        skills: skills?.map((s) => s.name) ?? [],
      };
      const action = writeOrUpdate(file, JSON.stringify(config, null, 2) + "\n");
      results.push({ file: ".openscience/skills.json", action, harness: harness.id });
      break;
    }

    case "t3-code": {
      const file = join(cwd, ".t3", "config.json");
      const config = {
        $schema: "https://t3.chat/schema/harness.json",
        name: "Scientific Research Workspace",
        skillsRoot: harness.project,
        worktreeSync: true,
        reverseMcp: { enabled: true, skillsDir: harness.project },
      };
      const action = writeIfMissing(file, JSON.stringify(config, null, 2) + "\n");
      if (action === "created") {
        results.push({ file: ".t3/config.json", action, harness: harness.id });
      }
      break;
    }

    case "aider": {
      const file = join(cwd, "CONVENTIONS.md");
      const action = updateMarkdownAnchor(file, "Research Conventions & Skills", harness.project, skills);
      results.push({ file: "CONVENTIONS.md", action, harness: harness.id });
      break;
    }

    case "cursor": {
      const file = join(cwd, ".cursorrules");
      const action = updateMarkdownAnchor(file, "Research Agent Skills", harness.project, skills);
      results.push({ file: ".cursorrules", action, harness: harness.id });
      break;
    }

    case "windsurf": {
      const file = join(cwd, ".windsurfrules");
      const action = updateMarkdownAnchor(file, "Research Agent Skills", harness.project, skills);
      results.push({ file: ".windsurfrules", action, harness: harness.id });
      break;
    }

    case "openhands": {
      const file = join(cwd, ".openhands", "microagents", "repo.md");
      const action = updateMarkdownAnchor(file, "OpenHands Scientific Microagent Skills", harness.project, skills);
      results.push({ file: ".openhands/microagents/repo.md", action, harness: harness.id });
      break;
    }

    case "roo-code": {
      const file = join(cwd, ".roomodes");
      const config = {
        customModes: [
          {
            slug: "scientist",
            name: "Research Scientist",
            roleDefinition: "You are a scientific research agent with access to domain-specific research skills.",
            groups: ["read", "edit", "command"],
            customInstructions: `Consult skills under ${harness.project} before writing code or running experiments.`,
          },
        ],
      };
      const action = writeIfMissing(file, JSON.stringify(config, null, 2) + "\n");
      if (action === "created") {
        results.push({ file: ".roomodes", action, harness: harness.id });
      }
      break;
    }

    case "goose": {
      const file = join(cwd, ".goosehints");
      const action = updateMarkdownAnchor(file, "Goose Research Hints", harness.project, skills);
      results.push({ file: ".goosehints", action, harness: harness.id });
      break;
    }

    default: {
      // General agent harnesses (codex, copilot, gemini-cli, antigravity, opencode, hermes, zed, trae, continue, agents)
      const file = join(cwd, "AGENTS.md");
      const action = updateMarkdownAnchor(file, "Research Agent Skills", harness.project, skills);
      results.push({ file: "AGENTS.md", action, harness: harness.id });
      break;
    }
  }

  return results;
}

export function autoConfigureAll(
  harnesses: Harness[],
  cwd: string = process.cwd(),
  skills?: SkillEntry[],
): ConfigureResult[] {
  const results: ConfigureResult[] = [];
  const handledFiles = new Set<string>();

  for (const h of harnesses) {
    const res = configureHarness(h, cwd, skills);
    for (const r of res) {
      const key = `${r.harness}:${r.file}`;
      if (!handledFiles.has(key)) {
        handledFiles.add(key);
        results.push(r);
      }
    }
  }
  return results;
}
