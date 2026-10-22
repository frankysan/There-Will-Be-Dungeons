#!/usr/bin/env node
// Lint maintained Markdown without third-party glob parsers. Node.js >=22.
import { readdir, readFile, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { lint } from "markdownlint/promise";
import { applyFixes } from "markdownlint";

const root = fileURLToPath(new URL("../", import.meta.url));
process.chdir(root);

const directories = ["episodes", "narrative", "world", "project", "reports"];
const fix = process.argv.slice(2).includes("--fix");
const unexpected = process.argv.slice(2).filter((arg) => arg !== "--fix");
if (unexpected.length) {
  console.error("Unknown arguments: " + unexpected.join(", "));
  process.exit(2);
}

async function collectMarkdown(dir) {
  const entries = await readdir(dir, { withFileTypes: true });
  const paths = [];
  for (const entry of entries) {
    const file = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      paths.push(...await collectMarkdown(file));
    } else if (entry.isFile() && entry.name.endsWith(".md")) {
      paths.push(file);
    }
    // Intentionally skip symlinks and other non-file entries.
  }
  return paths;
}

const files = [
  "README.md",
  ...(await Promise.all(directories.map(collectMarkdown))).flat()
].sort();
const config = JSON.parse(await readFile(".markdownlint.json", "utf8"));

if (fix) {
  let changed = 0;
  for (const file of files) {
    const original = await readFile(file, "utf8");
    const results = await lint({ strings: { [file]: original }, config });
    const revised = applyFixes(original, results[file] ?? []);
    if (revised !== original) {
      await writeFile(file, revised, "utf8");
      changed += 1;
    }
  }
  console.log("Automatically updated " + changed + " file(s); verify the diff.");
}

const results = await lint({ files, config });
let violations = 0;
for (const file of files) {
  for (const issue of results[file] ?? []) {
    violations += 1;
    const rule = issue.ruleNames[0];
    const details = issue.errorDetail ? " (" + issue.errorDetail + ")" : "";
    console.error(file.replaceAll("\\", "/") + ":" + issue.lineNumber + " " +
      rule + " " + issue.ruleDescription + details);
  }
}
console.log("Checked " + files.length + " maintained Markdown files; " +
  violations + " violation(s).");
if (violations) process.exitCode = 1;
