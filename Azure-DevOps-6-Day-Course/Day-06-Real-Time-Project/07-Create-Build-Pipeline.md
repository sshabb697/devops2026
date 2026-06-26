# 07 - Create Build Pipeline

## Overview

Now we create the **CI build pipeline** that installs dependencies, runs tests, and publishes an artifact. Then we wire it into the branch policy as **build validation** so every PR must pass it.

## Step 1 — Create the Pipeline

1. **Pipelines → New pipeline**.
2. **Where is your code?** → **Azure Repos Git**.
3. Select `contoso-tasks-app`.
4. **Configure** → choose **Node.js** (or **Starter pipeline**).
5. Replace the YAML with:

```yaml
trigger:
  - main

pr:
  - main

pool:
  vmImage: 'ubuntu-latest'

steps:
  - task: NodeTool@0
    displayName: 'Install Node.js'
    inputs:
      versionSpec: '20.x'

  - task: Cache@2
    displayName: 'Cache npm'
    inputs:
      key: 'npm | "$(Agent.OS)" | package-lock.json'
      path: '$(Pipeline.Workspace)/.npm'

  - script: npm ci
    displayName: 'Install dependencies'

  - script: npm test
    displayName: 'Run tests'

  - task: PublishPipelineArtifact@1
    displayName: 'Publish artifact'
    inputs:
      targetPath: '$(System.DefaultWorkingDirectory)'
      artifact: 'drop'
```

6. **Save and run** → commit the `azure-pipelines.yml` to `main` (this initial commit is allowed; if blocked, commit to a branch and PR it).

✅ **Checkpoint:** The pipeline runs green and publishes a `drop` artifact.

## Step 2 — Rename the Pipeline (optional)

Rename to `Contoso-CI` (Pipelines → ⋯ → Rename/move) for clarity.

## Step 3 — Add Build Validation to `main`

Now enforce the build on every PR (completes Day 2 lesson 08):

1. **Repos → Branches → main → ⋯ → Branch policies**.
2. Under **Build Validation → +**:
   - Pipeline: `Contoso-CI`.
   - Trigger: **Automatic**.
   - Policy requirement: **Required**.
   - Build expiration: e.g., 12 hours.
3. Save.

✅ **Checkpoint:** `main` now requires `Contoso-CI` to pass before a PR can complete.

## Step 4 — Prove It with a Pull Request

1. Push your earlier `feature/12-health-endpoint` branch (if not already).
2. **Repos → Pull requests → New** → source `feature/12-health-endpoint` → target `main`.
3. **Link the work item** (`#12` story), add a title/description.
4. Watch the **build validation** run automatically on the PR.
5. Approve (separate account or adjust reviewer count for the solo lab) and **Complete (Squash)**.

✅ **Checkpoint:** The PR shows the required build check and merges only after it passes.

## Verification

- [ ] `Contoso-CI` pipeline builds and tests the app.
- [ ] An artifact is published.
- [ ] Build validation is required on `main`.
- [ ] A PR passed the build and merged via squash.

## Summary

- Created the `Contoso-CI` build pipeline (install → test → publish artifact).
- Added it as **required build validation** on `main`.
- Verified a PR runs the build and only merges when it passes.

➡️ Next: [08 - Create Multi-Stage Pipeline](./08-Create-Multi-Stage-Pipeline.md)
