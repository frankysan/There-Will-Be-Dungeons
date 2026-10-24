#!/usr/bin/env node
// Lint maintained Markdown without third-party glob parsers. Node.js >=22.
import { readdir, readFile, realpath, stat, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { lint } from "markdownlint/promise";
import { applyFixes } from "markdownlint";

const root = fileURLToPath(new URL("../", import.meta.url));
process.chdir(root);

const directories = ["delvers", "episodes", "narrative", "world", "project", "reports"];
const args = process.argv.slice(2);
const fix = args.includes("--fix");
const filesFlag = args.indexOf("--files");
const selected = filesFlag >= 0 ? args.slice(filesFlag + 1) : null;
const unexpected = filesFlag >= 0
  ? args.slice(0, filesFlag).filter((arg) => arg !== "--fix")
  : args.filter((arg) => arg !== "--fix");
if (unexpected.length || (selected && (!selected.length || selected.some((arg) => arg.startsWith("--")))) ||
    (selected && fix)) {
  console.error("Usage: lint-markdown.mjs [--fix] OR lint-markdown.mjs --files <path.md> [...]");
  process.exit(2);
}

async function selectedMarkdown(paths) {
  const resolvedRoot = await realpath(root);
  const valid = [];
  for (const input of paths) {
    const absolute = path.resolve(root, input);
    const relative = path.relative(root, absolute);
    const inside = relative && relative !== ".." &&
      !relative.startsWith(".." + path.sep) && !path.isAbsolute(relative);
    const maintained = relative === "README.md" ||
      (relative.endsWith(".md") &&
       directories.some((directory) => relative.startsWith(directory + path.sep)));
    if (!inside || !maintained) {
      throw new Error("Not a maintained Markdown path: " + input);
    }
    const physical = await realpath(absolute);
    const relativePhysical = path.relative(resolvedRoot, physical);
    if (relativePhysical === ".." || relativePhysical.startsWith(".." + path.sep) ||
        path.isAbsolute(relativePhysical) || !(await stat(absolute)).isFile()) {
      throw new Error("Path is not a regular file inside the repository: " + input);
    }
    valid.push(relative);
  }
  return [...new Set(valid)].sort();
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

const files = selected
  ? await selectedMarkdown(selected)
  : [
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
