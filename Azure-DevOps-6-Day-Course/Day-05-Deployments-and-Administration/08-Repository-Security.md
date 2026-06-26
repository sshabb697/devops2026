# 08 - Repository Security

## Overview

**Repository security** protects your source code: who can read it, contribute to it, manage it, and rewrite history. This builds on Day 2 (Repository Permissions) and adds the broader security practices for keeping a codebase safe in Azure Repos.

## Layers of Repo Protection

```
Permissions (who can do what)
  + Branch policies (quality gates on PRs)
  + Branch security (per-branch restrictions)
  + Secret hygiene (.gitignore, push protection)
  + Code review (PRs)
= a secure repository
```

## Permissions (Recap)

Set at **Project settings → Repositories → (repo) → Security**. Key permissions:

| Permission | Controls |
| ---------- | -------- |
| **Read** | Clone/view |
| **Contribute** | Push, create branches |
| **Contribute to pull requests** | Comment/vote on PRs |
| **Force push (rewrite history)** | Force-push / delete refs |
| **Manage permissions** | Change security |
| **Bypass policies when pushing / completing PRs** | Override protections |

Assign to **groups**, follow **least privilege**, and remember **Deny wins**.

## Branch Policies (Recap)

Protect important branches with policies (Day 2, lesson 08): required reviewers, linked work items, comment resolution, and **build validation**. Direct pushes to a policy-protected branch are blocked — changes flow through PRs.

## Branch-Level Security

Beyond policies, set **branch security** (Repos → Branches → ⋯ → Branch security) to:
- **Deny Force push** on `main`/release branches (prevents history rewrites).
- Restrict who can **manage** a branch.
- **Lock** a branch to make it temporarily read-only.

## Protecting Secrets in Code

- Add a thorough **`.gitignore`** (Day 2, lesson 11) so secrets/config never get committed.
- Never commit credentials; use **variable groups / Key Vault / secure files** instead.
- If a secret is committed, **rotate it immediately** — removing it from history is not enough once it's pushed.
- Consider **secret scanning** tools/extensions to catch leaks in PRs.

## Cross-Project / Fork Considerations

- For public projects, **forks** can submit PRs — be careful running pipelines on untrusted PRs (don't expose secrets to fork builds).
- Restrict who can create repos and who can change repo settings.

## Auditing Access

- Review **repo permissions** periodically.
- Use **audit logs** (lesson 14) to see security and access changes.
- Remove access for people who leave the team (ideally via **Entra ID** group sync).

## Best Practices Checklist

- [ ] Assign permissions to **groups**, least privilege.
- [ ] Protect `main` with **branch policies** + **build validation**.
- [ ] **Deny force push** on protected branches.
- [ ] Keep secrets out of the repo (`.gitignore`, Key Vault).
- [ ] Limit **bypass** permissions to very few admins.
- [ ] Don't expose secrets to **fork/PR** builds in public projects.
- [ ] Review access and audit logs regularly.

## Summary

- Repo security combines **permissions**, **branch policies**, **branch security**, and **secret hygiene**.
- Deny force push on protected branches; require PRs with policies.
- Keep secrets out of source control and rotate any that leak.
- Limit bypass rights and audit access regularly.

## Knowledge Check

1. What's the difference between a branch policy and branch security?
2. Why isn't deleting a committed secret from a file enough?
3. What's a key risk with pipelines triggered by forked PRs?

➡️ Next: [09 - Pipeline Security](./09-Pipeline-Security.md)
