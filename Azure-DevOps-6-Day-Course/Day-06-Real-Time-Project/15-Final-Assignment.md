# 15 - Final Assignment

## Overview

This is your capstone assessment. Working **independently**, you'll set up a complete CI/CD solution for a new application of your choice, applying everything from Days 1–5. Treat it like a real task at a new job.

**Estimated time:** 2–4 hours (self-paced)

---

## The Task

Choose **one** of the [Sample-Applications](../../Sample-Applications/) (DotNet, Java, NodeJS, or Python) — **not** the one used in the Day 6 walkthrough if you used Node.js — and deliver a full Azure DevOps solution for it.

> Picking a different language forces you to adapt the pipeline tasks, which is the point.

---

## Requirements

Your solution must include all of the following. Check each off as you complete it.

### 1. Project & Repo
- [ ] A project (Git + a process of your choice).
- [ ] A repository containing the chosen sample app.
- [ ] A meaningful `README.md` describing the app.

### 2. Source Control & Quality
- [ ] `main` protected by **branch policies**: ≥1 reviewer, no self-approval, linked work items, comment resolution.
- [ ] At least **one feature delivered via a pull request** (linked to a work item) and merged with **squash**.
- [ ] A correct **`.gitignore`** for the language.

### 3. Planning (Boards)
- [ ] An **Epic → Feature → ≥2 User Stories** with acceptance criteria.
- [ ] At least one story broken into **Tasks**.
- [ ] One **Bug** with severity/priority.
- [ ] Stories planned into a **sprint**.

### 4. CI Build Pipeline
- [ ] A **YAML** pipeline that installs deps, **builds**, and **runs tests**.
- [ ] Publishes a **pipeline artifact**.
- [ ] Wired as **required build validation** on `main`.

### 5. Multi-Stage CD
- [ ] **Build → DeployDev → DeployProd** stages.
- [ ] **Build once, deploy many** (artifact reused).
- [ ] `dev` and `production` **environments** created.

### 6. Governance
- [ ] **Approval** on `production`.
- [ ] **Branch control** check (`main` only) on `production`.
- [ ] A **variable group** used by the pipeline (with at least one secret).

### 7. Observability
- [ ] A **dashboard** with build history, deployment status, and a work-item chart.
- [ ] **Notifications** configured for build failures.

### 8. Documentation
- [ ] A short write-up (in the repo Wiki or README) covering:
  - The branching strategy chosen and why.
  - How the pipeline works (stages and gates).
  - How to run/deploy locally.

---

## Stretch Goals (Optional)

- [ ] Use a **template** to factor out build steps.
- [ ] Add **code coverage** publishing and a coverage gate.
- [ ] Deploy to a **real Azure Web App** via a service connection (workload identity federation).
- [ ] Add a **canary or rolling** deployment strategy.
- [ ] Add a **business hours** or **exclusive lock** check on production.
- [ ] Link the pipeline to **Azure Boards** so completed PRs close stories automatically.

---

## Self-Assessment Rubric

| Area | Points |
| ---- | -----: |
| Project & repo set up correctly | 10 |
| Branch policies + PR workflow | 20 |
| Boards planning (hierarchy + sprint) | 15 |
| CI build pipeline + validation | 20 |
| Multi-stage CD + environments | 20 |
| Approvals + checks + variable group | 10 |
| Dashboard + notifications + docs | 5 |
| **Total** | **100** |

**Passing:** 70+. **Strong:** 85+. Add stretch goals for mastery.

---

## How to Demonstrate Completion

Capture evidence (screenshots in the `Images/` folder or notes in the Wiki):
1. The protected `main` with policies.
2. A merged PR linked to a work item.
3. A green multi-stage run paused for prod approval, then completed.
4. The environments' deployment history.
5. Your dashboard.

---

## Reflection

After finishing, write a short reflection:
- What was hardest, and how did you solve it?
- What would you do differently in a real production setup?
- Which DORA metric would you focus on improving first, and why?

---

## Congratulations!

If you've completed this assignment, you can set up a complete, governed CI/CD solution in Azure DevOps from scratch — a core DevOps engineering skill.

### Where to Go Next
- Pursue the **[AZ-400 certification](../../Resources/Useful-Links.md)**.
- Explore **Infrastructure as Code** (Bicep, Terraform) and **containers/Kubernetes**.
- Add **security scanning** (SonarCloud, dependency scanning) to your pipelines.
- Revisit the [Interview Questions](../../Resources/Interview-Questions.md) to prepare for roles.

Thank you for completing the **Azure DevOps 6-Day Course**. Happy shipping! 🚀

➡️ Back to the [Course Home](../README.md)
