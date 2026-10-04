import { spawnSync } from "node:child_process";
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { createInterface } from "node:readline/promises";
import { fileURLToPath } from "node:url";
import { detectHarnesses, harnesses, resolveHarnesses, targetDirs, type Harness } from "./harness.js";
import { readLock, selectSkills, installSkills, uninstallSkills, verifyInstall, type Selection } from "./install.js";
import { resolveSource, REPO_SLUG, type Catalog, type Source } from "./source.js";

const PKG = JSON.parse(readFileSync(join(dirname(fileURLToPath(import.meta.url)), "..", "package.json"), "utf8")) as {
  version: string;
};

const HELP = `research-agent-skills v${PKG.version}
Agent skills for scientific research, paper writing, journal formats and literature review.
By Kalaris Labs - https://github.com/${REPO_SLUG}

Usage:
  npx research-agent-skills                        interactive install
  npx research-agent-skills install [skills...]    install skills (default: research-essentials bundle)
  npx research-agent-skills list [--category c]    list available skills
  npx research-agent-skills search <query>         search skills by name, description, tags
  npx research-agent-skills installed              show what is installed where
  npx research-agent-skills update                 reinstall installed skills at the selected version
  npx research-agent-skills uninstall [skills...]  remove skills installed by this tool (--all for every one)
  npx research-agent-skills doctor                 check harnesses, Python/uv, and installed-file integrity

Selection:
  --bundle <b>        research-essentials, ml-research, ai-research, biology-research,
                      chemistry-research, medicine-research, physics-research
  --category <c>      one or more categories, comma separated (see: list --categories)
  --all               every skill (not recommended: loads many skill descriptions into context)

Targets:
  --harness <h>       auto (default), all, or comma list: ${harnesses().map((h) => h.id).join(", ")}
  --project           install into the current project (default: global, in your home directory)
  --symlink           link instead of copy (copy is default and safest)

Source:
  --version <v>       release to install (default: ${PKG.version}; "latest" queries GitHub)
  --source <dir>      install from a local checkout instead of a GitHub release

Other:
  --force             replace existing folders not installed by this tool
  --dry-run           show what would happen
  -y, --yes           no prompts
  -h, --help          this help`;

interface Args {
  cmd: string;
  positional: string[];
  flags: Record<string, string | boolean>;
}

const BOOL_FLAGS = new Set(["all", "project", "global", "symlink", "copy", "force", "dry-run", "yes", "help", "categories",
  "json"]);

export function parseArgs(argv: string[]): Args {
  const flags: Record<string, string | boolean> = {};
  const positional: string[] = [];
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === "-y") flags.yes = true;
    else if (a === "-h") flags.help = true;
    else if (a.startsWith("--")) {
      const [k, v] = a.slice(2).split("=", 2);
      if (v !== undefined) flags[k] = v;
      else if (BOOL_FLAGS.has(k)) flags[k] = true;
      else if (i + 1 < argv.length && !argv[i + 1].startsWith("-")) flags[k] = argv[++i];
      else throw new Error(`--${k} needs a value`);
    } else positional.push(a);
  }
  const cmd = positional.shift() ?? "";
  return { cmd, positional, flags };
}

const log = (m: string) => process.stdout.write(m + "\n");
const list = (v: string | boolean | undefined) => (typeof v === "string" ? v.split(",").map((s) => s.trim()).filter(Boolean) : []);

async function getSource(a: Args): Promise<Source> {
  return resolveSource({
    source: typeof a.flags.source === "string" ? a.flags.source : undefined,
    version: typeof a.flags.version === "string" ? a.flags.version : PKG.version,
    log,
  });
}

function scopeOf(a: Args): "global" | "project" {
  return a.flags.project ? "project" : "global";
}

async function interactive(catalog: Catalog & { bundles?: Record<string, { description: string; categories: string[]; skills?: string[] }> }):
  Promise<{ sel: Selection; chosen: Harness[] }> {
  const rl = createInterface({ input: process.stdin, output: process.stdout });
  try {
    const options: { label: string; sel: Selection }[] = [
      ...Object.entries(catalog.bundles ?? {}).map(([id, b]) => ({ label: `${id} (bundle) - ${b.description}`, sel: { bundles: [id] } })),
      ...catalog.categories.filter((c) => c.count).map((c) => ({ label: `${c.id} (${c.count}) - ${c.description}`, sel: { categories: [c.id] } })),
    ];
    log("\nWhat would you like to install?\n");
    options.forEach((o, i) => log(`  ${String(i + 1).padStart(2)}. ${o.label}`));
    const answer = (await rl.question("\nNumbers, comma separated [1]: ")).trim() || "1";
    const sel: Selection = { bundles: [], categories: [] };
    for (const part of answer.split(",")) {
      const o = options[Number(part.trim()) - 1];
      if (!o) throw new Error(`invalid choice '${part}'`);
      sel.bundles!.push(...(o.sel.bundles ?? []));
      sel.categories!.push(...(o.sel.categories ?? []));
    }
    const detected = detectHarnesses();
    const all = harnesses();
    log("\nInstall for which agents?\n");
    all.forEach((h, i) => log(`  ${String(i + 1).padStart(2)}. ${h.label}${detected.some((d) => d.id === h.id) ? "  (detected)" : ""}`));
    const def = detected.length ? detected.map((d) => all.indexOf(d) + 1).join(",") : "1";
    const hAns = (await rl.question(`\nNumbers, comma separated [${def}]: `)).trim() || def;
    const chosen = hAns.split(",").map((p) => {
      const h = all[Number(p.trim()) - 1];
      if (!h) throw new Error(`invalid choice '${p}'`);
      return h;
    });
    return { sel, chosen };
  } finally {
    rl.close();
  }
}

async function cmdInstall(a: Args): Promise<number> {
  const src = await getSource(a);
  const catalog = src.catalog as Catalog & { bundles?: Record<string, { description: string; categories: string[]; skills?: string[] }> };
  let sel: Selection = { names: a.positional, categories: list(a.flags.category), bundles: list(a.flags.bundle),
    all: Boolean(a.flags.all) };
  let chosen: Harness[];
  const nothingSelected = !sel.names!.length && !sel.categories!.length && !sel.bundles!.length && !sel.all;
  if (nothingSelected && !a.flags.yes && process.stdin.isTTY && a.cmd === "") {
    ({ sel, chosen } = await interactive(catalog));
  } else {
    if (nothingSelected) sel = { bundles: ["research-essentials"] };
    chosen = resolveHarnesses(typeof a.flags.harness === "string" ? a.flags.harness : undefined);
  }
  const skills = selectSkills(catalog, sel);
  const mode = a.flags.symlink ? "symlink" : "copy";
  const dirs = targetDirs(chosen, scopeOf(a));
  log(`\nInstalling ${skills.length} skill(s) from v${src.version} for ${chosen.map((h) => h.label).join(", ")}`);
  for (const dir of dirs) {
    const r = installSkills(src, skills, dir, { mode, force: Boolean(a.flags.force), dryRun: Boolean(a.flags["dry-run"]), log });
    log(`  ${dir}: ${r.installed.length} installed, ${r.updated.length} updated, ${r.skipped.length} skipped`);
  }
  const needsPython = skills.filter((s) => s.has_scripts).length;
  if (needsPython) log(`\n${needsPython} of these skills include Python scripts; run \`research-agent-skills doctor\` to check Python/uv.`);
  log(a.flags["dry-run"] ? "\nDry run: nothing was written." : "\nDone. Restart your agent to load new skills.");
  return 0;
}

async function cmdList(a: Args): Promise<number> {
  const { catalog } = await getSource(a);
  if (a.flags.categories) {
    catalog.categories.forEach((c) => log(`${c.id.padEnd(32)} ${String(c.count).padStart(3)}  ${c.description}`));
    return 0;
  }
  const cats = list(a.flags.category);
  const skills = catalog.skills.filter((s) => !cats.length || cats.includes(s.category));
  if (a.flags.json) { log(JSON.stringify(skills, null, 2)); return 0; }
  skills.forEach((s) => log(`${s.name.padEnd(40)} ${s.category.padEnd(30)} ${s.description.slice(0, 80)}`));
  log(`\n${skills.length} skills`);
  return 0;
}

async function cmdSearch(a: Args): Promise<number> {
  const { catalog } = await getSource(a);
  const terms = a.positional.map((t) => t.toLowerCase());
  if (!terms.length) throw new Error("usage: research-agent-skills search <query>");
  const scored = catalog.skills.map((s) => {
    const hay = `${s.name} ${s.description} ${s.tags.join(" ")} ${s.category}`.toLowerCase();
    const score = terms.reduce((n, t) => n + (s.name.includes(t) ? 5 : 0) + (hay.includes(t) ? 1 : 0), 0);
    return { s, score };
  }).filter((x) => x.score > 0 && terms.every((t) => `${x.s.name} ${x.s.description} ${x.s.tags.join(" ")}`.toLowerCase().includes(t)));
  scored.sort((x, y) => y.score - x.score).slice(0, 25)
    .forEach(({ s }) => log(`${s.name.padEnd(40)} ${s.description.slice(0, 100)}`));
  if (!scored.length) log("no matches");
  return 0;
}

function allTargetDirs(a: Args): string[] {
  const hs = typeof a.flags.harness === "string" ? resolveHarnesses(a.flags.harness) : harnesses();
  return targetDirs(hs, scopeOf(a));
}

async function cmdInstalled(a: Args): Promise<number> {
  let any = false;
  for (const dir of allTargetDirs(a)) {
    const lock = readLock(dir);
    if (!lock) continue;
    any = true;
    log(`${dir}  (v${lock.version})\n  ${Object.keys(lock.skills).sort().join(", ")}`);
  }
  if (!any) log("No skills installed by research-agent-skills were found.");
  return 0;
}

async function cmdUpdate(a: Args): Promise<number> {
  const src = await getSource(a);
  for (const dir of allTargetDirs(a)) {
    const lock = readLock(dir);
    if (!lock) continue;
    const names = Object.keys(lock.skills).filter((n) => src.catalog.skills.some((s) => s.name === n));
    const skills = selectSkills(src.catalog, { names });
    const mode = Object.values(lock.skills)[0]?.mode ?? "copy";
    const r = installSkills(src, skills, dir, { mode, force: false, dryRun: Boolean(a.flags["dry-run"]), log });
    log(`${dir}: ${r.updated.length} updated to v${src.version}`);
  }
  return 0;
}

async function cmdUninstall(a: Args): Promise<number> {
  const names = a.flags.all ? "all" : a.positional;
  if (names !== "all" && !names.length) throw new Error("name the skills to remove, or pass --all");
  for (const dir of allTargetDirs(a)) {
    const removed = uninstallSkills(dir, names, Boolean(a.flags["dry-run"]));
    if (removed.length) log(`${dir}: removed ${removed.join(", ")}`);
  }
  return 0;
}

function version(cmd: string, args: string[]): string | undefined {
  const r = spawnSync(cmd, args, { encoding: "utf8", shell: process.platform === "win32" });
  return r.status === 0 ? (r.stdout || r.stderr).trim().split("\n")[0] : undefined;
}

async function cmdDoctor(a: Args): Promise<number> {
  let problems = 0;
  log(`research-agent-skills ${PKG.version} on Node ${process.version} (${process.platform})`);
  const detected = detectHarnesses();
  log(`Agents detected: ${detected.length ? detected.map((h) => h.label).join(", ") : "none (use --harness to choose)"}`);
  const py = version("python3", ["--version"]) ?? version("python", ["--version"]);
  const uv = version("uv", ["--version"]);
  log(`Python: ${py ?? "not found"}   uv: ${uv ?? "not found"}`);
  if (!py && !uv) log("  Skills with scripts/ need Python 3.11+; install uv: https://docs.astral.sh/uv/");
  for (const dir of allTargetDirs(a)) {
    const lock = readLock(dir);
    if (!lock) continue;
    const issues = verifyInstall(dir);
    log(`${dir}: ${Object.keys(lock.skills).length} skills, ${issues.length ? `${issues.length} integrity issue(s)` : "integrity OK"}`);
    issues.slice(0, 20).forEach((i) => log(`  ! ${i.skill}: ${i.problem}`));
    problems += issues.length;
  }
  return problems ? 1 : 0;
}

export async function main(argv: string[] = process.argv.slice(2)): Promise<number> {
  if (argv.length === 1 && (argv[0] === "--version" || argv[0] === "-v")) { log(PKG.version); return 0; }
  const a = parseArgs(argv);
  if (a.flags.help || a.cmd === "help") { log(HELP); return 0; }
  switch (a.cmd) {
    case "":
    case "install":
    case "add": return cmdInstall(a);
    case "list":
    case "ls": return cmdList(a);
    case "search": return cmdSearch(a);
    case "installed": return cmdInstalled(a);
    case "update":
    case "upgrade": return cmdUpdate(a);
    case "uninstall":
    case "remove": return cmdUninstall(a);
    case "doctor": return cmdDoctor(a);
    default:
      log(`unknown command '${a.cmd}'\n`);
      log(HELP);
      return 2;
  }
}
