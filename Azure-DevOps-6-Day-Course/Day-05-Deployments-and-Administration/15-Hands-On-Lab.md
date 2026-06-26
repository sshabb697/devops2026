# 15 - Hands-On Lab: Secure Multi-Stage Deployment

## Goal

Extend your CI pipeline into a governed CD pipeline: create environments, add a deployment job, gate production with an approval and a branch-control check, and use a variable group/secure file. Then review security and audit settings.

**Estimated time:** 60 minutes

## Prerequisites

- Completed Day 3 lab (you have a working CI pipeline in `Course-Project`).

---

## Part 1 — Create Environments

1. **Pipelines → Environments → New environment** → name `dev` → Resource: **None** → Create.
2. Repeat to create `production`.

✅ **Checkpoint:** Two environments exist.

---

## Part 2 — Add an Approval to Production

1. Open **production → ⋯ → Approvals and checks → + → Approvals**.
2. Add yourself as an approver.
3. Enable **"Requestors can't approve their own runs"** is optional for this solo lab — you can leave it off so you can approve.
4. Set a **timeout** (e.g., 1 day). Save.

---

## Part 3 — Add a Branch Control Check

1. **production → Approvals and checks → + → Branch control**.
2. Allowed branches: `refs/heads/main`.
3. Save.

✅ **Checkpoint:** Production has an Approval **and** a Branch control check.

---

## Part 4 — Add a Variable Group

1. **Pipelines → Library → + Variable group** → `deploy-settings`.
2. Add `targetUrl` = `https://example-dev.local` (and mark a `apiKey` value as **secret** for practice).
3. Save.

---

## Part 5 — Convert the Pipeline to Multi-Stage

Edit your `azure-pipelines.yml`:

```yaml
trigger:
  - main

pool:
  vmImage: 'ubuntu-latest'

variables:
  - group: 'deploy-settings'

stages:
  - stage: Build
    jobs:
      - job: Build
        steps:
          - script: echo "Build & test..."
          - task: PublishPipelineArtifact@1
            inputs:
              targetPath: '$(System.DefaultWorkingDirectory)'
              artifact: 'drop'

  - stage: DeployDev
    dependsOn: Build
    jobs:
      - deployment: DeployDev
        environment: 'dev'
        strategy:
          runOnce:
            deploy:
              steps:
                - download: current
                  artifact: drop
                - script: echo "Deploying to $(targetUrl)"

  - stage: DeployProd
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
                - script: echo "Deploying to PRODUCTION"
```

Save and run (authorize the variable group/environments when prompted).

✅ **Checkpoint:** Build → DeployDev run automatically; **DeployProd pauses** waiting for approval.

---

## Part 6 — Approve the Production Deployment

1. On the paused run, click **Review → Approve**.
2. Watch DeployProd proceed.

✅ **Checkpoint:** Production deploys only after your approval.

> Try running the pipeline from a **non-main branch** — the branch control check should block production.

---

## Part 7 — (Optional) Add a Secure File

1. **Library → Secure files → + Secure file** → upload any small text file named `config.env`.
2. Add a step in DeployProd:
   ```yaml
   - task: DownloadSecureFile@1
     name: cfg
     inputs:
       secureFile: 'config.env'
   - script: echo "Secure file at $(cfg.secureFilePath)"
   ```
3. Run and authorize.

---

## Part 8 — Review Security & Audit

1. **Project settings → Service connections** — review (create an Azure RM connection if you have a subscription).
2. **Environments → production → ⋯ → Security** — note who can deploy.
3. **Organization settings → Auditing** — explore recent events (enable if needed).

---

## Deliverables / Verification

- [ ] `dev` and `production` environments created.
- [ ] Production gated by an **approval** and a **branch control** check.
- [ ] A **variable group** consumed by the pipeline.
- [ ] A multi-stage pipeline: Build → DeployDev → DeployProd (approved).
- [ ] (Optional) A **secure file** downloaded in the prod stage.
- [ ] Reviewed environment **security** and **audit logs**.

---

## Reflection Questions

1. Why attach approvals to the **environment** rather than writing them in YAML?
2. How does branch control reduce the risk of deploying the wrong code to prod?
3. What would you add to make production deployments safer (hint: lesson 07)?

---

🎉 **Outstanding!** You can now deploy with governance. Tomorrow you'll combine everything into a complete real-time project.

➡️ Continue to [Day 6 — Real-Time Project](../Day-06-Real-Time-Project/README.md)
