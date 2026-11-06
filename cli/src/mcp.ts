import { spawnSync } from "node:child_process";
import { existsSync, readdirSync, readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { createInterface } from "node:readline";
import { fileURLToPath } from "node:url";
import { onPath, resolveHarnesses, targetDirs } from "./harness.js";
import { installSkills, selectSkills } from "./install.js";
import { resolveSource, type Catalog, type Source } from "./source.js";

const PKG = JSON.parse(
  readFileSync(join(dirname(fileURLToPath(import.meta.url)), "..", "package.json"), "utf8"),
) as { version: string; name: string };

interface JsonRpcRequest {
  jsonrpc: "2.0";
  id?: number | string | null;
  method: string;
  params?: Record<string, unknown>;
}

interface JsonRpcResponse {
  jsonrpc: "2.0";
  id?: number | string | null;
  result?: unknown;
  error?: { code: number; message: string; data?: unknown };
}

export const TOOLS = [
  {
    name: "search_skills",
    description: "Search 280+ scientific research agent skills by keywords, domains, or categories.",
    inputSchema: {
      type: "object",
      properties: {
        query: {
          type: "string",
          description: "Search keywords (e.g. 'alphafold', 'chembl', 'systematic review', 'docking', 'genome')",
        },
        category: {
          type: "string",
          description: "Optional category filter (e.g. 'genetics', 'chemistry-research', 'literature-review')",
        },
      },
      required: ["query"],
    },
  },
  {
    name: "get_skill",
    description: "Retrieve full instructions, documentation (SKILL.md), and helper scripts for a specific research agent skill.",
    inputSchema: {
      type: "object",
      properties: {
        name: {
          type: "string",
          description: "Exact name of the skill (e.g. 'chembl-database', 'alphafold-database-fetch-and-analyze')",
        },
      },
      required: ["name"],
    },
  },
  {
    name: "list_bundles",
    description: "List curated scientific skill bundles across biology, chemistry, medicine, physics, and ML research.",
    inputSchema: {
      type: "object",
      properties: {},
    },
  },
  {
    name: "list_skills",
    description: "List available scientific skills, optionally filtered by category or bundle.",
    inputSchema: {
      type: "object",
      properties: {
        category: { type: "string", description: "Filter by category ID" },
        bundle: { type: "string", description: "Filter by bundle ID (e.g. 'research-essentials', 'biology-research')" },
      },
    },
  },
  {
    name: "install_skills",
    description: "Install one or more scientific skills into an agent harness.",
    inputSchema: {
      type: "object",
      properties: {
        skills: {
          type: "array",
          items: { type: "string" },
          description: "List of skill names to install",
        },
        harness: {
          type: "string",
          description: "Target harness ID or 'auto' (e.g. 'claude-science', 't3-code', 'antigravity', 'cursor', 'codex')",
        },
        project: {
          type: "boolean",
          description: "If true, install into current project directory instead of user home",
        },
      },
      required: ["skills"],
    },
  },
  {
    name: "run_skill_script",
    description: "Execute a Python script bundled inside a research agent skill with parameters and timeout protection.",
    inputSchema: {
      type: "object",
      properties: {
        skill: {
          type: "string",
          description: "Name of the skill, e.g. 'chembl-database', 'alphafold-database-fetch-and-analyze', 'pubmed-database'",
        },
        script: {
          type: "string",
          description: "Filename of the script inside the skill's scripts/ directory, e.g. 'query_chembl.py'",
        },
        args: {
          type: "array",
          items: { type: "string" },
          description: "CLI arguments to pass to the script, e.g. ['--help']",
        },
        timeout_seconds: {
          type: "number",
          description: "Timeout in seconds (default 30, max 120)",
        },
      },
      required: ["skill", "script"],
    },
  },
];

export async function runMcpServer(sourceOpts: { source?: string; version?: string } = {}): Promise<void> {
  const logErr = (m: string) => process.stderr.write(`[research-agent-skills-mcp] ${m}\n`);
  const src: Source = await resolveSource({
    source: sourceOpts.source,
    version: sourceOpts.version ?? PKG.version,
    log: logErr,
  });
  const catalog = src.catalog as Catalog & {
    bundles?: Record<string, { description: string; categories: string[]; skills?: string[] }>;
  };

  const send = (res: JsonRpcResponse) => {
    process.stdout.write(JSON.stringify(res) + "\n");
  };

  const handleToolCall = (name: string, args: Record<string, unknown> = {}): { text: string } => {
    switch (name) {
      case "search_skills": {
        const query = String(args.query || "").toLowerCase();
        const category = args.category ? String(args.category).toLowerCase() : undefined;
        const terms = query.split(/\s+/).filter(Boolean);

        const scored = catalog.skills
          .filter((s) => !category || s.category.toLowerCase() === category)
          .map((s) => {
            const hay = `${s.name} ${s.description} ${s.tags.join(" ")} ${s.category}`.toLowerCase();
            const score = terms.reduce(
              (n, t) => n + (s.name.includes(t) ? 5 : 0) + (hay.includes(t) ? 1 : 0),
              0,
            );
            return { s, score };
          })
          .filter(
            (x) =>
              x.score > 0 &&
              terms.every((t) =>
                `${x.s.name} ${x.s.description} ${x.s.tags.join(" ")}`.toLowerCase().includes(t),
              ),
          )
          .sort((a, b) => b.score - a.score)
          .slice(0, 20);

        return {
          text: JSON.stringify(
            {
              matches_count: scored.length,
              skills: scored.map(({ s }) => ({
                name: s.name,
                category: s.category,
                description: s.description,
                tags: s.tags,
                has_scripts: s.has_scripts,
              })),
            },
            null,
            2,
          ),
        };
      }

      case "get_skill": {
        const skillName = String(args.name || "").trim();
        const entry = catalog.skills.find((s) => s.name === skillName);
        if (!entry) throw new Error(`Skill '${skillName}' not found in catalog.`);

        const skillDir = join(src.root, entry.path);
        const skillMdPath = join(skillDir, "SKILL.md");
        const skillMd = existsSync(skillMdPath) ? readFileSync(skillMdPath, "utf8") : "";

        let scripts: string[] = [];
        const scriptsDir = join(skillDir, "scripts");
        if (existsSync(scriptsDir)) {
          scripts = readdirSync(scriptsDir);
        }

        let references: string[] = [];
        const refsDir = join(skillDir, "references");
        if (existsSync(refsDir)) {
          references = readdirSync(refsDir);
        }

        return {
          text: JSON.stringify(
            {
              name: entry.name,
              category: entry.category,
              description: entry.description,
              has_scripts: entry.has_scripts,
              scripts,
              references,
              skill_markdown: skillMd,
            },
            null,
            2,
          ),
        };
      }

      case "list_bundles": {
        return {
          text: JSON.stringify(
            {
              bundles: catalog.bundles ?? {},
            },
            null,
            2,
          ),
        };
      }

      case "list_skills": {
        const cat = args.category ? String(args.category) : undefined;
        const b = args.bundle ? String(args.bundle) : undefined;
        let skills = catalog.skills;

        if (cat) {
          skills = skills.filter((s) => s.category === cat);
        }
        if (b && catalog.bundles?.[b]) {
          const bundle = catalog.bundles[b];
          const cats = new Set(bundle.categories);
          const direct = new Set(bundle.skills ?? []);
          skills = skills.filter((s) => cats.has(s.category) || direct.has(s.name));
        }

        return {
          text: JSON.stringify(
            {
              count: skills.length,
              skills: skills.map((s) => ({
                name: s.name,
                category: s.category,
                description: s.description,
                has_scripts: s.has_scripts,
              })),
            },
            null,
            2,
          ),
        };
      }

      case "install_skills": {
        const skillNames = Array.isArray(args.skills) ? (args.skills as string[]) : [];
        if (!skillNames.length) throw new Error("No skills specified.");
        const harnessSpec = typeof args.harness === "string" ? args.harness : "auto";
        const scope = args.project ? "project" : "global";

        const selected = selectSkills(catalog, { names: skillNames });
        const chosenHarnesses = resolveHarnesses(harnessSpec);
        const dirs = targetDirs(chosenHarnesses, scope);

        const results: Record<string, unknown> = {};
        for (const dir of dirs) {
          const r = installSkills(src, selected, dir, {
            mode: "copy",
            force: false,
            dryRun: false,
            log: (m) => logErr(m),
          });
          results[dir] = r;
        }

        return {
          text: JSON.stringify(
            {
              installed_count: selected.length,
              harnesses: chosenHarnesses.map((h) => h.label),
              targets: results,
            },
            null,
            2,
          ),
        };
      }

      case "run_skill_script": {
        const skillName = String(args.skill || "").trim();
        const scriptName = String(args.script || "").trim();
        const scriptArgs = Array.isArray(args.args) ? args.args.map(String) : [];
        const timeoutSec = Math.min(Math.max(Number(args.timeout_seconds || 30), 1), 120);

        if (!skillName) throw new Error("Argument 'skill' is required.");
        if (!scriptName) throw new Error("Argument 'script' is required.");
        if (scriptName.includes("..") || scriptName.includes("/") || scriptName.includes("\\")) {
          throw new Error("Invalid script name: path traversal is not permitted.");
        }

        const entry = catalog.skills.find((s) => s.name === skillName);
        if (!entry) throw new Error(`Skill '${skillName}' not found in catalog.`);

        const skillDir = join(src.root, entry.path);
        const scriptFile = join(skillDir, "scripts", scriptName);
        if (!existsSync(scriptFile)) {
          throw new Error(`Script '${scriptName}' does not exist in skill '${skillName}/scripts/'.`);
        }

        const startTime = Date.now();
        let cmd = "python";
        let spawnArgs: string[] = [];

        if (onPath("uv")) {
          cmd = "uv";
          spawnArgs = ["run", "python", scriptFile, ...scriptArgs];
        } else if (onPath("python3")) {
          cmd = "python3";
          spawnArgs = [scriptFile, ...scriptArgs];
        } else {
          cmd = "python";
          spawnArgs = [scriptFile, ...scriptArgs];
        }

        const proc = spawnSync(cmd, spawnArgs, {
          cwd: skillDir,
          timeout: timeoutSec * 1000,
          encoding: "utf8",
          maxBuffer: 10 * 1024 * 1024,
          // Never use a shell: args come from the model and cmd.exe would interpret metacharacters.
          shell: false,
          env: { ...process.env, PYTHONUNBUFFERED: "1" },
        });

        const executionTimeMs = Date.now() - startTime;
        const timedOut = Boolean(proc.error && (proc.error as { code?: string }).code === "ETIMEDOUT");

        return {
          text: JSON.stringify(
            {
              skill: skillName,
              script: scriptName,
              command: `${cmd} ${spawnArgs.join(" ")}`,
              exit_code: proc.status,
              execution_time_ms: executionTimeMs,
              timed_out: timedOut,
              stdout: proc.stdout || "",
              stderr: proc.stderr || (proc.error ? proc.error.message : ""),
            },
            null,
            2,
          ),
        };
      }

      default:
        throw new Error(`Unknown tool: ${name}`);
    }
  };

  const rl = createInterface({ input: process.stdin, terminal: false });

  rl.on("line", (line) => {
    const trimmed = line.trim();
    if (!trimmed) return;
    let req: JsonRpcRequest;
    try {
      req = JSON.parse(trimmed) as JsonRpcRequest;
    } catch {
      send({ jsonrpc: "2.0", id: null, error: { code: -32700, message: "Parse error" } });
      return;
    }

    if (!req.method) {
      if (req.id !== undefined) {
        send({ jsonrpc: "2.0", id: req.id, error: { code: -32600, message: "Invalid Request" } });
      }
      return;
    }

    // Notifications require no response
    if (req.method === "notifications/initialized") {
      logErr("Client initialized session");
      return;
    }

    try {
      switch (req.method) {
        case "initialize": {
          send({
            jsonrpc: "2.0",
            id: req.id,
            result: {
              protocolVersion: "2024-11-05",
              capabilities: {
                tools: {},
                resources: {},
              },
              serverInfo: {
                name: "research-agent-skills-mcp",
                version: PKG.version,
              },
            },
          });
          break;
        }

        case "ping": {
          send({ jsonrpc: "2.0", id: req.id, result: {} });
          break;
        }

        case "tools/list": {
          send({
            jsonrpc: "2.0",
            id: req.id,
            result: {
              tools: TOOLS,
            },
          });
          break;
        }

        case "tools/call": {
          const params = req.params as { name: string; arguments?: Record<string, unknown> };
          const res = handleToolCall(params.name, params.arguments);
          send({
            jsonrpc: "2.0",
            id: req.id,
            result: {
              content: [
                {
                  type: "text",
                  text: res.text,
                },
              ],
            },
          });
          break;
        }

        case "resources/list": {
          const sample = catalog.skills.slice(0, 30).map((s) => ({
            uri: `skill://${s.name}`,
            name: `${s.name} documentation`,
            description: s.description,
            mimeType: "text/markdown",
          }));
          send({
            jsonrpc: "2.0",
            id: req.id,
            result: {
              resources: sample,
            },
          });
          break;
        }

        case "resources/read": {
          const params = req.params as { uri: string };
          const uri = params?.uri || "";
          if (uri.startsWith("skill://")) {
            const skillName = uri.replace("skill://", "").trim();
            const entry = catalog.skills.find((s) => s.name === skillName);
            if (!entry) throw new Error(`Resource '${uri}' not found.`);
            const skillMdPath = join(src.root, entry.path, "SKILL.md");
            const content = existsSync(skillMdPath) ? readFileSync(skillMdPath, "utf8") : "";
            send({
              jsonrpc: "2.0",
              id: req.id,
              result: {
                contents: [
                  {
                    uri,
                    mimeType: "text/markdown",
                    text: content,
                  },
                ],
              },
            });
          } else {
            throw new Error(`Unsupported URI schema: ${uri}`);
          }
          break;
        }

        default: {
          send({
            jsonrpc: "2.0",
            id: req.id,
            error: { code: -32601, message: `Method '${req.method}' not found` },
          });
          break;
        }
      }
    } catch (err: unknown) {
      const msg = err instanceof Error ? err.message : String(err);
      send({
        jsonrpc: "2.0",
        id: req.id,
        error: { code: -32000, message: msg },
      });
    }
  });

  return new Promise(() => { });
}
