# 04 - Push to Azure Repos

## Overview

Your app runs locally and you can build artifacts. Now put the **source code** in **Azure Repos** so Azure Pipelines can build it on every push.

> **Remember:** You push **source code**, not the `publish/` folder or ZIP. The pipeline creates artifacts in the cloud.

## Prerequisites

- [Day 1 lab](../Day-01-Azure-DevOps-Fundamentals/15-Hands-On-Lab.md) completed — you have an **organization** and **project**.
- [Git installed](../Day-02-Azure-Repos-Git/03-Git-Installation.md).
- ContosoTasks project from lessons 02–03.

---

## Step 1 — Create a Repository in Azure DevOps

1. Open your project at [https://dev.azure.com](https://dev.azure.com).
2. Go to **Repos → Files**.
3. If a repo already exists and you want a fresh one: **Repos → ⋯ → New repository**.
4. Name it `ContosoTasks` → **Create**.

Copy the **remote URL** (HTTPS), e.g.:

```
https://dev.azure.com/MyOrg/MyProject/_git/ContosoTasks
```

---

## Step 2 — Add Pipeline YAML to the Repo

Copy the CI pipeline file into your project root. From the course repo:

**PowerShell:**

```powershell
copy "path\to\repo\Azure-DevOps-6-Day-Course\Sample-Applications\DotNet\azure-pipelines.yml" `
     C:\devops-labs\ContosoTasks\azure-pipelines.yml
```

Or create `azure-pipelines.yml` manually (we will use it in lesson 05):

```yaml
trigger:
  - main

pr:
  - main

pool:
  vmImage: 'ubuntu-latest'

variables:
  buildConfiguration: 'Release'

steps:
  - task: UseDotNet@2
    displayName: 'Use .NET SDK 8.x'
    inputs:
      packageType: 'sdk'
      version: '8.x'

  - task: DotNetCoreCLI@2
    displayName: 'Restore'
    inputs:
      command: 'restore'
      projects: '**/*.csproj'

  - task: DotNetCoreCLI@2
    displayName: 'Build'
    inputs:
      command: 'build'
      projects: '**/*.csproj'
      arguments: '--configuration $(buildConfiguration) --no-restore'

  - task: DotNetCoreCLI@2
    displayName: 'Test'
    inputs:
      command: 'test'
      projects: '**/*Tests.csproj'
      arguments: '--configuration $(buildConfiguration)'

  - task: DotNetCoreCLI@2
    displayName: 'Publish'
    inputs:
      command: 'publish'
      publishWebProjects: true
      arguments: '--configuration $(buildConfiguration) --output $(Build.ArtifactStagingDirectory)'
      zipAfterPublish: true

  - task: PublishPipelineArtifact@1
    displayName: 'Publish artifact'
    inputs:
      targetPath: '$(Build.ArtifactStagingDirectory)'
      artifact: 'drop'
```

---

## Step 3 — Initialize Git and Commit

From your `ContosoTasks` folder:

```powershell
cd C:\devops-labs\ContosoTasks

git init
git add .
git status
```

Confirm `publish/`, `bin/`, `obj/`, and `*.zip` are **not** listed (thanks to `.gitignore`).

```powershell
git commit -m "Initial commit: Contoso Tasks API with CI pipeline"
```

---

## Step 4 — Connect to Azure Repos and Push

```powershell
git branch -M main
git remote add origin https://dev.azure.com/MyOrg/MyProject/_git/ContosoTasks
git push -u origin main
```

Replace the URL with your repository URL. Sign in when prompted (PAT or browser auth).

✅ **Checkpoint:** In Azure DevOps → **Repos → Files**, you see your source code and `azure-pipelines.yml`.

---

## Visual — Local to Remote

```
  YOUR LAPTOP                              AZURE DEVOPS
  ┌────────────────────┐                  ┌─────────────────────────┐
  │ ContosoTasks/      │    git push      │ Repos: ContosoTasks     │
  │ ├── src/           │ ──────────────►  │ ├── src/                │
  │ ├── tests/         │                  │ ├── tests/              │
  │ ├── .gitignore     │                  │ ├── .gitignore          │
  │ └── azure-         │                  │ └── azure-pipelines.yml │
  │     pipelines.yml  │                  │                         │
  └────────────────────┘                  └─────────────────────────┘

  NOT pushed: publish/, bin/, obj/, *.zip
```

---

## Step 5 — Verify on the Web

1. **Repos → Files** — browse `src/ContosoTasks/Program.cs`.
2. **Repos → Commits** — see your initial commit.
3. **Repos → Branches** — `main` should exist.

---

## Authentication Tips

| Method | When to use |
| ------ | ----------- |
| **Browser login** | Easiest when Git Credential Manager is installed (default on Windows) |
| **Personal Access Token (PAT)** | CI scripts, Linux, or when browser auth fails |

To create a PAT: **User settings → Personal access tokens → New Token** → scope **Code (Read & write)**.

---

## Troubleshooting

| Problem | Fix |
| ------- | --- |
| `remote origin already exists` | `git remote set-url origin <new-url>` |
| `failed to push` / auth | Use PAT as password; enable HTTPS credential helper |
| Large files rejected | Ensure `publish/` and `bin/` are in `.gitignore` |

---

## Summary

- Source code lives in **Azure Repos**; build artifacts do not.
- `azure-pipelines.yml` in the repo root defines the CI pipeline (next lesson).
- `git push` to `main` will trigger the pipeline once it is created.

## Knowledge Check

1. Why do we not commit the `publish/` folder?
2. Where does `azure-pipelines.yml` need to live in the repository?
3. What branch name does the pipeline trigger on?

➡️ Next: [05 - Create CI Pipeline](./05-Create-CI-Pipeline.md)
