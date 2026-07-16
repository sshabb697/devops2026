# 06 - Deploy to Azure App Service

## Overview

**CD (Continuous Deployment)** takes the `drop` artifact from CI and deploys it to **Azure App Service** — a managed platform for hosting web apps. After this lesson, your API will be live on a public URL.

> **Goal:** `https://contoso-tasks-<yourname>.azurewebsites.net/health` returns `{ "status": "ok" }`.

---

## End-to-End Flow (Visual)

```
  Developer          Azure DevOps                    Azure
  ─────────          ────────────                    ─────

  git push ───────►  CI: Build & Test
                     Publish artifact "drop"
                            │
                            ▼
                     CD: Deploy stage
                     (AzureWebApp@1)  ──────────►  App Service
                                                   (hosts .NET 8 API)
                            │
                            ▼
                     https://your-app.azurewebsites.net
```

---

## Prerequisites

- Lessons 01–05 complete (CI pipeline working, `drop` artifact exists).
- An [Azure subscription](https://azure.microsoft.com/free/) (free tier works).
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) installed (optional but recommended).

---

## Part 1 — Create Azure App Service

You need three Azure resources: **Resource Group**, **App Service Plan**, and **Web App**.

### Option A — Azure Portal

1. Go to [https://portal.azure.com](https://portal.azure.com).
2. **Create a resource** → **Web App**.
3. Settings:
   - **Resource Group:** `contoso-devops-rg` (create new)
   - **Name:** `contoso-tasks-<your-unique-suffix>` (globally unique)
   - **Publish:** Code
   - **Runtime stack:** `.NET 8 (LTS)`
   - **Operating System:** Linux (recommended) or Windows
   - **Region:** nearest to you
   - **Pricing plan:** Free F1 or Basic B1
4. Click **Review + create** → **Create**.

### Option B — Azure CLI

```powershell
# Login once
az login

# Set variables — change WEBAPP_NAME to something globally unique
$RESOURCE_GROUP = "contoso-devops-rg"
$LOCATION = "eastus"
$PLAN_NAME = "contoso-plan"
$WEBAPP_NAME = "contoso-tasks-yourname123"

az group create --name $RESOURCE_GROUP --location $LOCATION

az appservice plan create `
  --name $PLAN_NAME `
  --resource-group $RESOURCE_GROUP `
  --is-linux `
  --sku B1

az webapp create `
  --name $WEBAPP_NAME `
  --resource-group $RESOURCE_GROUP `
  --plan $PLAN_NAME `
  --runtime "DOTNET:8.0"
```

Write down your **Web App name** — you need it in the pipeline YAML.

✅ **Checkpoint:** In the portal, your Web App status is **Running**. Browse to `https://<WEBAPP_NAME>.azurewebsites.net` — you may see a default page (no app deployed yet).

---

## Part 2 — Create a Service Connection

Pipelines need permission to deploy to Azure without storing passwords in YAML.

1. Azure DevOps → **Project settings** → **Service connections**.
2. **New service connection** → **Azure Resource Manager** → **Next**.
3. Choose **Service principal (automatic)** (recommended) or **Workload identity federation**.
4. Select your **Subscription** and **Resource group** (`contoso-devops-rg`).
5. Name: `azure-contoso-connection`.
6. Check **Grant access permission to all pipelines** (for the lab) → **Save**.

✅ **Checkpoint:** Service connection `azure-contoso-connection` appears with a green status.

> Production tip: restrict which pipelines can use the connection — see [Day 5 — Service Connections](../Day-05-Deployments-and-Administration/03-Service-Connections.md).

---

## Part 3 — Create a Deployment Environment (Optional but Recommended)

1. **Pipelines → Environments → New environment**.
2. Name: `production` → **Create**.

This records deployment history and lets you add approvals later.

---

## Part 4 — Upgrade Pipeline to CI/CD

Replace `azure-pipelines.yml` with the multi-stage version. Use the file from the sample app:

**`azure-pipelines-full.yml`** in [Sample-Applications/DotNet](../Sample-Applications/DotNet/azure-pipelines-full.yml)

Or copy this YAML (update `azureSubscription` and `appName`):

```yaml
trigger:
  - main

pr:
  - main

pool:
  vmImage: 'ubuntu-latest'

variables:
  buildConfiguration: 'Release'
  azureSubscription: 'azure-contoso-connection'   # your service connection name
  webAppName: 'contoso-tasks-yourname123'         # your App Service name

stages:
  - stage: Build
    displayName: 'Build & Test'
    jobs:
      - job: Build
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

  - stage: Deploy
    displayName: 'Deploy to Azure App Service'
    dependsOn: Build
    condition: succeeded()
    jobs:
      - deployment: DeployWebApp
        displayName: 'Deploy to App Service'
        environment: 'production'
        strategy:
          runOnce:
            deploy:
              steps:
                - download: current
                  artifact: drop

                - task: AzureWebApp@1
                  displayName: 'Deploy ZIP to App Service'
                  inputs:
                    azureSubscription: '$(azureSubscription)'
                    appType: 'webAppLinux'
                    appName: '$(webAppName)'
                    package: '$(Pipeline.Workspace)/drop/**/*.zip'
```

**Commit and push:**

```powershell
git add azure-pipelines.yml
git commit -m "Add CD stage: deploy to Azure App Service"
git push
```

On first run, authorize the **service connection** and **environment** when prompted.

---

## Part 5 — Verify Deployment

1. Watch the pipeline: **Build** stage → **Deploy** stage.
2. When both succeed, open:

```
https://<WEBAPP_NAME>.azurewebsites.net/health
```

**PowerShell:**

```powershell
Invoke-RestMethod "https://contoso-tasks-yourname123.azurewebsites.net/health"
```

✅ **Checkpoint:** Live URL returns `{ "status": "ok" }`.

3. Try other endpoints:

```
https://<WEBAPP_NAME>.azurewebsites.net/
https://<WEBAPP_NAME>.azurewebsites.net/tasks
```

4. **Pipelines → Environments → production** — see deployment history linked to the run.

---

## Full Journey — What Students Built

```
  LESSON 01-03 (local)          LESSON 04-05 (CI)           LESSON 06 (CD)
  ────────────────────          ─────────────────           ──────────────

  Install .NET                  Push to Azure Repos         App Service in Azure
  dotnet run localhost    →     Pipeline builds on push  →  AzureWebApp@1 deploys
  dotnet publish → ZIP          Artifact "drop" in cloud      Public HTTPS URL
```

---

## Troubleshooting

| Problem | Fix |
| ------- | --- |
| `azureSubscription` not found | Match exact service connection name in Project Settings |
| Deploy failed — package not found | Check `package:` path; list `$(Pipeline.Workspace)/drop` in a script step |
| App shows default page | Wrong runtime — set App Service to **.NET 8**; redeploy |
| 500 error after deploy | **App Service → Log stream**; enable **Application Logging** |
| Linux vs Windows | Use `appType: webAppLinux` for Linux; `webApp` for Windows |

---

## Enhancements (Next Steps)

| Enhancement | Where to learn |
| ----------- | -------------- |
| Approval before production deploy | [Day 5 — Approvals](../Day-05-Deployments-and-Administration/06-Approvals.md) |
| Separate Dev and Prod stages | [Day 5 — Environments](../Day-05-Deployments-and-Administration/01-Environments.md) |
| Branch policies on `main` | [Day 2 — Branch Policies](../Day-02-Azure-Repos-Git/08-Branch-Policies.md) |
| Full end-to-end project | [Day 6 — Real-Time Project](../Day-06-Real-Time-Project/) |

---

## Deliverables Checklist

- [ ] Azure App Service created (.NET 8 runtime)
- [ ] Service connection configured in Azure DevOps
- [ ] Multi-stage pipeline: Build → Deploy
- [ ] App live at `https://<name>.azurewebsites.net/health`
- [ ] Deployment recorded on the `production` environment

---

## Summary

- **Azure App Service** hosts your published .NET app without managing VMs.
- A **service connection** lets the pipeline deploy securely to Azure.
- **CD** downloads the `drop` artifact and deploys it with `AzureWebApp@1`.
- You went from `dotnet run` on localhost to a **production URL** — the full DevOps loop.

## Knowledge Check

1. What three Azure resources did you create for hosting?
2. Why is a service connection used instead of putting Azure passwords in YAML?
3. Which pipeline task deploys the ZIP to App Service?
4. What is the difference between the CI stage and the Deploy stage?

---

🎉 **Congratulations!** You deployed a .NET application from local development to Azure using Azure DevOps CI/CD.

➡️ Continue: [Day 5 — Deployments & Administration](../Day-05-Deployments-and-Administration/) for approvals, checks, and governance.
