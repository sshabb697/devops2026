# 15 - Hands-On Lab: Build Your First CI Pipeline

## Goal

Create a YAML CI pipeline that builds and tests a sample application, publishes an artifact, and runs automatically on every push. Then add a second stage and a variable group.

**Estimated time:** 60 minutes

## Prerequisites

- Completed Day 2 lab (code in `Course-Project`).
- One of the [Sample-Applications](../Sample-Applications/) pushed to your repo (NodeJS is quickest).

---

## Part 1 — Add Sample Code

Copy a sample app into your repo (NodeJS example):

```bash
# From your cloned Course-Project repo
cp -r /path/to/Sample-Applications/NodeJS/* .
git add .
git commit -m "Add Node.js sample app"
git push origin main
```

> Or use the [Sample-Applications/NodeJS](../Sample-Applications/NodeJS/) files as a reference and recreate them.

---

## Part 2 — Create the YAML Pipeline

1. **Pipelines → New pipeline**.
2. Choose **Azure Repos Git** → select `Course-Project`.
3. Choose **Starter pipeline** (or **Node.js**).
4. Replace the contents with:

```yaml
trigger:
  - main

pool:
  vmImage: 'ubuntu-latest'

steps:
  - task: NodeTool@0
    inputs:
      versionSpec: '20.x'
    displayName: 'Install Node.js'

  - script: npm ci
    displayName: 'Install dependencies'

  - script: npm test
    displayName: 'Run tests'

  - task: PublishPipelineArtifact@1
    inputs:
      targetPath: '$(System.DefaultWorkingDirectory)'
      artifact: 'drop'
    displayName: 'Publish artifact'
```

5. Click **Save and run** → commit directly to `main`.

✅ **Checkpoint:** The run starts, the steps execute, and you see green checkmarks. An artifact named `drop` appears in the run summary.

---

## Part 3 — Verify CI Triggers

```bash
# Make a small change and push
echo "// trivial change" >> app.js
git commit -am "Trigger CI"
git push origin main
```

✅ **Checkpoint:** A new run starts automatically (continuous integration working).

---

## Part 4 — Add a Variable Group

1. **Pipelines → Library → + Variable group** → name it `app-settings`.
2. Add a variable `greeting` = `Hello from CI`.
3. Save.
4. Edit your pipeline YAML to use it:

```yaml
variables:
  - group: 'app-settings'

# add a step:
  - script: echo "$(greeting)"
    displayName: 'Print greeting'
```

5. Save and run.

✅ **Checkpoint:** The log prints `Hello from CI`.

> When prompted, **authorize** the pipeline to use the variable group.

---

## Part 5 — Add a Second Stage (Multi-Stage)

Convert to a multi-stage pipeline with a (simulated) deploy stage:

```yaml
trigger:
  - main

pool:
  vmImage: 'ubuntu-latest'

stages:
  - stage: Build
    jobs:
      - job: Build
        steps:
          - task: NodeTool@0
            inputs:
              versionSpec: '20.x'
          - script: npm ci
          - script: npm test
          - task: PublishPipelineArtifact@1
            inputs:
              targetPath: '$(System.DefaultWorkingDirectory)'
              artifact: 'drop'

  - stage: DeployDev
    dependsOn: Build
    condition: succeeded()
    jobs:
      - job: Deploy
        steps:
          - download: current
            artifact: drop
          - script: echo "Deploying to Dev..."
```

Save and run.

✅ **Checkpoint:** Two stages run in order; `DeployDev` downloads the `drop` artifact.

---

## Part 6 — Add Build Validation to a Branch Policy

1. **Repos → Branches → main → ⋯ → Branch policies**.
2. Under **Build Validation**, add your pipeline.
3. Now create a branch, push a change, and open a PR — the CI build must pass before merge.

✅ **Checkpoint:** The PR shows a required build check.

---

## Deliverables / Verification

- [ ] A YAML pipeline that builds and tests the app.
- [ ] CI triggers automatically on push.
- [ ] A **variable group** used in the pipeline.
- [ ] A **multi-stage** pipeline with a deploy stage consuming an artifact.
- [ ] **Build validation** wired into a branch policy.

---

## Reflection Questions

1. Why publish an artifact in the Build stage instead of rebuilding in Deploy?
2. What would you change to deploy to a real environment with an approval?
3. When would you switch from `ubuntu-latest` to a self-hosted pool?

---

🎉 **Excellent!** You can now automate builds. Tomorrow you'll plan and track the work that feeds these pipelines using Azure Boards.

➡️ Continue to [Day 4 — Azure Boards](../Day-04-Azure-Boards/README.md)
