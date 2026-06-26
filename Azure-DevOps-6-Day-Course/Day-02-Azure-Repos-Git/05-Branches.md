# 05 - Branches

## Overview

A **branch** is an independent line of development. It lets you work on a feature, fix, or experiment in isolation without affecting the main codebase. In Git, branches are cheap and fast because a branch is just a movable pointer to a commit.

## Why Branch?

- Develop features in parallel without stepping on each other.
- Keep `main` always stable and releasable.
- Isolate experiments and risky changes.
- Enable code review via pull requests before merging.

## The Default Branch

Most repos use `main` (older repos may use `master`) as the default/integration branch. In Azure Repos, the default branch is what new clones check out and what pull requests target by default.

## Working with Branches

```bash
git branch                      # list local branches (* = current)
git branch feature-login        # create a branch
git checkout feature-login      # switch to it
git checkout -b feature-login   # create AND switch (shortcut)

# Modern equivalents (Git 2.23+)
git switch feature-login        # switch
git switch -c feature-login     # create + switch
```

Push a new branch to Azure Repos:

```bash
git push -u origin feature-login
```

Delete branches:

```bash
git branch -d feature-login         # delete local (must be merged)
git branch -D feature-login         # force-delete local
git push origin --delete feature-login   # delete remote branch
```

## Visualizing Branches

```
        C1 ── C2 ── C3            (main)
                     \
                      C4 ── C5    (feature-login)  ◄── HEAD
```

After merging `feature-login` into `main`:

```
        C1 ── C2 ── C3 ─────── M  (main)
                     \        /
                      C4 ── C5
```

## Merging

Bring changes from one branch into another:

```bash
git checkout main
git merge feature-login
```

Two outcomes:
- **Fast-forward:** if `main` hasn't changed, the pointer just moves forward (no merge commit).
- **Three-way merge:** if both branches advanced, Git creates a **merge commit** combining them (may require conflict resolution — see lesson 09).

## Keeping a Branch Up to Date

While working on a long-lived feature branch, sync with `main` regularly to reduce conflicts:

```bash
git checkout feature-login
git merge main          # bring main's changes into your branch
# or, for a linear history:
git rebase main
```

## Branches in Azure Repos (Web UI)

- **Repos → Branches** lists all branches with ahead/behind indicators.
- You can create a branch from a work item (links them automatically).
- Set a branch as a **favorite** or change the **default** branch.
- Apply **branch policies** (next lessons) to protect important branches.

## Best Practices

- Use short-lived branches; merge frequently.
- Name branches clearly: `feature/login`, `bugfix/null-check`, `hotfix/payment`.
- Never commit directly to `main` in a team — use branches + pull requests.
- Delete branches after they're merged to keep the repo tidy.

## Summary

- A branch is a lightweight, movable pointer enabling isolated work.
- Create/switch with `git switch -c`, merge with `git merge`.
- Merges are fast-forward or three-way (the latter creates a merge commit).
- Keep feature branches short and synced with `main`.

## Knowledge Check

1. What command creates and switches to a new branch in one step?
2. What is the difference between a fast-forward and a three-way merge?
3. How do you delete a remote branch in Azure Repos from the CLI?

➡️ Next: [06 - Branching Strategy](./06-Branching-Strategy.md)
