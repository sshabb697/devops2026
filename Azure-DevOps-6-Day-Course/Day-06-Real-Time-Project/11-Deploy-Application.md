# 11 - Deploy Application

## Overview

Time to run the full flow and deploy Contoso Tasks. We'll cover both a **simulated deploy** (works for everyone) and a **real Azure Web App deploy** (if you have an Azure subscription).

## Trigger the Pipeline

Make a change via the GitHub Flow we set up:

```bash
git checkout main && git pull origin main
git checkout -b feature/20-release
# small change, e.g., bump version in package.json
git commit -am "Prepare release"
git push -u origin feature/20-release
```

Open a PR → build validation passes → approve → **Complete (Squash)**. The merge to `main` triggers the multi-stage pipeline.

## Watch It Flow

1. **Build** — installs, tests, publishes `drop`.
2. **DeployDev** — downloads `drop`, runs the deploy (auto).
3. **DeployProd** — **pauses** for your **approval** + branch control.

## Approve Production

1. On the paused run, click **Review → Approve** (add a comment).
2. **DeployProd** proceeds.

✅ **Checkpoint:** The app is "deployed" to Dev automatically and to Prod after approval.

---

## Option A — Simulated Deploy (default)

The deploy steps use `echo`/scripts, so no cloud account is needed. You can make the simulation more realistic:

```yaml
deploy:
  steps:
    - download: current
      artifact: drop
    - script: |
        echo "Starting deployment of Contoso Tasks..."
        ls -la $(Pipeline.Workspace)/drop
        echo "Deployment complete. Version: $(Build.BuildNumber)"
      displayName: 'Deploy (simulated)'
```

## Option B — Real Azure Web App Deploy

If you have an Azure subscription:

1. Create an **Azure Web App** (Linux, Node 20) in the portal or CLI:
   ```bash
   az group create -n contoso-rg -l eastus
   az appservice plan create -g contoso-rg -n contoso-plan --is-linux --sku B1
   az webapp create -g contoso-rg -p contoso-plan -n contoso-tasks-<unique> --runtime "NODE:20-lts"
   ```
2. Create an **Azure Resource Manager service connection** (Day 5, lesson 03) named `azure-prod` (use **workload identity federation**).
3. Replace the prod deploy step:
   ```yaml
   deploy:
     steps:
       - download: current
         artifact: drop
       - task: AzureWebApp@1
         inputs:
           azureSubscription: 'azure-prod'
           appName: 'contoso-tasks-<unique>'
           package: '$(Pipeline.Workspace)/drop'
   ```
4. Run the pipeline and approve prod. Browse to `https://contoso-tasks-<unique>.azurewebsites.net/health`.

✅ **Checkpoint:** The live app responds at its URL.

---

## Verify the Deployment History

- **Environments → production** → see the new deployment entry (run, commit, who approved).
- **Environments → dev** → see its deployment history too.

## Verification

- [ ] Full pipeline ran: Build → DeployDev → (approval) → DeployProd.
- [ ] Production required and received approval.
- [ ] (Option B) The app is reachable in Azure.
- [ ] Deployment history recorded on both environments.

## Summary

- Ran the end-to-end CI/CD flow and deployed the app.
- Production deployed only after approval and branch control.
- Optionally deployed to a real Azure Web App via a service connection.

➡️ Next: [12 - Monitor Pipeline](./12-Monitor-Pipeline.md)
