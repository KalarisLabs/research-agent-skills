#!/usr/bin/env node
import { main } from "./cli.js";

main().then(
  (code) => process.exit(code),
  (err: Error) => {
    process.stderr.write(`error: ${err.message}\n`);
    process.exit(1);
  },
);
