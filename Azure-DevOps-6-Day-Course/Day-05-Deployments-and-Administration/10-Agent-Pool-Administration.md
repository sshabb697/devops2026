# 10 - Agent Pool Administration

## Overview

Building on Day 3's agent concepts, this lesson covers **administering** agent pools: creating them, adding agents, granting access and security, managing capabilities, and controlling parallel jobs at the organization level.

## Organization vs Project Pools

- **Organization-level pools** (Organization settings → Agent pools) are defined once and can be shared with multiple projects.
- **Project-level agent pools** (Project settings → Agent pools) are references that grant a project access to an org pool.

```
Organization
└── Agent pool "linux-builders"  (the real pool)
    ├── shared with → Project A
    └── shared with → Project B
```

## Creating a Pool & Adding Agents

1. **Organization settings → Agent pools → Add pool**.
   - Type: **Self-hosted** or **Azure virtual machine scale set**.
2. Open the pool → **New agent** → follow the OS-specific instructions to download, configure (`config.sh`/`config.cmd`), and register the agent (Day 3, lesson 14).
3. Optionally run the agent **as a service** so it's always available.

## Security & Roles

Set roles on a pool (pool → **Security**):

| Role | Capability |
| ---- | ---------- |
| **Reader** | View the pool |
| **User** | Use the pool in pipelines |
| **Administrator** | Manage agents, security, settings |
| **Creator** (org) | Create new pools |

Grant **project access** so a project can use an org pool (pool → ... → settings, or "Add pool" at the project level).

## Capabilities

Each agent advertises **capabilities**:
- **System capabilities** — auto-detected (OS, installed tools, env vars).
- **User-defined capabilities** — add custom name/value pairs (e.g., `gpu=true`).

Pipelines target agents via **demands** that must match capabilities:

```yaml
pool:
  name: 'linux-builders'
  demands:
    - docker
    - gpu -equals true
```

## Parallel Jobs (Concurrency)

The number of concurrent jobs is governed by **parallel jobs** at **Organization settings → Parallel jobs**:
- **Microsoft-hosted** parallelism (purchased separately).
- **Self-hosted** parallelism (one free; buy more for concurrency).
- More parallel jobs → shorter queues, more simultaneous builds.

## Azure VM Scale Set Agents

For elastic self-hosted capacity, use a **VM Scale Set pool**:
- Azure DevOps scales the number of agent VMs up/down based on demand.
- Combines self-hosted control (custom images, network access) with auto-scaling.
- Configure max/min agents, idle time, and the scale set image.

## Maintenance & Health

- Monitor agent **status** (online/offline) and **jobs** in the pool view.
- Configure **maintenance jobs** to clean stale work directories.
- Keep the agent software **updated** (auto-update is supported for self-hosted).
- Decommission unused agents.

## Best Practices

- Use **org-level pools** shared to projects to avoid duplication.
- Apply **least privilege** with pool roles; limit who can administer.
- Use **demands/capabilities** to route jobs to the right agents.
- Right-size **parallel jobs** to balance cost and queue time.
- Consider **scale set agents** for bursty/self-hosted workloads.
- Restrict pool access for projects running **untrusted** code.

## Summary

- Agent pools are created at the org level and shared to projects.
- Add/register agents, set **roles/security**, and grant **project access**.
- Match jobs to agents with **capabilities/demands**.
- Control concurrency via **parallel jobs**; use **VM Scale Set** pools for auto-scaling.

## Knowledge Check

1. What's the difference between an org-level and project-level pool reference?
2. How do you route a job to an agent that has a GPU?
3. What setting controls how many jobs can run at the same time?

➡️ Next: [11 - Organization Settings](./11-Organization-Settings.md)
