# Day 3 — Azure Pipelines

Today is all about automation. You'll learn how **Azure Pipelines** implements CI/CD, the difference between Classic and YAML pipelines, how to structure a pipeline, and how agents, variables, templates, and artifacts fit together. By the end you'll author a real build pipeline.

## Learning Objectives

By the end of today you will be able to:

- Explain CI/CD and how Azure Pipelines implements it.
- Compare **Classic** and **YAML** pipelines and choose appropriately.
- Read and write the **pipeline structure**: stages, jobs, steps.
- Build a working **CI build pipeline** for a **.NET** application (see [.NET Deployment Workshop](../DotNet-Deployment-Workshop/05-Create-CI-Pipeline.md)).
- Understand release/CD concepts.
- Use **variables**, **variable groups**, and **templates**.
- Publish and consume **artifacts**.
- Configure **agent pools** and choose between **Microsoft-hosted** and **self-hosted** agents.

## Lessons

| # | Lesson |
| - | ------ |
| 01 | [CI/CD](./01-CI-CD.md) |
| 02 | [Pipeline Overview](./02-Pipeline-Overview.md) |
| 03 | [Classic Pipelines](./03-Classic-Pipelines.md) |
| 04 | [YAML Pipelines](./04-YAML-Pipelines.md) |
| 05 | [Pipeline Structure](./05-Pipeline-Structure.md) |
| 06 | [Build Pipeline](./06-Build-Pipeline.md) |
| 07 | [Release Pipeline Concept](./07-Release-Pipeline-Concept.md) |
| 08 | [Variables](./08-Variables.md) |
| 09 | [Variable Groups](./09-Variable-Groups.md) |
| 10 | [Templates](./10-Templates.md) |
| 11 | [Artifacts](./11-Artifacts.md) |
| 12 | [Agent Pools](./12-Agent-Pools.md) |
| 13 | [Microsoft-Hosted Agent](./13-Microsoft-Hosted-Agent.md) |
| 14 | [Self-Hosted Agent](./14-Self-Hosted-Agent.md) |
| 15 | [Hands-On Lab](./15-Hands-On-Lab.md) |

## Sample Pipelines

Ready-to-use YAML files live in the [`YAML/`](./YAML/) folder, paired with the demo apps in [Sample-Applications](../Sample-Applications/).

For a full **.NET** path (local `dotnet publish` → CI artifact → **Azure App Service**), see the [.NET Deployment Workshop](../DotNet-Deployment-Workshop/).

> Keep the [Azure DevOps Cheat Sheet](../Resources/Azure-DevOps-Cheat-Sheet.md) handy for YAML keywords and predefined variables.
