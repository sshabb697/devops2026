# 06 - Branching Strategy

## Overview

A **branching strategy** is an agreed-upon convention for how a team creates, names, and merges branches. A good strategy keeps the codebase stable, makes releases predictable, and reduces merge pain. This lesson compares the most common strategies.

## 1. GitHub Flow (Simple)

A lightweight model centered on `main`:

1. `main` is always deployable.
2. Create a short-lived **feature branch** off `main`.
3. Open a **pull request** for review.
4. Merge back into `main` and deploy.

```
main ──●──────────●──────────●──►
        \        /
         feature (PR)
```

**Best for:** continuous delivery, web apps, small/medium teams. Simple and fast.

## 2. GitFlow (Structured)

A heavier model with multiple long-lived branches:

| Branch | Purpose |
| ------ | ------- |
| `main` | Production-ready, tagged releases |
| `develop` | Integration branch for next release |
| `feature/*` | New features (branch off `develop`) |
| `release/*` | Stabilize a release (branch off `develop`) |
| `hotfix/*` | Urgent production fixes (branch off `main`) |

```
main    ──●─────────────────●───────●──►  (tags: v1.0, v1.1)
           \               /       /
release     \         ●───●       /
             \       /     \     /
develop  ●────●──●──●───────●───●──►
              \  /
feature        ●
```

**Best for:** scheduled releases, multiple versions in production, larger teams. More overhead.

## 3. Trunk-Based Development

Everyone integrates into a single branch (`main`/trunk) with very short-lived branches (often less than a day), behind **feature flags** if needed.

```
main ──●─●─●─●─●─●─●──►   (tiny branches merged constantly)
```

**Best for:** high-performing teams practicing CI/CD with strong test automation. Minimizes merge conflicts.

## 4. Release Branching

Cut a `release/x.y` branch when preparing a release; bug fixes go there and are merged back. Common in product teams maintaining multiple supported versions.

## Comparison

| Strategy | Complexity | Long-lived branches | Best for |
| -------- | ---------- | ------------------- | -------- |
| GitHub Flow | Low | `main` only | Continuous delivery |
| Trunk-Based | Low | `main` only | Mature CI/CD teams |
| GitFlow | High | `main`, `develop` | Scheduled releases |
| Release Branching | Medium | `main` + releases | Multiple supported versions |

## Branch Naming Conventions

Pick a convention and enforce it:

```
feature/<work-item-id>-<short-description>   e.g., feature/1234-user-login
bugfix/<work-item-id>-<short-description>    e.g., bugfix/1290-null-pointer
hotfix/<short-description>                   e.g., hotfix/payment-timeout
release/<version>                            e.g., release/2.1.0
```

Including the work item ID lets Azure Repos auto-link branches and PRs to Azure Boards.

## Choosing a Strategy

- **Small team shipping continuously?** → GitHub Flow or Trunk-Based.
- **Strong automated tests and want speed?** → Trunk-Based.
- **Need formal releases / multiple versions?** → GitFlow or Release Branching.

> Whatever you choose, protect your integration branch with **branch policies** (lesson 08) and keep branches short-lived.

## Summary

- A branching strategy is a team convention for branching and merging.
- Common strategies: **GitHub Flow**, **GitFlow**, **Trunk-Based**, **Release Branching**.
- Choose based on release cadence, team size, and test maturity.
- Use consistent branch naming, ideally linking to work item IDs.

## Knowledge Check

1. Which strategy keeps only `main` as a long-lived branch and is simplest?
2. In GitFlow, where do hotfix branches branch from?
3. Why include a work item ID in branch names?

➡️ Next: [07 - Pull Requests](./07-Pull-Requests.md)
