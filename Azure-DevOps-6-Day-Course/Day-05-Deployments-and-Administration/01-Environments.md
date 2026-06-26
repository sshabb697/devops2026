# 01 - Environments

## Overview

An **environment** in Azure Pipelines is a named collection of deployment targets — such as a group of VMs, a Kubernetes namespace, or just a logical target like "production." Environments give you **deployment history**, **traceability**, and a place to attach **approvals and checks**.

## Why Environments?

- **Track deployments** — see what version is deployed where, and when.
- **Approvals & checks** — gate deployments to sensitive targets (e.g., production).
- **Resource targeting** — deploy to specific VMs/Kubernetes resources within the environment.
- **Security** — control who can deploy to each environment.

## Creating an Environment

1. **Pipelines → Environments → New environment**.
2. Name it (e.g., `dev`, `qa`, `production`).
3. Optionally add a **resource**:
   - **None** — a logical environment (for scripts/cloud deploys).
   - **Kubernetes** — a namespace in a cluster.
   - **Virtual machines** — register VMs via an agent script.

## Using an Environment in YAML

Environments are referenced by **deployment jobs**:

```yaml
- stage: DeployProd
  jobs:
    - deployment: Deploy
      environment: 'production'      # ← the environment
      strategy:
        runOnce:
          deploy:
            steps:
              - script: echo "Deploying..."
```

Targeting a specific resource within an environment:

```yaml
      environment:
        name: 'production'
        resourceName: 'web-vm-01'
        resourceType: VirtualMachine
```

## Deployment History

Each environment shows a **history** of deployments: which pipeline run, which commit, who triggered it, and the result. This is invaluable for audits and incident response ("what changed in prod yesterday?").

## Approvals and Checks on Environments

This is the key governance feature: on an environment you can configure **checks** (Environment → ⋯ → **Approvals and checks**), including:

- **Approvals** (human sign-off) — lesson 06.
- **Branch control**, **Business hours**, **Invoke REST API**, **Azure Policy**, etc. — lesson 07.

When a deployment job targets the environment, the pipeline **pauses** until the checks pass.

## Environment Security

Set **permissions** per environment (Environment → ⋯ → Security):
- **Creator / Administrator / User** roles.
- Restrict which pipelines/users can deploy to `production`.

## Typical Environment Setup

```
dev          → no approvals (fast feedback)
qa           → optional approval by QA lead
staging      → approval + business-hours check
production   → approval (2 people) + branch control (main only)
```

## Summary

- An environment is a named deployment target with history, security, and checks.
- Reference it from **deployment jobs** via `environment:`.
- Attach **approvals and checks** to gate deployments (especially production).
- Use environment **security** to control who can deploy where.

## Knowledge Check

1. What three things do environments provide beyond a plain deploy step?
2. Which job type targets an environment?
3. Where do you configure approvals for a production deployment?

➡️ Next: [02 - Deployment Jobs](./02-Deployment-Jobs.md)
