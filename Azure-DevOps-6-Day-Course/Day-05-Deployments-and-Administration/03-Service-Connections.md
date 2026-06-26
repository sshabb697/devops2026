# 03 - Service Connections

## Overview

A **service connection** is a secured, stored credential/endpoint that lets your pipelines authenticate to **external services** — Azure, AWS, GCP, Docker registries, Kubernetes, GitHub, and more — without putting secrets in your YAML.

## Why Service Connections?

- **Security** — credentials are encrypted and managed centrally, not in code.
- **Reuse** — one connection used by many pipelines.
- **Governance** — control which pipelines can use a connection (authorization).
- **Auditability** — usage is tracked.

## Where to Manage

**Project settings → Service connections**. Each project has its own list (can be shared across projects).

## Common Connection Types

| Type | Used for |
| ---- | -------- |
| **Azure Resource Manager** | Deploy to Azure (App Service, AKS, VMs, etc.) |
| **Docker Registry** | Push/pull container images (ACR, Docker Hub) |
| **Kubernetes** | Deploy to a cluster |
| **GitHub** | Access GitHub repos |
| **AWS / GCP** | Deploy to other clouds (via extensions) |
| **Generic** | Any service with a URL + credentials |
| **SSH** | Deploy to servers over SSH |

## Creating an Azure Resource Manager Connection

1. **Project settings → Service connections → New service connection → Azure Resource Manager**.
2. Choose an authentication method:
   - **Workload identity federation (recommended)** — passwordless, uses OIDC; no secret to rotate.
   - **Service principal (automatic/manual)** — uses an app registration + secret/certificate.
   - **Managed identity** — for self-hosted agents on Azure.
3. Select the **subscription** / **resource group** scope.
4. Name it (e.g., `azure-prod`) and save.

## Using a Service Connection in YAML

Reference it by name in tasks that need it:

```yaml
steps:
  - task: AzureWebApp@1
    inputs:
      azureSubscription: 'azure-prod'   # ← service connection name
      appName: 'my-web-app'
      package: '$(Pipeline.Workspace)/drop/**/*.zip'
```

Docker example:

```yaml
  - task: Docker@2
    inputs:
      containerRegistry: 'my-acr'       # ← Docker service connection
      repository: 'myapp'
      command: 'buildAndPush'
      tags: '$(Build.BuildId)'
```

## Security & Authorization

- A new connection can be set to **"Grant access permission to all pipelines"** or restricted.
- Restrict to specific pipelines via **Security → Pipeline permissions**.
- Set **user roles** (Administrator / User) on the connection.
- Prefer **workload identity federation** to avoid stored secrets entirely.

## Best Practices

- Use **workload identity federation** (no secrets to leak or rotate).
- **Scope** connections narrowly (a resource group, not the whole subscription, when possible).
- **Restrict** which pipelines can use production connections.
- Use **separate connections** per environment (`azure-dev`, `azure-prod`).
- Combine with **environment approvals** so production deploys are gated.

## Summary

- A service connection securely stores credentials to external services for pipelines.
- Common types: Azure Resource Manager, Docker, Kubernetes, GitHub, AWS/GCP, SSH.
- Reference by name in tasks (e.g., `azureSubscription: 'azure-prod'`).
- Prefer **workload identity federation**; restrict and scope connections tightly.

## Knowledge Check

1. Why store credentials in a service connection instead of YAML?
2. Which Azure auth method is passwordless and recommended?
3. How do you limit which pipelines can use a production connection?

➡️ Next: [04 - Library](./04-Library.md)
