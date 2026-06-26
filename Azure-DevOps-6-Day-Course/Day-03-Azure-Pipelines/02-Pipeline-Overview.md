# 02 - Pipeline Overview

## Overview

**Azure Pipelines** is the CI/CD service in Azure DevOps. It automatically builds, tests, and deploys your code to any target — any language, any platform, any cloud. This lesson gives you the big picture before we dive into specifics.

## What Azure Pipelines Can Do

- Build apps in **.NET, Java, Node.js, Python, Go, C++, mobile**, containers, and more.
- Run on **Linux, Windows, and macOS** agents.
- Deploy to **Azure, AWS, GCP, Kubernetes, VMs, on-prem**, app stores.
- Integrate with **Azure Repos, GitHub, Bitbucket**, and other Git providers.
- Run tests, publish results and code coverage, and gate releases.

## Key Concepts and Terms

| Term | Meaning |
| ---- | ------- |
| **Pipeline** | The whole automated process (definition of build/deploy) |
| **Run** | A single execution of a pipeline |
| **Stage** | A major division of the pipeline (e.g., Build, Deploy) |
| **Job** | A set of steps that run on one agent |
| **Step** | A single action: a **task** or a **script** |
| **Task** | A pre-packaged action (e.g., `DotNetCoreCLI@2`) |
| **Agent** | The machine that runs a job |
| **Artifact** | Output of a build, shared with later stages |
| **Trigger** | What causes a pipeline to run |
| **Environment** | A deployment target with checks/approvals |

## Two Authoring Experiences

| | Classic | YAML |
| --- | ------- | ---- |
| Defined where | GUI (web designer) | `azure-pipelines.yml` in the repo |
| Versioned with code | No | Yes |
| Reviewable in PRs | No | Yes |
| Microsoft's recommendation | Legacy | **Preferred** |

We cover both, but focus on **YAML** (lesson 04 onward).

## How a Pipeline Runs (High Level)

```
Trigger fires (push/PR/schedule)
   → Azure Pipelines queues a run
   → An agent is allocated from an agent pool
   → The agent checks out your code
   → It executes each stage → job → step
   → Artifacts are published; results/logs are recorded
   → (CD) Deployment stages run, with approvals/checks
```

## Where to Find Pipelines

In your project: **Pipelines** in the left nav, which contains:
- **Pipelines** — your build/CI definitions and run history.
- **Environments** — deployment targets with checks/approvals.
- **Releases** — Classic release pipelines (CD).
- **Library** — variable groups and secure files.
- **Task groups / Deployment groups** (Classic).

## Free Tier (at a glance)

- **Microsoft-hosted:** free parallel job(s) with monthly minutes (more generous for public projects).
- **Self-hosted:** one free parallel job; you provide the machines.

(Limits change over time — see [Useful Links](../Resources/Useful-Links.md).)

## Summary

- Azure Pipelines is a language/platform/cloud-agnostic CI/CD service.
- Core hierarchy: **Pipeline → Stages → Jobs → Steps**, run by **agents**.
- Two authoring styles: Classic (GUI) and YAML (as-code, preferred).

## Knowledge Check

1. What runs a pipeline job — and where does it come from?
2. List the four levels of the pipeline hierarchy.
3. Why is YAML preferred over Classic?

➡️ Next: [03 - Classic Pipelines](./03-Classic-Pipelines.md)
