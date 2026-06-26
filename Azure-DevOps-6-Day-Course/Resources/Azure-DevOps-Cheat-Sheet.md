# Azure DevOps Cheat Sheet

A quick-reference summary of the key concepts, terms, and commands used across the five Azure DevOps services.

---

## The Five Services

| Service | Purpose |
| ------- | ------- |
| **Azure Boards** | Agile planning: work items, backlogs, sprints, Kanban, dashboards |
| **Azure Repos** | Git (and TFVC) source control hosting |
| **Azure Pipelines** | CI/CD build and release automation |
| **Azure Test Plans** | Manual and exploratory testing |
| **Azure Artifacts** | Package feeds (NuGet, npm, Maven, Python, Universal) |

---

## Hierarchy

```
Organization (dev.azure.com/<org>)
└── Project
    ├── Boards (work items)
    ├── Repos  (Git repositories)
    ├── Pipelines (build & release)
    ├── Test Plans
    └── Artifacts (feeds)
```

---

## Work Item Hierarchy (Agile process)

```
Epic
└── Feature
    └── User Story
        ├── Task
        └── Bug
```

---

## Access Levels

| Level | Cost | Capability |
| ----- | ---- | ---------- |
| **Stakeholder** | Free | View/edit work items, limited Boards & Pipelines |
| **Basic** | Free for first 5 users | Full access except Test Plans |
| **Basic + Test Plans** | Paid | Everything including Test Plans |

---

## Pipeline YAML Quick Reference

```yaml
trigger:
  - main

pool:
  vmImage: 'ubuntu-latest'

variables:
  buildConfiguration: 'Release'

stages:
  - stage: Build
    jobs:
      - job: BuildJob
        steps:
          - script: echo "Building..."
            displayName: 'Build step'
```

Key keywords:

| Keyword | Meaning |
| ------- | ------- |
| `trigger` | Branches that start a CI run |
| `pr` | Branches that trigger on pull request |
| `pool` | Agent pool / image to run on |
| `stages` | Top-level phases (Build, Test, Deploy) |
| `jobs` | Units that run on a single agent |
| `steps` | Individual tasks/scripts within a job |
| `variables` | Reusable values |
| `template` | Reusable YAML file |

---

## Azure CLI (DevOps extension)

```bash
# Install the DevOps extension
az extension add --name azure-devops

# Sign in / set defaults
az devops login
az devops configure --defaults organization=https://dev.azure.com/<org> project=<project>

# Projects
az devops project list
az devops project create --name "MyProject"

# Repos
az repos list
az repos create --name "MyRepo"

# Pipelines
az pipelines list
az pipelines run --name "MyPipeline"

# Boards work items
az boards work-item create --title "Fix login bug" --type "Bug"
```

---

## Branch Policy Checklist

- [ ] Require a minimum number of reviewers
- [ ] Check for linked work items
- [ ] Check for comment resolution
- [ ] Limit merge types (squash, rebase, etc.)
- [ ] Build validation (must pass pipeline)
- [ ] Automatically included reviewers

---

## Common Predefined Pipeline Variables

| Variable | Description |
| -------- | ----------- |
| `Build.BuildId` | Unique numeric build ID |
| `Build.SourceBranch` | Triggering branch ref |
| `Build.SourceVersion` | Commit SHA |
| `Build.ArtifactStagingDirectory` | Path to stage artifacts |
| `Agent.OS` | OS of the agent |
| `System.DefaultWorkingDirectory` | Default working directory |

---

## Useful Keyboard / Portal Tips

- Press `?` in the Azure DevOps web UI to see keyboard shortcuts.
- Use the global search bar to find code, work items, and wiki pages.
- Pin frequently used queries and dashboards to your project home.

See the [Git Cheat Sheet](./Git-Cheat-Sheet.md) for source-control commands.
