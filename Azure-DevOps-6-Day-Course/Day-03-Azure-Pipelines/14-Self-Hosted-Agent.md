# 14 - Self-Hosted Agent

## Overview

A **self-hosted agent** is an agent you install and run on your own machine — a physical server, a VM, or a container — and register with an Azure DevOps agent pool. You control the environment, software, and lifecycle. This is the choice when Microsoft-hosted agents don't fit.

## Why Self-Hosted?

- **Custom software** — pre-install exactly the tools/versions you need.
- **More power** — bigger CPU/RAM/disk than hosted agents.
- **Persistence** — caches, dependencies, and Docker layers survive between runs (faster builds).
- **Private network access** — reach internal resources (databases, on-prem servers).
- **Cost control at scale** — heavy build volumes can be cheaper on your own infra.
- **Specialized hardware** — GPUs, specific OS versions, mobile build farms.

## How It Works

```
Your machine (VM / server / container)
   └── Azure Pipelines agent software (registered to a pool)
         ↕  long-poll connection
   Azure DevOps  →  assigns jobs to the agent
```

The agent **polls** Azure DevOps for work — so it only needs **outbound** connectivity (no inbound firewall holes).

## Installing a Self-Hosted Agent (Linux example)

1. **Create/choose a pool:** Organization settings → **Agent pools** → **Add pool** (e.g., `self-hosted-linux`).
2. **Generate a PAT** with **Agent Pools (read, manage)** scope.
3. **Download & configure** on the machine:

```bash
# Create a folder and download the agent (URL from the "New agent" dialog)
mkdir myagent && cd myagent
curl -O https://vstsagentpackage.azureedge.net/agent/<version>/vsts-agent-linux-x64-<version>.tar.gz
tar zxvf vsts-agent-linux-x64-*.tar.gz

# Configure (interactive)
./config.sh
#   Server URL: https://dev.azure.com/<org>
#   Auth type:  PAT  → paste your token
#   Pool:       self-hosted-linux
#   Agent name: <hostname>

# Run interactively...
./run.sh
# ...or install as a service so it runs in the background
sudo ./svc.sh install
sudo ./svc.sh start
```

Windows and macOS use `config.cmd`/`config.sh` with equivalent steps.

## Using the Pool in YAML

```yaml
pool:
  name: 'self-hosted-linux'
  demands:
    - docker            # require an agent that has Docker
```

## Capabilities and Demands

- The agent auto-detects **capabilities** (installed software, env vars).
- You can add **user-defined capabilities** (name/value) in the pool UI.
- Jobs use **demands** to require specific capabilities, ensuring they land on a suitable agent.

## Running Agents in Containers / Scale Sets

- **Docker:** run the agent inside a container for clean, reproducible self-hosted builds.
- **Azure VM Scale Set agents:** Azure DevOps can auto-scale a pool of self-hosted agents on a VM Scale Set — combining self-hosted control with elastic capacity.

## Maintenance Responsibilities

With great control comes maintenance — **you** must:
- Patch the OS and installed tools.
- Keep the agent software updated.
- Clean the work directory/caches periodically.
- Secure the machine (it can access your secrets and networks).

## Microsoft-Hosted vs Self-Hosted (Recap)

| | Microsoft-hosted | Self-hosted |
| --- | ---------------- | ----------- |
| Maintenance | None | You |
| Environment | Fresh each run | Persistent |
| Custom software | Install at runtime | Pre-installed |
| Private network | No | Yes |
| Best for | Standard stacks, getting started | Custom needs, scale, private access |

## Security Considerations

- Self-hosted agents can access your internal network and pipeline secrets — **isolate** them appropriately.
- Be cautious running **public/PR builds** on self-hosted agents (untrusted code on your infra).
- Restrict pool **permissions** and use dedicated, hardened machines.

## Summary

- Self-hosted agents run on your own machines and give full control over the environment.
- Install via `config.sh`/`config.cmd`, register to a pool, optionally run as a service.
- Choose self-hosted for custom software, power, persistence, or private network access.
- You own all maintenance and security.

## Knowledge Check

1. What kind of connectivity does a self-hosted agent require — inbound or outbound?
2. Give two reasons to choose self-hosted over Microsoft-hosted.
3. What is a key security risk of running PR builds on self-hosted agents?

➡️ Next: [15 - Hands-On Lab](./15-Hands-On-Lab.md)
