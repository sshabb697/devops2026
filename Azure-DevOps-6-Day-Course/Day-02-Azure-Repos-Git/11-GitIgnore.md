# 11 - .gitignore

## Overview

A **`.gitignore`** file tells Git which files and folders to **ignore** — never track or commit. This keeps your repository clean of build outputs, dependencies, secrets, and machine-specific files.

## Why Ignore Files?

- **Build artifacts** (`bin/`, `obj/`, `dist/`, `target/`) are regenerated — no need to version them.
- **Dependencies** (`node_modules/`, `.venv/`) are huge and restorable from package managers.
- **Secrets** (`.env`, credentials) must never be committed.
- **OS/editor files** (`.DS_Store`, `.vscode/`, `*.swp`) are personal noise.

## How It Works

- Place a `.gitignore` file in your repo (usually at the root).
- Each line is a **pattern**; matching files are excluded from `git status` and `git add`.
- `.gitignore` itself **is** committed so the whole team shares the rules.

## Pattern Syntax

| Pattern | Matches |
| ------- | ------- |
| `*.log` | All files ending in `.log` |
| `build/` | A directory named `build` (anywhere) |
| `/secret.txt` | `secret.txt` only in the repo root |
| `temp/*.tmp` | `.tmp` files inside `temp/` |
| `**/logs` | `logs` directories at any depth |
| `!keep.log` | **Negation** — do NOT ignore `keep.log` |
| `# comment` | A comment line |

## Example `.gitignore` Files

### Node.js
```gitignore
node_modules/
npm-debug.log*
dist/
.env
coverage/
```

### Python
```gitignore
__pycache__/
*.pyc
.venv/
env/
*.egg-info/
.pytest_cache/
```

### .NET
```gitignore
bin/
obj/
*.user
.vs/
[Dd]ebug/
[Rr]elease/
```

### Java (Maven/Gradle)
```gitignore
target/
build/
*.class
.gradle/
.idea/
```

### General / OS / Editor
```gitignore
.DS_Store
Thumbs.db
.vscode/
*.swp
.env
*.local
```

## Getting Ready-Made Templates

- GitHub maintains a comprehensive collection: [github.com/github/gitignore](https://github.com/github/gitignore).
- Many tools (`dotnet new gitignore`, IDE templates) can generate one for you.

## Already-Tracked Files

`.gitignore` only affects **untracked** files. If a file is already committed, adding it to `.gitignore` won't remove it. Untrack it first:

```bash
git rm --cached secret.txt        # stop tracking, keep the local file
git commit -m "Stop tracking secret.txt"
```

For a whole folder:
```bash
git rm -r --cached node_modules/
```

## Tips

- Add `.gitignore` **before** your first commit to avoid tracking junk.
- Never commit secrets — use ignored `.env` files plus a committed `.env.example` template.
- Use `git status --ignored` to see what's being ignored.
- A global ignore for personal files: `git config --global core.excludesfile ~/.gitignore_global`.

## Summary

- `.gitignore` excludes files/folders from Git tracking.
- Ignore build outputs, dependencies, secrets, and OS/editor files.
- It only affects untracked files — use `git rm --cached` for already-tracked ones.
- Use language-specific templates and never commit secrets.

## Knowledge Check

1. Why should `node_modules/` be in `.gitignore`?
2. Does adding an already-committed file to `.gitignore` remove it from the repo?
3. What does a leading `!` do in a `.gitignore` pattern?

➡️ Next: [12 - Repository Permissions](./12-Repository-Permissions.md)
