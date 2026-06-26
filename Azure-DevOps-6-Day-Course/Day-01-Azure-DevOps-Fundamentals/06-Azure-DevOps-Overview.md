# 06 - Azure DevOps Overview

## Overview

**Azure DevOps** is Microsoft's cloud-based suite of development tools that supports the entire software lifecycle — planning, source control, CI/CD, testing, and package management. It provides everything a team needs to plan, build, and ship software collaboratively.

## A Brief History

- Originated as **Team Foundation Server (TFS)** — an on-premises product.
- Evolved into **Visual Studio Team Services (VSTS)** in the cloud.
- Rebranded to **Azure DevOps** in 2018, splitting into five independently usable services.

## Two Deployment Options

| Option | Description |
| ------ | ----------- |
| **Azure DevOps Services** | The cloud-hosted SaaS version at `dev.azure.com`. Microsoft manages everything. Recommended for most teams. |
| **Azure DevOps Server** | The on-premises version you host and maintain yourself (formerly TFS). Used when data must stay on-prem. |

This course focuses on **Azure DevOps Services** (cloud).

## The Five Core Services

| Service | What it does |
| ------- | ------------ |
| **Azure Boards** | Agile planning and work tracking (Epics, Stories, Tasks, Kanban, sprints) |
| **Azure Repos** | Unlimited private Git repositories (and TFVC) for source control |
| **Azure Pipelines** | CI/CD for any language, platform, and cloud |
| **Azure Test Plans** | Manual, exploratory, and automated test management |
| **Azure Artifacts** | Hosted package feeds for NuGet, npm, Maven, Python, and more |

You can adopt them all together or pick only the ones you need (e.g., use only Pipelines while keeping code on GitHub).

## Why Choose Azure DevOps?

- **End-to-end** — one platform covers the whole lifecycle.
- **Language/platform agnostic** — works with .NET, Java, Node.js, Python, Go, mobile, containers, etc.
- **Any cloud / any OS** — deploy to Azure, AWS, GCP, on-prem; build on Windows, Linux, macOS agents.
- **Integrations** — connects to GitHub, Slack, Teams, Jira, and thousands of Marketplace extensions.
- **Scales** — from a solo developer to large enterprises.
- **Flexible** — use the whole suite or individual services.

## Pricing at a Glance

- **Free tier:** First 5 users (Basic), unlimited Stakeholders, free private Git repos, limited free pipeline minutes.
- **Paid:** Additional users, parallel pipeline jobs, and Test Plans are billed per user/month.

(See [Access Levels](./13-Access-Levels.md) for details.)

## How You Access It

- **Web portal:** `https://dev.azure.com/<your-organization>`
- **Azure CLI:** the `azure-devops` extension
- **REST APIs:** automate anything programmatically
- **IDE integration:** Visual Studio, VS Code, Eclipse, IntelliJ

## Azure DevOps vs GitHub

Microsoft owns both. They overlap but serve different audiences:

| | Azure DevOps | GitHub |
| --- | ------------ | ------ |
| Focus | Enterprise ALM suite | Developer/open-source collaboration |
| Planning | Azure Boards | GitHub Issues/Projects |
| CI/CD | Azure Pipelines | GitHub Actions |
| Best when | You want an integrated enterprise suite | You want community + code-centric workflow |

They also integrate well together (e.g., Azure Boards + GitHub repos).

## Summary

- Azure DevOps is Microsoft's end-to-end DevOps platform.
- It comes as cloud **Services** or on-prem **Server**.
- It offers five composable services covering the full lifecycle.

## Knowledge Check

1. Name the five core Azure DevOps services.
2. What is the difference between Azure DevOps Services and Azure DevOps Server?
3. Can you use Azure Pipelines without using Azure Repos?

➡️ Next: [07 - Azure DevOps Architecture](./07-Azure-DevOps-Architecture.md)
