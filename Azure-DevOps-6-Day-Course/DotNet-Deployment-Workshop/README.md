# .NET Deployment Workshop — Local to Azure App Service

A **hands-on, step-by-step workshop** that takes students from zero to a live .NET web app on **Azure App Service**, deployed through **Azure DevOps CI/CD**.

You will do everything in order — first on your machine, then in the cloud — so each step builds on the last.

## Learning Path

```
  LOCAL (your laptop)                    AZURE DEVOPS + AZURE
  ───────────────────                    ─────────────────────

  01 Install .NET SDK
         │
         ▼
  02 Create web app → run on localhost
         │
         ▼
  03 Build & publish → generate artifact (ZIP)
         │
         ▼
  04 Push code to Azure Repos  ────────►  Remote Git repository
         │
         ▼
  05 Create CI pipeline        ────────►  Build + test + publish artifact
         │
         ▼
  06 CD + Azure App Service    ────────►  Deploy ZIP → live URL
```

## Lessons

| # | Lesson | What you do | Time |
| - | ------ | ----------- | ---- |
| 01 | [Install .NET SDK](./01-Install-DotNet-SDK.md) | Install SDK, verify `dotnet` works | 15m |
| 02 | [Create Web App & Run Locally](./02-Create-WebApp-and-Run-Locally.md) | Scaffold app, run on `localhost` | 30m |
| 03 | [Build & Publish Artifact Locally](./03-Build-Publish-Artifact-Locally.md) | `dotnet publish`, inspect output, create ZIP | 25m |
| 04 | [Push to Azure Repos](./04-Push-to-Azure-Repos.md) | Init Git, push to remote repo | 25m |
| 05 | [Create CI Pipeline](./05-Create-CI-Pipeline.md) | YAML pipeline: restore → build → test → artifact | 40m |
| 06 | [Deploy to Azure App Service](./06-Deploy-to-Azure-App-Service.md) | App Service + service connection + CD stage | 45m |

**Total:** ~3 hours of focused lab time.

## Prerequisites

- Completed [Day 1 — Azure DevOps Fundamentals](../Day-01-Azure-DevOps-Fundamentals/) (you have an **organization** and **project**).
- [Git](../Day-02-Azure-Repos-Git/03-Git-Installation.md) installed.
- A code editor ([Visual Studio Code](https://code.visualstudio.com/) recommended).
- For lesson 06: an [Azure subscription](https://azure.microsoft.com/free/) (free tier is enough).

## Sample Application

This workshop uses **Contoso Tasks** — a minimal ASP.NET Core API. You can:

- **Build it from scratch** in lesson 02 (recommended for first-time .NET learners), or
- **Copy** the ready-made app from [Sample-Applications/DotNet](../Sample-Applications/DotNet/).

Both paths produce the same result.

## When to Use This Workshop

| If you are teaching… | Use this workshop… |
| -------------------- | ------------------ |
| Day 2 (Git) concepts | After lesson 04 as the Git push lab |
| Day 3 (Pipelines) | Lessons 05–06 as the pipeline lab (use .NET instead of Node) |
| Day 5 (Deployments) | Lesson 06 for real Azure App Service deploy |
| A dedicated .NET track | Run all six lessons in one session |

## Deliverables Checklist

By the end, each student should have:

- [ ] .NET SDK installed and verified
- [ ] A web API running locally
- [ ] A published artifact (folder + ZIP) on disk
- [ ] Code pushed to an Azure Repos repository
- [ ] A CI pipeline that builds, tests, and publishes an artifact on every push to `main`
- [ ] An Azure App Service running the deployed app
- [ ] A CD stage that deploys the artifact to App Service

## Next Steps

- Add [branch policies](../Day-02-Azure-Repos-Git/08-Branch-Policies.md) and [environments with approvals](../Day-05-Deployments-and-Administration/06-Approvals.md).
- Complete the full [Day 6 Real-Time Project](../Day-06-Real-Time-Project/) with multi-stage governance.
