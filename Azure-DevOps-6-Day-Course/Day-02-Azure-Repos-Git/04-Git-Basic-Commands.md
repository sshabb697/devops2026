# 04 - Git Basic Commands

## Overview

This lesson walks through the commands you'll use every day, in the order you'd typically use them. Follow along in a scratch folder to build muscle memory.

## Starting a Repository

```bash
git init                # turn the current folder into a Git repo
git clone <url>         # copy an existing remote repo locally
git clone <url> myapp   # clone into a folder named "myapp"
```

## Checking Status and Differences

```bash
git status              # what's modified, staged, untracked
git diff                # unstaged changes (working dir vs staged)
git diff --staged       # staged changes (staged vs last commit)
```

## Staging and Committing

```bash
git add file.txt        # stage a single file
git add .               # stage everything in the current dir
git add -p              # interactively stage parts of files

git commit -m "Add login form"      # commit staged changes
git commit -am "Fix typo"           # stage tracked files AND commit
```

**Writing good commit messages:**
- Use the imperative mood: "Add feature", not "Added feature".
- Keep the summary line under ~50 characters.
- Add a blank line and details if needed.

## Viewing History

```bash
git log                              # full history
git log --oneline                    # compact, one line per commit
git log --oneline --graph --all      # visual branch graph
git show <commit>                    # details of a specific commit
```

## Working with Remotes

```bash
git remote -v                        # list configured remotes
git remote add origin <url>          # connect to a remote
git push -u origin main              # first push (sets upstream)
git push                             # subsequent pushes
git fetch                            # download remote changes (no merge)
git pull                             # fetch + merge into current branch
```

## Undoing Things

```bash
git restore file.txt                 # discard working changes to a file
git restore --staged file.txt        # unstage a file (keep changes)
git commit --amend -m "New message"  # fix the last commit (before pushing!)
git reset --soft HEAD~1              # undo last commit, keep changes staged
git reset --mixed HEAD~1            # undo last commit, keep changes unstaged
git reset --hard HEAD~1             # undo last commit, DISCARD changes
git revert <commit>                  # safely undo a commit via a new commit
```

> ⚠️ `reset --hard` and `--amend` rewrite history. Avoid them on commits you've already pushed/shared.

## A Complete Example Workflow

```bash
# 1. Clone the Azure Repos repository
git clone https://dev.azure.com/myorg/Course-Project/_git/Course-Project
cd Course-Project

# 2. Create a file
echo "# My App" > README.md

# 3. Stage and commit
git add README.md
git commit -m "Add project README"

# 4. Push to Azure Repos
git push -u origin main

# 5. Make another change
echo "More details" >> README.md
git status
git diff
git commit -am "Expand README"
git push
```

## Quick Reference Table

| Task | Command |
| ---- | ------- |
| Initialize repo | `git init` |
| Clone repo | `git clone <url>` |
| Check status | `git status` |
| Stage changes | `git add .` |
| Commit | `git commit -m "msg"` |
| View history | `git log --oneline` |
| Push | `git push` |
| Pull | `git pull` |
| Discard file changes | `git restore <file>` |

## Summary

- The core loop is **edit → `add` → `commit` → `push`**.
- Use `status`, `diff`, and `log` constantly to understand state.
- Know the safe undo (`revert`, `restore`) vs the dangerous ones (`reset --hard`, `--amend`).

## Knowledge Check

1. What's the difference between `git fetch` and `git pull`?
2. How do you stage and commit in a single command?
3. Which undo command is safe to use on already-pushed commits?

➡️ Next: [05 - Branches](./05-Branches.md)
