// Property-based fuzz tests (fast-check) for the parsers that handle untrusted input:
// downloaded tarballs, archive entry paths, SHA256SUMS files and command-line arguments.
import assert from "node:assert/strict";
import { tmpdir } from "node:os";
import { join, resolve, sep } from "node:path";
import { test } from "node:test";
import { gzipSync } from "node:zlib";
import fc from "fast-check";

import { parseArgs } from "../dist/cli.js";
import { parseSums } from "../dist/source.js";
import { readTar, safeJoin } from "../dist/tar.js";

const RUNS = Number(process.env.FUZZ_RUNS ?? 500);
const dest = join(tmpdir(), "ras-fuzz-dest");

/** Path segments biased toward traversal tricks. */
const segment = fc.oneof(
  fc.constantFrom("..", ".", "", "~", "C:", "c:", "\\", "..\\..", "%2e%2e", "\0", "skills", "SKILL.md"),
  fc.string({ maxLength: 12 }),
);
const archivePath = fc.oneof(
  fc.array(segment, { maxLength: 8 }).map((parts) => parts.join("/")),
  fc.array(segment, { maxLength: 8 }).map((parts) => parts.join("\\")),
  fc.array(segment, { maxLength: 8 }).map((parts) => "/" + parts.join("/")),
  fc.string({ maxLength: 64 }),
);

test("fuzz safeJoin: a returned path never escapes the destination", () => {
  const root = resolve(dest);
  fc.assert(
    fc.property(archivePath, (p) => {
      let target;
      try {
        target = safeJoin(dest, p);
      } catch (e) {
        assert.ok(e instanceof Error);
        return;
      }
      assert.ok(target === root || target.startsWith(root + sep), `${JSON.stringify(p)} -> ${target}`);
    }),
    { numRuns: RUNS * 4 },
  );
});

test("fuzz readTar: arbitrary bytes either parse or throw an Error", () => {
  const limits = { maxEntries: 50, maxFileBytes: 1 << 16, maxTotalBytes: 1 << 18 };
  const bytes = fc.uint8Array({ maxLength: 4096 });
  const input = fc.oneof(bytes, bytes.map((b) => gzipSync(b)));
  fc.assert(
    fc.property(input, (b) => {
      let entries;
      try {
        entries = readTar(Buffer.from(b), limits);
      } catch (e) {
        assert.ok(e instanceof Error); // rejected input: only the parser's own errors are acceptable
        return;
      }
      // Assertions run outside the try block so a violated limit fails the property.
      assert.ok(entries.length <= limits.maxEntries);
      for (const e of entries) assert.ok(e.data.length <= limits.maxFileBytes);
    }),
    { numRuns: RUNS },
  );
});

test("fuzz parseSums: only well-formed hashes are returned, lowercased", () => {
  const hash = fc.stringMatching(/^[0-9a-fA-F]{64}$/);
  const line = fc.oneof(
    fc.string({ maxLength: 120 }),
    fc.tuple(hash, fc.constantFrom(" ", "  ", " *"), fc.string({ minLength: 1, maxLength: 40 })).map(([h, s, n]) => h + s + n),
  );
  fc.assert(
    fc.property(fc.array(line, { maxLength: 20 }), fc.constantFrom("\n", "\r\n"), (lines, eol) => {
      const sums = parseSums(lines.join(eol));
      for (const [name, h] of Object.entries(sums)) {
        assert.match(h, /^[0-9a-f]{64}$/);
        assert.equal(name, name.trim());
      }
    }),
    { numRuns: RUNS },
  );
});

test("fuzz parseArgs: arbitrary argv never crashes with a non-Error", () => {
  const arg = fc.oneof(
    fc.constantFrom("-y", "-h", "--yes", "--global", "--skill", "--agent", "--agent=", "--=", "--", "-", "add", "list", "update"),
    fc.string({ maxLength: 20 }).map((s) => "--" + s),
    fc.string({ maxLength: 20 }),
  );
  fc.assert(
    fc.property(fc.array(arg, { maxLength: 10 }), (argv) => {
      try {
        parseArgs(argv);
      } catch (e) {
        assert.ok(e instanceof Error);
      }
    }),
    { numRuns: RUNS },
  );
});
