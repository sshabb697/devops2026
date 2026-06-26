# 11 - Artifacts

## Overview

The word "artifacts" means two related things in Azure DevOps:

1. **Pipeline artifacts** — files produced by a build (binaries, packages, reports) that are published and shared between stages or kept for download.
2. **Azure Artifacts** — a service hosting **package feeds** (NuGet, npm, Maven, Python, Universal).

This lesson covers both.

---

## Part 1: Pipeline Artifacts

### Why publish artifacts?
- **Build once, deploy many** — produce the deployable once and reuse it in every deployment stage.
- **Traceability** — each run keeps its artifacts for download/audit.
- **Decoupling** — separate the build stage from deployment stages.

### Publishing an artifact

Modern (recommended) task:

```yaml
steps:
  - task: PublishPipelineArtifact@1
    inputs:
      targetPath: '$(Build.ArtifactStagingDirectory)'
      artifact: 'drop'
```

Older task (still common):

```yaml
  - task: PublishBuildArtifacts@1
    inputs:
      PathtoPublish: '$(Build.ArtifactStagingDirectory)'
      ArtifactName: 'drop'
```

### Consuming an artifact in a later stage

```yaml
- stage: Deploy
  dependsOn: Build
  jobs:
    - deployment: Deploy
      environment: 'dev'
      strategy:
        runOnce:
          deploy:
            steps:
              - download: current        # downloads artifacts from this run
                artifact: drop
              - script: ls $(Pipeline.Workspace)/drop
```

> In **deployment jobs**, artifacts are downloaded **automatically** by default; `download` lets you customize or disable it.

---

## Part 2: Azure Artifacts (Package Feeds)

### What it is
A hosted, private (or public) **feed** that stores and shares packages across your organization.

Supported package types:
- **NuGet** (.NET)
- **npm** (Node.js)
- **Maven** (Java)
- **Python (PyPI)**
- **Cargo** (Rust)
- **Universal Packages** (any files)

### Creating a feed
1. **Artifacts → + Create Feed**.
2. Name it and choose visibility/scope (project or organization).
3. Configure **upstream sources** to proxy public registries (e.g., nuget.org, npmjs).

### Publishing & consuming in a pipeline (npm example)

```yaml
steps:
  - task: npmAuthenticate@0
    inputs:
      workingFile: .npmrc

  - script: npm publish
    displayName: 'Publish package to feed'
```

NuGet example:

```yaml
  - task: NuGetCommand@2
    inputs:
      command: 'push'
      packagesToPush: '$(Build.ArtifactStagingDirectory)/*.nupkg'
      publishVstsFeed: 'MyProject/MyFeed'
```

### Feed views
Feeds support views to promote quality:

| View | Meaning |
| ---- | ------- |
| `@local` | All packages in the feed |
| `@prerelease` | Promoted, pre-release quality |
| `@release` | Promoted, release quality |

### Upstream sources
A feed can proxy public registries, so consumers get both internal and public packages from a single URL — with caching and an audit trail.

---

## Pipeline Artifacts vs Azure Artifacts

| | Pipeline artifacts | Azure Artifacts |
| --- | ------------------ | --------------- |
| Stores | Build outputs per run | Versioned packages |
| Used for | Passing files between stages / downloads | Sharing libraries/dependencies |
| Lifetime | Tied to the run (retention policy) | Long-lived, versioned |

## Summary

- **Pipeline artifacts** carry build outputs between stages (publish with `PublishPipelineArtifact@1`, consume with `download`).
- **Azure Artifacts** hosts package feeds (NuGet, npm, Maven, Python, Universal) with views and upstream sources.
- Deployment jobs auto-download pipeline artifacts.

## Knowledge Check

1. Which task is the recommended way to publish pipeline artifacts?
2. In a deployment job, do you need to manually download artifacts?
3. What is an upstream source in an Azure Artifacts feed?

➡️ Next: [12 - Agent Pools](./12-Agent-Pools.md)
