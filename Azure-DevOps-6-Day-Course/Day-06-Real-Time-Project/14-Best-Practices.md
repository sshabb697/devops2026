# 14 - Best Practices

## Overview

A consolidated set of best practices spanning the whole course. Use this as a checklist when setting up Azure DevOps for any real project.

## Organization & Project

- Prefer **one organization** per company; **fewer, larger projects** with teams over many small ones.
- Connect to **Microsoft Entra ID** for centralized identity, MFA, and conditional access.
- Tighten **org security policies** (limit PATs, OAuth/SSH, third-party app access).
- Keep **Project Collection / Project Administrators** to a minimal, trusted set.

## Source Control (Repos)

- Use **Git** with a clear, simple **branching strategy** (GitHub Flow or trunk-based for most teams).
- **Protect `main`** with branch policies: required reviewers, linked work items, build validation, comment resolution.
- **Deny force push** on protected branches.
- Keep branches **short-lived** and PRs **small**.
- Keep secrets **out of the repo**; use a thorough `.gitignore`.
- Use **squash merges** for a clean history (team preference).

## Boards & Planning

- Choose the right **process** (Agile/Scrum/Basic/CMMI) and customize via **inherited processes**.
- Maintain a **refined, prioritized backlog**; keep the top "ready."
- Write user stories with **acceptance criteria** (INVEST).
- Link work items to **branches/PRs/builds** for traceability.
- Use **dashboards** to make progress visible.

## Pipelines (CI/CD)

- Author pipelines in **YAML** (versioned, reviewed, reusable).
- **Build once, deploy many** — share a single artifact across environments.
- Keep pipelines **fast** (caching, parallel jobs, only build what changed).
- Use **templates** to standardize and reduce duplication.
- Publish **test results and coverage**; gate merges on them.
- Use **multi-stage** pipelines for CI + CD in one place.

## Security

- Store secrets in **variable groups (Key Vault)** and **secure files** — never in YAML.
- Don't expose secrets to **forked/PR** builds.
- Use **service connections** with **workload identity federation**; scope them narrowly.
- Gate sensitive **environments** with **approvals** and **checks** (branch control, business hours).
- Apply **least privilege** everywhere; assign permissions to **groups**.
- Be cautious running untrusted code on **self-hosted agents**.

## Deployments

- Use **environments** for history, security, and checks.
- Choose a **deployment strategy** (runOnce/rolling/canary) appropriate to risk.
- Add **smoke tests** post-deploy and **rollback** on failure.
- Require **approval** + **branch control** for production.
- Separate **service connections** per environment (`azure-dev`, `azure-prod`).

## Observability & Operations

- Configure **notifications** for failures and pending approvals (Teams/Slack).
- Track **DORA metrics** (deployment frequency, lead time, change failure rate, MTTR).
- Enable **audit logs** and **stream** them to a SIEM/Log Analytics.
- Maintain **dashboards** for delivery health.

## Culture (back to Day 1)

- Foster **shared ownership** between dev and ops.
- Automate relentlessly; eliminate manual, error-prone steps.
- Make work and metrics **visible**.
- Run **blameless retrospectives**; learn from failures.
- Ship **small and often**.

## The Golden Rules (TL;DR)

1. Protect `main`; merge via reviewed PRs that pass CI.
2. Automate build/test/deploy in versioned YAML.
3. Build once, deploy many through gated environments.
4. Keep secrets out of code; use Key Vault/secure files.
5. Least privilege, audit everything.
6. Make it visible; measure and improve.

## Summary

This checklist distills the course into actionable practices across org/project setup, source control, planning, CI/CD, security, deployments, observability, and culture. Apply them to any real Azure DevOps project.

➡️ Next: [15 - Final Assignment](./15-Final-Assignment.md)
