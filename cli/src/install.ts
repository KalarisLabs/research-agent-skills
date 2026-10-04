import { cpSync, existsSync, lstatSync, mkdirSync, readdirSync, readFileSync, rmSync, symlinkSync, writeFileSync } from "node:fs";
import { join, relative } from "node:path";
import { sha256, type Catalog, type SkillEntry, type Source } from "./source.js";

export const LOCK_NAME = ".research-agent-skills.lock.json";

export interface LockFile {
  tool: "research-agent-skills";
  version: string;
  origin: string;
  updatedAt: string;
  skills: Record<string, { version: string; mode: "copy" | "symlink"; files: Record<string, string> }>;
}

export interface Selection {
  names?: string[];
  categories?: string[];
  bundles?: string[];
  all?: boolean;
}

/** Select skills. */

export function selectSkills(catalog: Catalog & { bundles?: Record<string, { categories: string[]; skills?: string[] }> },
  sel: Selection): SkillEntry[] {
  const byName = new Map(catalog.skills.map((s) => [s.name, s]));
  if (sel.all) return catalog.skills;
  const chosen = new Map<string, SkillEntry>();
  for (const n of sel.names ?? []) {
    const s = byName.get(n);
    if (!s) throw new Error(`unknown skill '${n}' (try: research-agent-skills search ${n})`);
    chosen.set(n, s);
  }
  const cats = new Set(sel.categories ?? []);
  for (const b of sel.bundles ?? []) {
    const bundle = catalog.bundles?.[b];
    if (!bundle) throw new Error(`unknown bundle '${b}'. Known: ${Object.keys(catalog.bundles ?? {}).join(", ")}`);
    bundle.categories.forEach((c) => cats.add(c));
    for (const name of bundle.skills ?? []) {
      const skill = byName.get(name);
      if (!skill) throw new Error(`bundle '${b}' references unknown skill '${name}'`);
      chosen.set(name, skill);
    }
  }
  for (const c of cats) {
    if (!catalog.categories.some((x) => x.id === c)) {
      throw new Error(`unknown category '${c}'. Known: ${catalog.categories.map((x) => x.id).join(", ")}`);
    }
    catalog.skills.filter((s) => s.category === c).forEach((s) => chosen.set(s.name, s));
  }
  return [...chosen.values()].sort((a, b) => a.name.localeCompare(b.name));
}

export function readLock(dir: string): LockFile | undefined {
  const f = join(dir, LOCK_NAME);
  return existsSync(f) ? (JSON.parse(readFileSync(f, "utf8")) as LockFile) : undefined;
}

function writeLock(dir: string, lock: LockFile): void {
  lock.updatedAt = new Date().toISOString();
  writeFileSync(join(dir, LOCK_NAME), JSON.stringify(lock, null, 2) + "\n");
}

/** Hash tree. */

export function hashTree(dir: string): Record<string, string> {
  const out: Record<string, string> = {};
  const walk = (d: string) => {
    for (const entry of readdirSync(d, { withFileTypes: true })) {
      const p = join(d, entry.name);
      if (entry.isDirectory()) walk(p);
      else if (entry.isFile()) out[relative(dir, p).split("\\").join("/")] = sha256(readFileSync(p));
    }
  };
  walk(dir);
  return out;
}

function isSymlink(p: string): boolean {
  try { return lstatSync(p).isSymbolicLink(); } catch { return false; }
}

export interface InstallResult { installed: string[]; updated: string[]; skipped: string[] }

/** Install skills. */

export function installSkills(src: Source, skills: SkillEntry[], targetDir: string,
  opts: { mode: "copy" | "symlink"; force: boolean; dryRun: boolean; log: (m: string) => void }): InstallResult {
  const res: InstallResult = { installed: [], updated: [], skipped: [] };
  const lock: LockFile = readLock(targetDir) ?? { tool: "research-agent-skills", version: src.version, origin: src.origin,
    updatedAt: "", skills: {} };
  if (!opts.dryRun) mkdirSync(targetDir, { recursive: true });
  for (const s of skills) {
    const from = join(src.root, s.path);
    const to = join(targetDir, s.name);
    if (!existsSync(join(from, "SKILL.md"))) throw new Error(`source is missing ${s.path}/SKILL.md`);
    const managed = s.name in lock.skills;
    if (existsSync(to) && !managed && !opts.force) {
      opts.log(`  skip ${s.name}: ${to} exists and was not installed by this tool (use --force to replace)`);
      res.skipped.push(s.name);
      continue;
    }
    (existsSync(to) ? res.updated : res.installed).push(s.name);
    if (opts.dryRun) continue;
    rmSync(to, { recursive: true, force: true });
    let mode = opts.mode;
    if (mode === "symlink") {
      try {
        symlinkSync(from, to, process.platform === "win32" ? "junction" : "dir");
      } catch {
        mode = "copy";
      }
    }
    if (mode === "copy") cpSync(from, to, { recursive: true, dereference: true });
    lock.skills[s.name] = { version: s.version, mode, files: mode === "copy" ? hashTree(to) : {} };
  }
  if (!opts.dryRun) {
    lock.version = src.version;
    lock.origin = src.origin;
    writeLock(targetDir, lock);
  }
  return res;
}

/** Uninstall skills. */

export function uninstallSkills(targetDir: string, names: string[] | "all", dryRun: boolean): string[] {
  const lock = readLock(targetDir);
  if (!lock) return [];
  const victims = names === "all" ? Object.keys(lock.skills) : names.filter((n) => n in lock.skills);
  for (const n of victims) {
    if (!dryRun) rmSync(join(targetDir, n), { recursive: true, force: true });
    delete lock.skills[n];
  }
  if (!dryRun) {
    if (Object.keys(lock.skills).length) writeLock(targetDir, lock);
    else rmSync(join(targetDir, LOCK_NAME), { force: true });
  }
  return victims;
}

export interface IntegrityIssue { skill: string; problem: string }

/** Compare installed copies against the hashes recorded at install time. */
export function verifyInstall(targetDir: string): IntegrityIssue[] {
  const lock = readLock(targetDir);
  if (!lock) return [];
  const issues: IntegrityIssue[] = [];
  for (const [name, info] of Object.entries(lock.skills)) {
    const dir = join(targetDir, name);
    if (!existsSync(dir)) { issues.push({ skill: name, problem: "missing" }); continue; }
    if (info.mode === "symlink" || isSymlink(dir)) continue;
    const now = hashTree(dir);
    for (const [f, h] of Object.entries(info.files)) {
      if (!(f in now)) issues.push({ skill: name, problem: `file removed: ${f}` });
      else if (now[f] !== h) issues.push({ skill: name, problem: `file modified: ${f}` });
    }
    for (const f of Object.keys(now)) if (!(f in info.files)) issues.push({ skill: name, problem: `unexpected file: ${f}` });
  }
  return issues;
}
