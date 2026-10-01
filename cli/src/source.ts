/**
 * Resolve a verified local copy of the skills repository.
 *
 * Default: download the signed-off release tarball for a pinned version from
 * GitHub Releases, verify it against the release SHA256SUMS, and extract it
 * into a per-version cache. `--source <dir>` uses a local checkout instead.
 */
import { createHash } from "node:crypto";
import { existsSync, mkdirSync, readFileSync, renameSync, rmSync, writeFileSync } from "node:fs";
import { homedir } from "node:os";
import { join, resolve } from "node:path";
import { extractEntries, readTar } from "./tar.js";

export const REPO_SLUG = "KalarisLabs/research-agent-skills";
const UA = "research-agent-skills-cli";

export interface SkillEntry {
  name: string;
  description: string;
  category: string;
  version: string;
  license: string;
  path: string;
  has_scripts: boolean;
  tags: string[];
}

export interface Catalog {
  name: string;
  version: string;
  categories: { id: string; description: string; count: number }[];
  skills: SkillEntry[];
}

export interface Source {
  root: string;
  version: string;
  catalog: Catalog;
  origin: string;
}

export function cacheRoot(env: NodeJS.ProcessEnv = process.env): string {
  if (env.RESEARCH_AGENT_SKILLS_CACHE) return env.RESEARCH_AGENT_SKILLS_CACHE;
  if (process.platform === "win32" && env.LOCALAPPDATA) return join(env.LOCALAPPDATA, "research-agent-skills");
  return join(env.XDG_CACHE_HOME ?? join(homedir(), ".cache"), "research-agent-skills");
}

export function sha256(data: Buffer): string {
  return createHash("sha256").update(data).digest("hex");
}

/** Parse `sha256sum` output into { filename: hash }. */
export function parseSums(text: string): Record<string, string> {
  const out: Record<string, string> = {};
  for (const line of text.split(/\r?\n/)) {
    const m = line.trim().match(/^([0-9a-f]{64})\s+\*?(.+)$/i);
    if (m) out[m[2].trim()] = m[1].toLowerCase();
  }
  return out;
}

export function loadCatalog(root: string): Catalog {
  const file = join(root, "catalog", "skills.json");
  if (!existsSync(file)) throw new Error(`not a research-agent-skills checkout (missing catalog/skills.json): ${root}`);
  return JSON.parse(readFileSync(file, "utf8")) as Catalog;
}

async function fetchBuffer(url: string): Promise<Buffer> {
  const res = await fetch(url, { headers: { "User-Agent": UA }, redirect: "follow" });
  if (!res.ok) throw new Error(`download failed (${res.status} ${res.statusText}): ${url}`);
  return Buffer.from(await res.arrayBuffer());
}

export async function latestVersion(): Promise<string> {
  const res = await fetch(`https://api.github.com/repos/${REPO_SLUG}/releases/latest`, {
    headers: { "User-Agent": UA, Accept: "application/vnd.github+json" },
  });
  if (!res.ok) throw new Error(`could not resolve latest release (${res.status})`);
  const tag = ((await res.json()) as { tag_name: string }).tag_name;
  return tag.replace(/^v/, "");
}

export async function resolveSource(opts: { source?: string; version: string; log: (m: string) => void }): Promise<Source> {
  if (opts.source) {
    const root = resolve(opts.source);
    const catalog = loadCatalog(root);
    return { root, version: catalog.version, catalog, origin: `local:${root}` };
  }
  const version = opts.version === "latest" ? await latestVersion() : opts.version.replace(/^v/, "");
  const dir = join(cacheRoot(), version);
  if (existsSync(join(dir, ".verified"))) {
    return { root: dir, version, catalog: loadCatalog(dir), origin: `cache:${dir}` };
  }
  const base = process.env.RAS_BASE_URL ?? `https://github.com/${REPO_SLUG}/releases/download/v${version}`;
  const asset = `research-agent-skills-${version}.tar.gz`;
  opts.log(`Downloading ${asset} ...`);
  const [tarball, sums] = await Promise.all([fetchBuffer(`${base}/${asset}`), fetchBuffer(`${base}/SHA256SUMS`)]);
  const expected = parseSums(sums.toString("utf8"))[asset];
  if (!expected) throw new Error(`SHA256SUMS for v${version} has no entry for ${asset}`);
  const actual = sha256(tarball);
  if (actual !== expected) throw new Error(`checksum mismatch for ${asset}: expected ${expected}, got ${actual}`);
  opts.log(`Verified SHA-256 ${actual.slice(0, 16)}...`);

  const tmp = `${dir}.tmp-${process.pid}`;
  rmSync(tmp, { recursive: true, force: true });
  mkdirSync(tmp, { recursive: true });
  const allowed = /^(skills\/|catalog\/|LICENSE$|THIRD_PARTY_NOTICES\.md$|LICENSES\/|VERSION$)/;
  extractEntries(readTar(tarball), tmp, 1, (rel) => allowed.test(rel));
  writeFileSync(join(tmp, ".verified"), `${actual}\n`);
  rmSync(dir, { recursive: true, force: true });
  renameSync(tmp, dir);
  return { root: dir, version, catalog: loadCatalog(dir), origin: `${base}/${asset}` };
}
