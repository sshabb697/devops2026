# 13 - Microsoft-Hosted Agent

## Overview

**Microsoft-hosted agents** are agents fully managed by Microsoft in the cloud. Each time you run a job, you get a **fresh virtual machine** with a wide range of pre-installed tools. You don't install, patch, or maintain anything — it's the easiest way to get started.

## Key Characteristics

- **Fully managed** — Microsoft provisions, patches, and retires the VMs.
- **Clean each run** — every job gets a brand-new, isolated VM, then it's discarded.
- **Pre-loaded** — common SDKs, runtimes, and tools come pre-installed.
- **No maintenance** — you focus on your pipeline, not infrastructure.

## Available Images

Specify an image via `vmImage`:

| `vmImage` | OS |
| --------- | -- |
| `ubuntu-latest` | Latest Ubuntu LTS (Linux) |
| `windows-latest` | Latest Windows Server |
| `macOS-latest` | Latest macOS |

Versioned images are also available (e.g., `ubuntu-22.04`, `windows-2022`, `macOS-14`).

```yaml
pool:
  vmImage: 'ubuntu-latest'
```

## What's Pre-Installed?

The images include a large software inventory: .NET, Node.js, Python, Java JDKs, Go, Docker, Git, Azure CLI, browsers, build tools, and more. The exact contents are published per image (see the [runner-images repository](https://github.com/actions/runner-images), which Azure shares with GitHub Actions).

If a tool version you need isn't present, install it as a step (e.g., `UseDotNet@2`, `NodeTool@0`, `UsePythonVersion@0`).

## Benefits

- ✅ Zero setup — start building immediately.
- ✅ Always patched and secure.
- ✅ Clean, reproducible environment every run.
- ✅ Multiple OS options.

## Limitations

- ⏱️ **Time limit** per job (e.g., 60 minutes on private projects' free tier; longer with paid parallelism).
- 💾 **No persistence** between runs — caches must be re-fetched (use the Cache task).
- 🔒 **No access** to your private networks by default.
- 🧰 **Fixed software set** — you can't pre-bake custom images (install at runtime instead).
- 📈 **Limited resources** (CPU/RAM/disk) compared to a beefy self-hosted machine.

## Speeding Up Hosted Builds

Because the VM is fresh each time, use **caching** to avoid re-downloading dependencies:

```yaml
steps:
  - task: Cache@2
    inputs:
      key: 'npm | "$(Agent.OS)" | package-lock.json'
      path: '$(Pipeline.Workspace)/.npm'
  - script: npm ci
```

## Free Tier Notes

- Public projects get generous free parallel jobs/minutes.
- Private projects get limited free minutes; buy parallel jobs to scale.
- Check **Organization settings → Parallel jobs** for your current grant.

## When to Use Microsoft-Hosted

- Getting started / learning.
- Standard tech stacks supported by the images.
- Teams that don't want to manage infrastructure.
- Open-source projects (generous free tier).

## Summary

- Microsoft-hosted agents are managed VMs with pre-installed tools, fresh each run.
- Choose an OS with `vmImage` (`ubuntu-latest`, `windows-latest`, `macOS-latest`).
- Zero maintenance, but time-limited, non-persistent, and no private network access.
- Use the **Cache** task to speed up dependency-heavy builds.

## Knowledge Check

1. What happens to a Microsoft-hosted VM after a job finishes?
2. How do you select Windows vs Linux for a hosted agent?
3. Name one limitation of Microsoft-hosted agents and a way to mitigate it.

➡️ Next: [14 - Self-Hosted Agent](./14-Self-Hosted-Agent.md)
