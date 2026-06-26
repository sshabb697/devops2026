# 09 - Merge Conflicts

## Overview

A **merge conflict** happens when Git can't automatically reconcile changes from two branches because the *same lines* of a file were changed differently (or one side edited a file the other deleted). Git pauses and asks **you** to decide what the result should be.

Conflicts are normal — not errors. Knowing how to resolve them calmly is an essential skill.

## When Do Conflicts Occur?

- Two branches edited the **same lines** of the same file.
- One branch **deleted** a file the other **modified**.
- Two branches **renamed** the same file differently.

They surface during `git merge`, `git rebase`, `git pull`, or when completing a pull request.

## What a Conflict Looks Like

When a conflict occurs, Git inserts **conflict markers** into the file:

```text
<<<<<<< HEAD
const greeting = "Hello, world!";
=======
const greeting = "Hi there!";
>>>>>>> feature-greeting
```

- `<<<<<<< HEAD` — the start of *your current branch's* version.
- `=======` — the divider.
- `>>>>>>> feature-greeting` — the end of the *incoming branch's* version.

## Resolving a Conflict (Step by Step)

```bash
git checkout main
git merge feature-greeting
# CONFLICT (content): Merge conflict in app.js
```

1. **See which files conflict:**
   ```bash
   git status
   ```
2. **Open each conflicted file** and decide the correct result. Edit to keep what you want and **remove all conflict markers** (`<<<<<<<`, `=======`, `>>>>>>>`):
   ```js
   const greeting = "Hello there!";   // resolved
   ```
3. **Stage the resolved files:**
   ```bash
   git add app.js
   ```
4. **Complete the merge:**
   ```bash
   git commit          # for merge
   # or, if rebasing:
   git rebase --continue
   ```

## Aborting

If things go sideways, you can back out:

```bash
git merge --abort     # cancel a merge
git rebase --abort    # cancel a rebase
```

## Tools That Help

- **`git mergetool`** — launches a configured visual merge tool.
- **VS Code** — shows "Accept Current / Accept Incoming / Accept Both" buttons inline.
- **Azure Repos web editor** — resolve simple conflicts directly in the browser during a PR.

## Resolving Conflicts in a Pull Request

If a PR shows conflicts with the target branch:
1. Azure Repos flags the conflict.
2. For simple cases, use the **web conflict editor** to resolve.
3. For complex cases, resolve locally:
   ```bash
   git checkout feature-branch
   git fetch origin
   git merge origin/main      # resolve conflicts here
   git push
   ```
   The PR updates automatically once you push the resolution.

## How to Avoid (Minimize) Conflicts

- **Pull/merge `main` often** into your feature branch.
- Keep branches **short-lived** and changes **small**.
- Coordinate so two people don't rewrite the same files.
- Use consistent formatting (a formatter/linter) to avoid noise conflicts.

## Summary

- Conflicts occur when Git can't auto-merge overlapping changes.
- Git marks conflicts with `<<<<<<<`, `=======`, `>>>>>>>`.
- Resolve by editing the file, removing markers, then `git add` + commit.
- Avoid conflicts by merging `main` frequently and keeping branches small.

## Knowledge Check

1. What do the markers `<<<<<<<`, `=======`, and `>>>>>>>` indicate?
2. What command cancels an in-progress merge?
3. Name two practices that reduce how often conflicts happen.

➡️ Next: [10 - Tags](./10-Tags.md)
