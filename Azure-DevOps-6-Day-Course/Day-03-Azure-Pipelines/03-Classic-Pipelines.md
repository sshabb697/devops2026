# 03 - Classic Pipelines

## Overview

**Classic pipelines** are configured through a graphical web designer rather than a YAML file. They were the original way to build pipelines in Azure DevOps. While YAML is now preferred, you'll still encounter Classic pipelines in many existing organizations, so it's important to understand them.

## Two Kinds of Classic Pipelines

1. **Classic Build pipelines** — the CI side (compile, test, publish artifacts).
2. **Classic Release pipelines** — the CD side (deploy artifacts to environments/stages).

> In Classic, build (CI) and release (CD) are **separate** definitions. In YAML, they're unified in one multi-stage file.

## Building a Classic Build Pipeline (GUI)

1. **Pipelines → New pipeline → Use the classic editor**.
2. Select your **source** (Azure Repos Git, GitHub, etc.) and repo/branch.
3. Choose a **template** (e.g., ".NET Desktop", "Node.js", or "Empty job").
4. Add **tasks** to the job by clicking **+** and searching the task catalog (e.g., "npm", "Visual Studio Build", "Publish Artifacts").
5. Configure each task's inputs in the right-hand panel.
6. Set **triggers**, **variables**, and **agent pool** via the tabs.
7. **Save & queue** to run.

## Classic Release Pipelines (GUI)

1. **Pipelines → Releases → New pipeline**.
2. Add an **artifact** source (the build pipeline's output).
3. Add **stages** (e.g., Dev → QA → Prod).
4. In each stage, define **tasks** (deploy steps).
5. Configure **pre/post-deployment approvals** and **gates**.
6. Enable the **continuous deployment trigger** to auto-create releases on new builds.

```
[Build Artifact] → [Dev stage] → [QA stage] → [Prod stage]
                      (approval)    (approval)   (approval)
```

## Pros and Cons of Classic

**Pros:**
- Visual and approachable for beginners.
- Rich task picker with inline help.
- Easy to click together a quick pipeline.

**Cons:**
- **Not version-controlled** — changes aren't in your repo or reviewable in PRs.
- Hard to **copy/reuse** across projects.
- No history/diff of pipeline changes alongside code.
- Microsoft is steering everyone toward YAML.

## Classic vs YAML (Preview)

| | Classic | YAML |
| --- | ------- | ---- |
| Stored in repo | ❌ | ✅ |
| Code review | ❌ | ✅ (PRs) |
| Reusable templates | Limited (task groups) | ✅ |
| Build + release unified | ❌ (separate) | ✅ (multi-stage) |
| Recommended for new work | ❌ | ✅ |

## When You Might Still Use Classic

- Maintaining legacy pipelines that already exist.
- Classic **release** pipelines with complex GUI gates that haven't been migrated.
- Quick experiments where you want a visual task picker.

> **Recommendation:** Author new pipelines in **YAML**. You can export a Classic pipeline's tasks to YAML to help migrate.

## Summary

- Classic pipelines are GUI-defined; build and release are separate.
- They're approachable but not version-controlled or easily reusable.
- Prefer **YAML** for new pipelines; understand Classic for existing systems.

## Knowledge Check

1. What is the biggest disadvantage of Classic pipelines vs YAML?
2. In Classic, are CI (build) and CD (release) one definition or two?
3. Where do you add deployment approvals in a Classic release pipeline?

➡️ Next: [04 - YAML Pipelines](./04-YAML-Pipelines.md)
