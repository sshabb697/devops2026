# 08 - Create Multi-Stage Pipeline

## Overview

We'll evolve the single-stage CI pipeline into a **multi-stage** pipeline that builds once and then deploys to **Dev** and **Production** stages. This applies Day 3 (structure) and Day 5 (deployment jobs/environments).

## The Plan

```
Stage: Build        → install, test, publish artifact
Stage: DeployDev     → deploy to environment "dev" (automatic)
Stage: DeployProd    → deploy to environment "production" (gated next lessons)
```

## Step 1 — Update `azure-pipelines.yml`

Edit the pipeline (via a feature branch + PR, since `main` is protected):

```yaml
trigger:
  - main

pool:
  vmImage: 'ubuntu-latest'

stages:
  - stage: Build
    displayName: 'Build & Test'
    jobs:
      - job: Build
        steps:
          - task: NodeTool@0
            inputs:
              versionSpec: '20.x'
          - script: npm ci
            displayName: 'Install dependencies'
          - script: npm test
            displayName: 'Run tests'
          - task: PublishPipelineArtifact@1
            displayName: 'Publish artifact'
            inputs:
              targetPath: '$(System.DefaultWorkingDirectory)'
              artifact: 'drop'

  - stage: DeployDev
    displayName: 'Deploy to Dev'
    dependsOn: Build
    condition: succeeded()
    jobs:
      - deployment: DeployDev
        environment: 'dev'
        strategy:
          runOnce:
            deploy:
              steps:
                - download: current
                  artifact: drop
                - script: echo "Deploying Contoso Tasks to DEV..."
                  displayName: 'Deploy to Dev'

  - stage: DeployProd
    displayName: 'Deploy to Production'
    dependsOn: DeployDev
    condition: succeeded()
    jobs:
      - deployment: DeployProd
        environment: 'production'
        strategy:
          runOnce:
            deploy:
              steps:
                - download: current
                  artifact: drop
                - script: echo "Deploying Contoso Tasks to PRODUCTION..."
                  displayName: 'Deploy to Prod'
```

> The environments `dev` and `production` are created in the next lesson. Referencing them here will auto-create them on first run, but we'll create them explicitly to attach checks.

## Step 2 — Open a PR and Merge

1. Commit the YAML change on a feature branch.
2. Open a PR → it triggers the **Build** stage as validation.
3. Merge (squash) after approval.

## Step 3 — Observe the Run

After merge to `main`, the pipeline runs:
- **Build** → publishes artifact.
- **DeployDev** → downloads artifact, runs the (simulated) deploy.
- **DeployProd** → will **pause** once we attach an approval (next lessons). Until then it deploys automatically.

✅ **Checkpoint:** A multi-stage run shows Build → DeployDev → DeployProd stages.

## Build Once, Deploy Many

Notice we build the artifact **once** in the Build stage and **download the same artifact** in each deploy stage — guaranteeing Dev and Prod get identical bits (Day 3, lesson 07).

## Verification

- [ ] Pipeline now has Build, DeployDev, DeployProd stages.
- [ ] Build publishes an artifact consumed by deploy stages.
- [ ] The run progresses through the stages in order.

## Summary

- Converted CI into a multi-stage CI/CD pipeline using **deployment jobs** and **environments**.
- Applied **build once, deploy many** by sharing the `drop` artifact.
- Next we'll create the environments and gate production.

➡️ Next: [09 - Create Environments](./09-Create-Environments.md)
