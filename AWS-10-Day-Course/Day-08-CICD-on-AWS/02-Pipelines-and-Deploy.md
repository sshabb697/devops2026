# 02 — Pipelines and deployments

**Learning objectives**

- Understand a **CodePipeline** as linked stages
- Know what **CodeDeploy** and `appspec.yml` do

---

## One-sentence idea

A pipeline watches your repo and, on every change, runs **Source → Build → Deploy** with no human in the loop.

---

## Pipeline stages

```text
┌─ Source ─┐   ┌─ Build ──┐   ┌─ Deploy ──┐
│ GitHub   │─▶ │ CodeBuild│─▶ │ CodeDeploy│─▶ EC2 / S3 / ECS
└──────────┘   └──────────┘   └───────────┘
```

- **Source:** triggers on each commit; grabs the code.
- **Build:** CodeBuild runs `buildspec.yml`, produces artifacts.
- **Deploy:** CodeDeploy (or S3/ECS) pushes the artifacts to the target.

Each stage passes **artifacts** to the next. If any stage fails, the pipeline stops — bad code doesn't reach production.

---

## CodeDeploy and appspec.yml

CodeDeploy needs an `appspec.yml` that answers:

- **Where do files go?** (`files:` → destination paths)
- **What scripts run, and when?** (`hooks:` → lifecycle events)

```yaml
version: 0.0
os: linux
files:
  - source: index.html
    destination: /var/www/html/
hooks:
  AfterInstall:
    - location: scripts/restart_server.sh
```

Lifecycle hooks (`BeforeInstall`, `AfterInstall`, `ApplicationStart`, …) let you stop/start services around the copy.

---

## Deployment strategies

| Strategy | How | Benefit |
| -------- | --- | ------- |
| **In-place** | Update the same servers | Simple |
| **Blue/Green** | Launch new set, switch traffic, keep old as fallback | **Zero-downtime**, easy rollback |

Blue/Green is the gold standard: if the new version is broken, flip traffic back instantly.

---

## Knowledge check

1. What happens to the pipeline if the Build stage fails?
2. What two questions does `appspec.yml` answer?

<details>
<summary>Answers</summary>

1. It stops — the Deploy stage never runs, so broken code isn't released.
2. Where files should be copied, and which scripts (hooks) run at each lifecycle event.

</details>

➡️ Next: [Lab 08B](./Lab-08B-CodePipeline.md)
