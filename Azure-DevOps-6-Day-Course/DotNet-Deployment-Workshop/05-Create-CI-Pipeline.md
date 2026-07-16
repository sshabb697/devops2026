# 05 - Create CI Pipeline

## Overview

A **CI (Continuous Integration) pipeline** automatically builds and tests your code every time you push to the repository. It produces the same **artifact** you created manually in lesson 03 — but on a clean build agent in the cloud.

> **Goal:** Push to `main` → pipeline runs → green build → `drop` artifact published.

---

## What CI Does (Visual)

```
  git push to main
        │
        ▼
  ┌─────────────────────────────────────────────────────────────┐
  │  AZURE PIPELINES (Microsoft-hosted agent — ubuntu-latest)   │
  │                                                             │
  │  1. Checkout code                                           │
  │  2. Install .NET 8 SDK        (UseDotNet@2)                 │
  │  3. dotnet restore            (DotNetCoreCLI@2)             │
  │  4. dotnet build Release      (DotNetCoreCLI@2)             │
  │  5. dotnet test               (DotNetCoreCLI@2)             │
  │  6. dotnet publish → ZIP      (DotNetCoreCLI@2)             │
  │  7. Upload artifact "drop"    (PublishPipelineArtifact@1)   │
  └─────────────────────────────────────────────────────────────┘
        │
        ▼
  Artifact "drop" stored — ready for CD (lesson 06)
```

---

## Prerequisites

- Lesson 04 complete — code and `azure-pipelines.yml` are in Azure Repos.

---

## Step 1 — Create the Pipeline

1. In your Azure DevOps project, go to **Pipelines → Pipelines**.
2. Click **New pipeline** (or **Create Pipeline**).
3. **Where is your code?** → **Azure Repos Git**.
4. Select the **ContosoTasks** repository.
5. **Configure your pipeline** → **Existing Azure Pipelines YAML file**.
6. Branch: `main`, Path: `/azure-pipelines.yml`.
7. Click **Continue** — review the YAML.
8. Click **Run** (or **Save and run**).

Authorize any prompts (resources, permissions).

✅ **Checkpoint:** A pipeline run starts automatically.

---

## Step 2 — Watch the Run

1. Click the running build number (e.g., `#20240609.1`).
2. Expand each step and compare to what you did locally:

| Pipeline step | Local equivalent (lesson 03) |
| ------------- | ---------------------------- |
| Use .NET SDK 8.x | `dotnet --version` |
| Restore | `dotnet restore` |
| Build | `dotnet build -c Release` |
| Test | `dotnet test` |
| Publish | `dotnet publish` + zip |
| Publish artifact | Your `ContosoTasks.zip` |

3. Wait for all steps to complete with green checkmarks.

✅ **Checkpoint:** Pipeline status is **Succeeded**.

---

## Step 3 — Inspect the Artifact

1. On the completed run, click **Summary** (or the run title).
2. Under **Related** or **Artifacts**, click **drop**.
3. Download and unzip — you should see the same structure as your local `publish/` folder.

```
drop/
└── ContosoTasks.zip    (or ContosoTasks/ folder inside)
```

This is the package lesson 06 will deploy to Azure App Service.

---

## Step 4 — Trigger on Push

Make a small change and push to verify CI triggers automatically:

```powershell
cd C:\devops-labs\ContosoTasks
# Edit welcome message in Program.cs, e.g. change "Welcome" text
git add .
git commit -m "Update welcome message"
git push
```

1. Go to **Pipelines** — a new run should start within seconds.
2. Confirm it succeeds.

✅ **Checkpoint:** Second pipeline run triggered by `git push` to `main`.

---

## Understand the YAML

Key sections of `azure-pipelines.yml`:

```yaml
trigger:          # Run when code is pushed to main
  - main

pr:               # Also run on pull requests to main
  - main

pool:             # Use Microsoft's Linux build VM
  vmImage: 'ubuntu-latest'

variables:
  buildConfiguration: 'Release'

steps:
  - task: UseDotNet@2          # Install SDK on the agent
  - task: DotNetCoreCLI@2      # restore, build, test, publish
  - task: PublishPipelineArtifact@1   # Save output for later stages
```

| Keyword | Meaning |
| ------- | ------- |
| `trigger` | Branches that start a CI build on push |
| `pool` | Which build agents to use |
| `task` | Pre-built action from Azure DevOps |
| `$(Build.ArtifactStagingDirectory)` | Agent folder where publish output goes |
| `artifact: 'drop'` | Name other stages use to download this output |

---

## Troubleshooting

| Failure | Common cause | Fix |
| ------- | ------------ | --- |
| Restore failed | Wrong path to `.csproj` | Ensure solution layout matches `**/*.csproj` |
| Test failed | Tests missing or failing | Run `dotnet test` locally first |
| Publish failed | Not a web project | `publishWebProjects: true` requires a Web SDK project |
| No artifact | Publish step failed | Fix publish; check `targetPath` |

See [Day 6 Troubleshooting](../Day-06-Real-Time-Project/13-Troubleshooting.md) for more.

---

## Summary

- CI runs the same build/test/publish steps you did locally — on every push.
- The **`drop` artifact** is the deployable ZIP stored by the pipeline.
- Next: add a **CD stage** to deploy `drop` to **Azure App Service**.

## Knowledge Check

1. What triggers this pipeline to run?
2. What is the name of the published artifact?
3. Which task installs the .NET SDK on the build agent?

➡️ Next: [06 - Deploy to Azure App Service](./06-Deploy-to-Azure-App-Service.md)
