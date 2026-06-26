# 05 - Pipeline Structure

## Overview

Every YAML pipeline is built from a clear hierarchy. Understanding **stages → jobs → steps** (and how agents fit in) lets you design pipelines that are organized, parallelizable, and easy to maintain.

## The Hierarchy

```
Pipeline
└── Stage(s)            major phases: Build, Test, DeployDev, DeployProd
    └── Job(s)          run on a single agent; can run in parallel
        └── Step(s)     tasks or scripts, run sequentially on the agent
```

### Stages
A **stage** is a logical boundary, often mapping to a phase like Build or a deployment environment. Stages run **sequentially** by default; you can control order with `dependsOn` and run them in parallel or conditionally.

### Jobs
A **job** runs on a single **agent** and is the unit of parallelism. Jobs within a stage can run in parallel (or in order via `dependsOn`). Each job starts on a fresh agent workspace.

Two job types:
- **Standard job** (`job`) — general build/test work.
- **Deployment job** (`deployment`) — targets an **environment**, tracks deployment history, and supports strategies (covered Day 5).

### Steps
A **step** is the smallest unit — a **task** or a **script**. Steps in a job run **sequentially** on the same agent.

## A Full Multi-Stage Example

```yaml
trigger:
  - main

variables:
  buildConfiguration: 'Release'

stages:
  - stage: Build
    displayName: 'Build & Test'
    jobs:
      - job: BuildJob
        pool:
          vmImage: 'ubuntu-latest'
        steps:
          - script: echo "Restoring..."
            displayName: 'Restore'
          - script: echo "Building in $(buildConfiguration)"
            displayName: 'Build'
          - script: echo "Testing..."
            displayName: 'Test'

  - stage: DeployDev
    displayName: 'Deploy to Dev'
    dependsOn: Build
    condition: succeeded()
    jobs:
      - deployment: DeployWeb
        environment: 'dev'
        strategy:
          runOnce:
            deploy:
              steps:
                - script: echo "Deploying to Dev..."
```

## Controlling Flow

### `dependsOn`
Defines order and lets you fan-out/fan-in:

```yaml
stages:
  - stage: A
  - stage: B
    dependsOn: A
  - stage: C
    dependsOn: A        # B and C both depend on A → run in parallel after A
```

### `condition`
Run a stage/job/step only when a condition is met:

```yaml
condition: succeeded()                                   # default
condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
```

### Matrix / parallel jobs
Run the same job across multiple configurations:

```yaml
jobs:
  - job: Test
    strategy:
      matrix:
        linux:
          imageName: 'ubuntu-latest'
        windows:
          imageName: 'windows-latest'
    pool:
      vmImage: $(imageName)
    steps:
      - script: echo "Testing on $(imageName)"
```

## Where `pool` Goes

`pool` can be set at the pipeline, stage, or job level. The most specific wins. Each **job** ultimately runs on one agent from that pool.

## Visualizing Structure

```
Build (stage)
  └── BuildJob (job, agent #1)
        ├── Restore (step)
        ├── Build   (step)
        └── Test    (step)
DeployDev (stage, depends on Build)
  └── DeployWeb (deployment job, agent #2)
        └── deploy steps
```

## Summary

- Pipelines are **Stages → Jobs → Steps**.
- Stages and steps run sequentially by default; jobs are the unit of parallelism.
- Use `dependsOn` for ordering, `condition` for conditional execution, and `strategy: matrix` for parallel configs.
- Each job runs on one agent from a `pool`.

## Knowledge Check

1. Which level is the unit of parallelism — stage, job, or step?
2. How do you make a stage run only after another succeeds?
3. What's the difference between a `job` and a `deployment` job?

➡️ Next: [06 - Build Pipeline](./06-Build-Pipeline.md)
