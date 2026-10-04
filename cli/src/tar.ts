/**
 * Minimal, defensive tar reader (ustar + GNU long names + pax path headers).
 * Only regular files and directories are materialized; links, devices and any
 * entry that would escape the destination are rejected.
 */
import { mkdirSync, writeFileSync } from "node:fs";
import { dirname, isAbsolute, normalize, resolve, sep } from "node:path";
import { gunzipSync } from "node:zlib";

export interface TarEntry {
  path: string;
  type: "file" | "dir";
  data: Buffer;
}

export interface ExtractLimits {
  maxEntries: number;
  maxTotalBytes: number;
  maxFileBytes: number;
}

export const DEFAULT_LIMITS: ExtractLimits = {
  maxEntries: 20_000,
  maxTotalBytes: 512 * 1024 * 1024,
  maxFileBytes: 16 * 1024 * 1024,
};

function cstr(buf: Buffer, start: number, len: number): string {
  const slice = buf.subarray(start, start + len);
  const nul = slice.indexOf(0);
  return slice.subarray(0, nul === -1 ? slice.length : nul).toString("utf8");
}

function octal(buf: Buffer, start: number, len: number): number {
  const s = cstr(buf, start, len).trim();
  return s ? parseInt(s, 8) : 0;
}

function parsePax(data: Buffer): Record<string, string> {
  const out: Record<string, string> = {};
  let i = 0;
  while (i < data.length) {
    const space = data.indexOf(0x20, i);
    if (space === -1) break;
    const len = parseInt(data.subarray(i, space).toString("utf8"), 10);
    if (!Number.isFinite(len) || len <= 0) break;
    const record = data.subarray(space + 1, i + len - 1).toString("utf8");
    const eq = record.indexOf("=");
    if (eq > 0) out[record.slice(0, eq)] = record.slice(eq + 1);
    i += len;
  }
  return out;
}

/** Parse a (gzipped) tarball into entries without touching the filesystem. */
export function readTar(input: Buffer, limits: ExtractLimits = DEFAULT_LIMITS): TarEntry[] {
  const buf = input[0] === 0x1f && input[1] === 0x8b ? gunzipSync(input, { maxOutputLength: limits.maxTotalBytes }) : input;
  const entries: TarEntry[] = [];
  let offset = 0;
  let longName: string | undefined;
  let paxPath: string | undefined;
  let total = 0;
  while (offset + 512 <= buf.length) {
    const header = buf.subarray(offset, offset + 512);
    if (header.every((b) => b === 0)) break;
    const size = octal(header, 124, 12);
    const typeflag = String.fromCharCode(header[156] || 0x30);
    const prefix = cstr(header, 345, 155);
    let name = cstr(header, 0, 100);
    if (prefix) name = `${prefix}/${name}`;
    const dataStart = offset + 512;
    const data = buf.subarray(dataStart, dataStart + size);
    offset = dataStart + Math.ceil(size / 512) * 512;

    if (typeflag === "L") { longName = cstr(data, 0, data.length); continue; }
    if (typeflag === "x") { paxPath = parsePax(data).path; continue; }
    if (typeflag === "g") continue; // global pax header (e.g. git commit id)
    const path = paxPath ?? longName ?? name;
    longName = undefined;
    paxPath = undefined;

    if (typeflag === "5") { entries.push({ path, type: "dir", data: Buffer.alloc(0) }); continue; }
    if (typeflag !== "0" && typeflag !== "\0" && typeflag !== "7") {
      throw new Error(`refusing tar entry of type '${typeflag}' (${path}): only regular files are allowed`);
    }
    if (size > limits.maxFileBytes) throw new Error(`tar entry too large: ${path}`);
    total += size;
    if (total > limits.maxTotalBytes) throw new Error("tarball exceeds size limit");
    entries.push({ path, type: "file", data: Buffer.from(data) });
    if (entries.length > limits.maxEntries) throw new Error("tarball has too many entries");
  }
  return entries;
}

/** Resolve an archive path under dest, or throw if it is absolute or escapes dest. */
export function safeJoin(dest: string, entryPath: string): string {
  const cleaned = entryPath.replace(/\\/g, "/");
  if (isAbsolute(cleaned) || /^[a-zA-Z]:/.test(cleaned) || cleaned.split("/").includes("..")) {
    throw new Error(`unsafe path in archive: ${entryPath}`);
  }
  const root = resolve(dest);
  const target = resolve(root, normalize(cleaned));
  if (target !== root && !target.startsWith(root + sep)) throw new Error(`unsafe path in archive: ${entryPath}`);
  return target;
}

/** Extract entries, stripping `strip` leading path components (like tar --strip-components). */
export function extractEntries(entries: TarEntry[], dest: string, strip = 1, filter?: (rel: string) => boolean): number {
  let count = 0;
  for (const e of entries) {
    const rel = e.path.replace(/\\/g, "/").split("/").filter(Boolean).slice(strip).join("/");
    if (!rel || (filter && !filter(rel))) continue;
    const target = safeJoin(dest, rel);
    if (e.type === "dir") { mkdirSync(target, { recursive: true }); continue; }
    mkdirSync(dirname(target), { recursive: true });
    writeFileSync(target, e.data);
    count++;
  }
  return count;
}

