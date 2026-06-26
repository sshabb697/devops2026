# 02 - Git Architecture

## Overview

To use Git effectively you need a mental model of how it stores and moves your work. Git has a small number of "areas" your files pass through, and a simple object model under the hood.

## The Three (Plus One) Areas

```
 Working Directory      Staging Area (Index)     Local Repository       Remote Repository
 ────────────────       ────────────────────     ────────────────       ─────────────────
   your files     ──►      git add        ──►       git commit    ──►       git push
   (edited)               (staged)                 (committed)            (shared)
                                            ◄── git checkout/restore
                                            ◄────────── git pull / fetch ──────────
```

### 1. Working Directory
The actual files on disk that you edit. Files here are **modified** but not yet tracked for the next commit.

### 2. Staging Area (Index)
A "draft" of your next commit. You add specific changes with `git add`. This lets you commit *some* changes while leaving others for later — crafting clean, logical commits.

### 3. Local Repository
The `.git` folder inside your project. `git commit` permanently records the staged snapshot here, complete with author, message, and a unique ID. Because the full history lives locally, you can work entirely offline.

### 4. Remote Repository
A shared copy (e.g., in **Azure Repos**, GitHub). You synchronize with `git push` (send) and `git fetch`/`git pull` (receive).

## File States

A tracked file moves through these states:

```
Untracked → (git add) → Staged → (git commit) → Committed → (edit) → Modified → (git add) → Staged → ...
```

| State | Meaning |
| ----- | ------- |
| **Untracked** | Git doesn't know about this file yet |
| **Modified** | Changed but not staged |
| **Staged** | Marked to go into the next commit |
| **Committed** | Safely stored in the local repo |

## Git's Object Model

Git stores everything as objects identified by a SHA-1 hash:

| Object | Represents |
| ------ | ---------- |
| **Blob** | The contents of a file |
| **Tree** | A directory (maps names → blobs/trees) |
| **Commit** | A snapshot: points to a tree + parent commit(s) + author + message |
| **Tag** | A named pointer to a commit (often a release) |

A **commit** is a full snapshot (not a diff), but Git stores them efficiently. Each commit points to its parent, forming the history graph.

## HEAD, Branches, and Refs

- A **branch** is just a lightweight, movable pointer to a commit.
- **HEAD** is a pointer to the branch (or commit) you currently have checked out.
- Creating a branch is cheap — it's a new pointer, not a copy of files.

```
        C1 ── C2 ── C3   (main)  ◄── HEAD
                     \
                      C4 ── C5   (feature)
```

## Why This Matters

- Understanding the **staging area** lets you make clean, intentional commits.
- Knowing commits are **snapshots with parents** explains how branching and merging work.
- Recognizing **local vs remote** explains why you must `push`/`pull` to share.

## Summary

- Files flow through **Working Directory → Staging Area → Local Repo → Remote Repo**.
- File states: untracked, modified, staged, committed.
- Git stores **blobs, trees, commits, tags**; branches are movable pointers; HEAD marks your current location.

## Knowledge Check

1. What command moves changes from the working directory to the staging area?
2. What is the difference between the local and remote repository?
3. What is a branch, technically?

➡️ Next: [03 - Git Installation](./03-Git-Installation.md)
