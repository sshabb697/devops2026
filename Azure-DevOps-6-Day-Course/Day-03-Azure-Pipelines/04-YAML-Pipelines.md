# 04 - YAML Pipelines

## Overview

**YAML pipelines** define your CI/CD process as code in a file (conventionally `azure-pipelines.yml`) stored in your repository. This is Microsoft's recommended approach because the pipeline is versioned, reviewable, and reusable — just like your application code.

## Why "Pipeline as Code"?

- **Versioned** — pipeline changes live in Git history alongside the code.
- **Reviewable** — changes go through pull requests.
- **Reproducible** — branching the repo branches the pipeline.
- **Reusable** — share logic via **templates**.
- **Portable** — copy the file to bootstrap new projects.

## A Minimal YAML Pipeline

```yaml
trigger:
  - main

pool:
  vmImage: 'ubuntu-latest'

steps:
  - script: echo "Hello, Azure Pipelines!"
    displayName: 'Say hello'
```

Save this as `azure-pipelines.yml` in the repo root.

## YAML Basics (for those new to YAML)

- **Indentation matters** — use **spaces**, never tabs.
- Key/value pairs: `key: value`.
- Lists use `-`:
  ```yaml
  fruits:
    - apple
    - banana
  ```
- Strings with special characters should be quoted.
- Comments start with `#`.

## Creating a YAML Pipeline in Azure DevOps

1. **Pipelines → New pipeline**.
2. Choose **where your code is** (Azure Repos Git / GitHub).
3. Select your repository.
4. Choose a **starter** template or an existing `azure-pipelines.yml`.
5. Review/edit the YAML in the in-browser editor (with autocomplete & task assistant).
6. **Save and run** — this commits the YAML file to your repo and triggers the first run.

## Key Top-Level Keywords

| Keyword | Purpose |
| ------- | ------- |
| `trigger` | CI branches that start a run |
| `pr` | Branches that trigger PR validation |
| `schedules` | Cron-based runs |
| `pool` | Which agent pool/image to use |
| `variables` | Reusable values |
| `parameters` | Runtime/template inputs |
| `stages` | Top-level phases |
| `jobs` | Units that run on an agent |
| `steps` | Individual actions |
| `resources` | External repos, pipelines, containers |

## Tasks vs Scripts

A **step** is either a built-in **task** or an inline **script**:

```yaml
steps:
  # A task (versioned, with named inputs)
  - task: DotNetCoreCLI@2
    inputs:
      command: 'build'
      projects: '**/*.csproj'

  # A script (runs in the agent's default shell)
  - script: |
      echo "Running tests..."
      dotnet test
    displayName: 'Run tests'

  # OS-specific scripts
  - bash: echo "on Linux/macOS"
  - pwsh: Write-Host "PowerShell Core"
```

## The Task Assistant

In the YAML editor, the **Task Assistant** panel lets you search the task catalog and generate the YAML snippet with the correct inputs — great while learning.

## Validating and Debugging

- Use **Validate** in the editor to catch syntax errors before running.
- Set `system.debug: true` as a variable for verbose logs.
- Check run logs per step to diagnose failures.

## Summary

- YAML pipelines define CI/CD as code in `azure-pipelines.yml`.
- They're versioned, reviewable, reusable, and the recommended approach.
- Steps are **tasks** (pre-built) or **scripts** (inline commands).
- Indentation (spaces) is significant in YAML.

## Knowledge Check

1. Where is a YAML pipeline definition stored?
2. What's the difference between a `task` step and a `script` step?
3. Why must you use spaces (not tabs) in YAML?

➡️ Next: [05 - Pipeline Structure](./05-Pipeline-Structure.md)
