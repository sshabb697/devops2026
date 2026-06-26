# 07 - Pull Requests

## Overview

A **pull request (PR)** is a request to merge changes from one branch into another. It is the heart of collaborative development in Azure Repos: it enables **code review**, **discussion**, **automated checks**, and **policy enforcement** before code reaches an important branch like `main`.

## Why Pull Requests?

- **Quality** — peers review changes before they merge.
- **Knowledge sharing** — the team sees what's changing and why.
- **Safety** — policies and builds can gate the merge.
- **Traceability** — PRs link commits, work items, and discussions.

## The Pull Request Lifecycle

```
1. Create branch  →  2. Commit & push  →  3. Open PR  →  4. Review & discuss
                                                              │
       6. Merge & (optionally) delete branch  ◄── 5. Approve + checks pass
```

## Creating a Pull Request in Azure Repos

1. Push your feature branch:
   ```bash
   git push -u origin feature/1234-user-login
   ```
2. In the portal, Azure Repos shows a **"Create a pull request"** prompt — or go to **Repos → Pull requests → New pull request**.
3. Set:
   - **Source branch** (your feature branch) and **target branch** (usually `main`).
   - **Title** and **description** (explain *what* and *why*).
   - **Reviewers** (required and optional).
   - **Work items** to link (e.g., `#1234`).
4. Click **Create**.

## Reviewing a Pull Request

Reviewers can:
- Read the **Files** tab to see the diff.
- Leave **comments** on specific lines.
- Mark comments as **resolved**.
- Vote:

| Vote | Meaning |
| ---- | ------- |
| ✅ **Approve** | Good to merge |
| ✅ **Approve with suggestions** | Minor, non-blocking notes |
| ⏳ **Wait for author** | Author should address feedback |
| ❌ **Reject** | Significant problems; do not merge |

## Completing (Merging) a Pull Request

When approvals and policies are satisfied, click **Complete**. Choose a merge type:

| Merge type | Result |
| ---------- | ------ |
| **Merge (no fast-forward)** | Keeps all commits + adds a merge commit |
| **Squash** | Combines all PR commits into one clean commit |
| **Rebase and fast-forward** | Replays commits onto target for a linear history |
| **Semi-linear merge** | Rebase then add a merge commit |

Common options on completion:
- **Delete source branch** after merge (recommended).
- **Complete linked work items** (e.g., move to Done).
- **Squash** for a tidy history.

## Draft Pull Requests

Mark a PR as **Draft** to share work-in-progress without triggering required reviewers or signalling it's ready to merge. Publish it when ready.

## Useful Features

- **@mentions** to notify teammates.
- **Auto-complete:** set a PR to merge automatically once all policies pass.
- **Attach work items** for traceability.
- **Comment policies:** require all comments resolved before completion (a branch policy).

## Best Practices

- Keep PRs **small and focused** — easier and faster to review.
- Write a clear **description** and link work items.
- Respond to all comments; resolve or discuss them.
- Don't merge your own PR without review (enforce via policy).
- Use **squash** to keep `main` history clean.

## Summary

- A pull request proposes merging one branch into another with review and checks.
- Reviewers comment and vote (Approve / Wait / Reject).
- Complete with a chosen merge type (merge, squash, rebase).
- Keep PRs small, well-described, and linked to work items.

## Knowledge Check

1. What is the main purpose of a pull request?
2. What does the **squash** merge option do?
3. When would you use a **draft** pull request?

➡️ Next: [08 - Branch Policies](./08-Branch-Policies.md)
