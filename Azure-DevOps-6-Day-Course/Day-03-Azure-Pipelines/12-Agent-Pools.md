# 12 - Agent Pools

## Overview

A pipeline job has to run *somewhere*. That "somewhere" is an **agent** — a piece of software running on a machine that executes your jobs. Agents are organized into **agent pools**. This lesson explains agents, pools, and how jobs get assigned to them.

## What is an Agent?

An **agent** is the compute that runs a pipeline **job**. It:
- Checks out your code.
- Runs the job's steps (tasks/scripts).
- Reports logs and results back to Azure DevOps.

One agent runs **one job at a time**.

## What is an Agent Pool?

An **agent pool** is a collection of agents. When a job needs to run, Azure Pipelines picks an available agent from the specified pool.

```
Agent Pool: "ubuntu-builders"
   ├── Agent 1  (busy)
   ├── Agent 2  (idle)  ◄── new job assigned here
   └── Agent 3  (idle)
```

Pools are shared across projects in an organization (you grant project access).

## Two Categories of Agents

| | Microsoft-hosted | Self-hosted |
| --- | ---------------- | ----------- |
| Who manages | Microsoft | You |
| Where | Microsoft's cloud | Your machines/VMs/containers |
| Setup | None | Install & register the agent |
| Maintenance | None (fresh VM each run) | You patch/maintain |
| Cost model | Parallel jobs / minutes | Your infra + 1 free parallel job |
| Customization | Limited to provided images | Full control |

Lessons 13 and 14 cover each in depth.

## Selecting a Pool in YAML

```yaml
# Microsoft-hosted (by image)
pool:
  vmImage: 'ubuntu-latest'

# A specific named pool (often self-hosted)
pool:
  name: 'ubuntu-builders'

# Target specific agents by capability/demand
pool:
  name: 'ubuntu-builders'
  demands:
    - docker
    - Agent.OS -equals Linux
```

## Parallel Jobs (Concurrency)

The number of jobs you can run **simultaneously** is governed by **parallel jobs** you've purchased/been granted:

- More parallel jobs → more concurrent builds → shorter queues.
- Configured under **Organization settings → Parallel jobs**.
- Microsoft-hosted and self-hosted parallelism are tracked/purchased separately.

## Capabilities and Demands

- Each agent advertises **capabilities** (installed software, OS, env vars).
- A job can specify **demands** — required capabilities.
- Azure Pipelines matches demands to agent capabilities to pick a suitable agent.

## Pool Administration (preview)

At **Organization settings → Agent pools** you can:
- Create pools and add agents.
- Grant **security** (who can use/manage a pool).
- Set **project access** (which projects can use the pool).
- View agent health and jobs.

(More on administration on Day 5.)

## Choosing Between Hosted and Self-Hosted

Use **Microsoft-hosted** when:
- You want zero maintenance and clean, fresh environments.
- Your tools are available in the standard images.

Use **self-hosted** when:
- You need custom software, more power, or longer-running caches.
- You must access private networks/resources.
- You want to control costs at scale.

## Summary

- An **agent** runs one job; an **agent pool** is a group of agents.
- Agents are **Microsoft-hosted** (managed by Microsoft) or **self-hosted** (managed by you).
- Select a pool with `pool: { vmImage }` or `pool: { name, demands }`.
- **Parallel jobs** control how many jobs run at once.

## Knowledge Check

1. How many jobs can a single agent run at the same time?
2. What's the difference between a Microsoft-hosted and a self-hosted agent?
3. What are "demands" used for?

➡️ Next: [13 - Microsoft-Hosted Agent](./13-Microsoft-Hosted-Agent.md)
