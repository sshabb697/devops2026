# 02 - Deployment Jobs

## Overview

A **deployment job** is a special kind of pipeline job used to deploy to an **environment**. Unlike a regular `job`, a `deployment` job records deployment **history** on the environment, automatically **downloads artifacts**, and supports **deployment strategies** like rolling and canary.

## Regular Job vs Deployment Job

| | `job` | `deployment` |
| --- | ----- | ------------ |
| Purpose | Build/test/general | Deploy to an environment |
| Targets environment | No | Yes |
| Records history | No | Yes (on the environment) |
| Auto-downloads artifacts | No | Yes |
| Supports strategies | No | runOnce, rolling, canary |

## Basic Syntax

```yaml
- stage: Deploy
  jobs:
    - deployment: DeployWeb
      environment: 'production'
      strategy:
        runOnce:
          deploy:
            steps:
              - script: echo "Deploying the app..."
```

Key points:
- `deployment:` names the job.
- `environment:` is **required**.
- `strategy:` defines how the deployment runs.

## Deployment Strategies

### runOnce (simplest)
Runs the lifecycle once.

```yaml
strategy:
  runOnce:
    preDeploy:
      steps: [ ... ]      # optional: setup
    deploy:
      steps: [ ... ]      # the deployment itself
    routeTraffic:
      steps: [ ... ]      # optional: shift traffic
    postRouteTraffic:
      steps: [ ... ]      # optional: validate
    on:
      success:
        steps: [ ... ]    # optional
      failure:
        steps: [ ... ]    # optional: rollback
```

### rolling
Updates targets in **batches** (e.g., 25% at a time) to reduce downtime. Used with VM resources.

```yaml
strategy:
  rolling:
    maxParallel: 2        # how many targets at once
    deploy:
      steps: [ ... ]
```

### canary
Releases to a **small subset** first, observes, then expands. Reduces blast radius of bad releases.

```yaml
strategy:
  canary:
    increments: [10, 50, 100]   # percent rolled out per increment
    deploy:
      steps: [ ... ]
```

## Lifecycle Hooks

Strategies expose **hooks** so you can run steps at each phase:

| Hook | Runs |
| ---- | ---- |
| `preDeploy` | Before deploying |
| `deploy` | The main deployment |
| `routeTraffic` | Shift traffic to the new version |
| `postRouteTraffic` | Validate after routing (smoke tests) |
| `on.success` / `on.failure` | After success/failure (e.g., rollback) |

## Artifacts in Deployment Jobs

Deployment jobs **automatically download** the current run's pipeline artifacts to `$(Pipeline.Workspace)`. Customize or disable with `download`:

```yaml
deploy:
  steps:
    - download: current
      artifact: drop
    - script: ls $(Pipeline.Workspace)/drop
```

## Targeting VM Resources

When an environment has VM resources, a deployment job can run **on each VM** (the agent runs there):

```yaml
- deployment: DeployToVMs
  environment:
    name: 'production'
    resourceType: VirtualMachine
  strategy:
    rolling:
      maxParallel: 1
      deploy:
        steps:
          - script: echo "Deploying on $(Agent.Name)"
```

## Best Practices

- Use **runOnce** for simple deploys; **rolling/canary** for zero-downtime/high-risk.
- Add **smoke tests** in `postRouteTraffic`.
- Implement **rollback** in `on: failure`.
- Keep deploy steps **idempotent** (safe to re-run).

## Summary

- A deployment job deploys to an environment, records history, auto-downloads artifacts, and supports strategies.
- Strategies: **runOnce**, **rolling**, **canary**, each with lifecycle hooks.
- Use hooks for setup, traffic routing, validation, and rollback.

## Knowledge Check

1. Name two things a deployment job does that a regular job doesn't.
2. Which strategy releases to a small subset first?
3. Which hook is ideal for post-deployment smoke tests?

➡️ Next: [03 - Service Connections](./03-Service-Connections.md)
