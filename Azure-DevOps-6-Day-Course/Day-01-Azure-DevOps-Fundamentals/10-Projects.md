# 10 - Projects

## Overview

A **project** is a container within an organization that holds everything a team needs to build a product: boards, repositories, pipelines, test plans, and artifacts. It is the primary **security and isolation boundary** in Azure DevOps.

## Creating a Project

From the organization home page:

1. Click **+ New project**.
2. Provide:
   - **Project name** (e.g., `eShopOnWeb`).
   - **Description** (optional but recommended).
   - **Visibility:**
     - **Private** — only members you add can see it.
     - **Public** — anyone on the internet can view (great for open source; some features differ).
3. Expand **Advanced** to choose:
   - **Version control:** Git (recommended) or TFVC.
   - **Work item process:** Basic, Agile, Scrum, or CMMI (covered next lesson).
4. Click **Create**.

## What's Inside a Project

| Component | Purpose |
| --------- | ------- |
| **Overview** | Summary, README/wiki, dashboards |
| **Boards** | Work items, backlogs, sprints |
| **Repos** | Git repositories |
| **Pipelines** | CI/CD definitions, environments, releases |
| **Test Plans** | Test suites and cases |
| **Artifacts** | Package feeds |
| **Project settings** | Permissions, teams, repos, service connections |

You can **turn services on/off** per project under **Project settings → Overview** (e.g., hide Test Plans if unused).

## Private vs Public Projects

| | Private | Public |
| --- | ------- | ------ |
| Who can view | Only added members | Anyone (anonymous) |
| Best for | Internal/commercial work | Open-source projects |
| Pipeline free minutes | Lower | Higher (more generous) |

## One Project vs Many

Microsoft generally recommends **fewer, larger projects**:

- Easier to share and cross-link work items, repos, and pipelines.
- Simpler administration and reporting.
- Use **teams** to organize people within a single project.

Use **separate projects** when you need strict isolation (different clients, security boundaries, or unrelated products).

## Renaming and Deleting

- You can **rename** a project from **Project settings → Overview** (the URL changes; update bookmarks and remotes).
- **Deleting** a project removes all its data and is recoverable only for a short window — be careful.

## Managing via Azure CLI

```bash
# Create a project
az devops project create \
  --name "eShopOnWeb" \
  --description "Demo e-commerce app" \
  --visibility private \
  --organization https://dev.azure.com/<org>

# List projects
az devops project list --organization https://dev.azure.com/<org>

# Delete a project (by id)
az devops project delete --id <project-id>
```

## Summary

- A project is the main isolation boundary inside an organization.
- It contains Boards, Repos, Pipelines, Test Plans, and Artifacts.
- Choose visibility (private/public), version control, and a process when creating it.
- Prefer fewer, larger projects with teams over many small projects.

## Knowledge Check

1. What four things can you configure when creating a project (incl. Advanced)?
2. When should you use separate projects instead of teams?
3. What is the difference between a private and public project?

➡️ Next: [11 - Process Templates](./11-Process-Templates.md)
