# 01 - Version Control

## Overview

**Version control** (a.k.a. source control) is a system that records changes to files over time so you can recall specific versions later, collaborate with others, and understand the history of a project.

If you've ever saved files like `report_final.docx`, `report_final_v2.docx`, `report_final_REALLY.docx` — that's manual version control, and it doesn't scale. Version control systems (VCS) solve this properly.

## Why Use Version Control?

- **History** — see who changed what, when, and why.
- **Collaboration** — many people work on the same codebase without overwriting each other.
- **Branching** — work on features in isolation, then merge.
- **Backup & recovery** — restore previous versions; nothing is truly lost.
- **Accountability** — every change is attributed to an author.
- **Experimentation** — try ideas on a branch without risking `main`.

## Types of Version Control Systems

### 1. Local VCS
Versions stored only on your own machine (e.g., RCS). No collaboration; risky if the machine fails.

### 2. Centralized VCS (CVCS)
A single central server holds all versioned files; clients check out files from it.

- Examples: **TFVC**, **Subversion (SVN)**, **Perforce**.
- **Pros:** simple, central control, fine-grained access.
- **Cons:** single point of failure; limited offline work; the server must be available to commit.

```
        ┌─────────────┐
        │   Server    │  (full history)
        └──────┬──────┘
        ┌──────┴──────┐
   ┌────▼───┐    ┌────▼───┐
   │Client A│    │Client B│  (working copy only)
   └────────┘    └────────┘
```

### 3. Distributed VCS (DVCS)
Every clone is a **full copy** of the repository, including its entire history.

- Examples: **Git**, **Mercurial**.
- **Pros:** work offline, fast, no single point of failure, powerful branching/merging.
- **Cons:** slightly steeper learning curve.

```
   ┌──────────────┐        ┌──────────────┐
   │  Client A    │◄──────►│   Remote     │
   │ (full repo)  │        │ (full repo)  │
   └──────────────┘        └──────┬───────┘
                                  │
                           ┌──────▼───────┐
                           │  Client B    │
                           │ (full repo)  │
                           └──────────────┘
```

## Centralized vs Distributed

| Aspect | Centralized (CVCS) | Distributed (DVCS) |
| ------ | ------------------ | ------------------ |
| History location | Central server only | Every clone |
| Offline work | Limited | Full |
| Speed | Network-dependent | Mostly local, fast |
| Single point of failure | Yes | No |
| Branching/merging | Heavier | Lightweight |
| Examples | TFVC, SVN | Git, Mercurial |

## Version Control in Azure Repos

Azure Repos supports **two** types:

- **Git** (distributed) — the modern default; what this course uses.
- **TFVC** (Team Foundation Version Control, centralized) — legacy; for teams migrating from older TFS setups.

Unless you have a specific reason, **choose Git**.

## Summary

- Version control tracks changes, enables collaboration, and preserves history.
- Three families: local, centralized (CVCS), distributed (DVCS).
- **Git** is a distributed VCS and the modern standard; Azure Repos supports Git and TFVC.

## Knowledge Check

1. Name three benefits of version control.
2. What is the key difference between centralized and distributed VCS?
3. Which two version control types does Azure Repos support?

➡️ Next: [02 - Git Architecture](./02-Git-Architecture.md)
