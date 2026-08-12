# 01 — Linux Fundamentals

## Why Linux for DevOps?

Linux powers most of the cloud, containers, and CI/CD agents. When you SSH into an Azure VM, run a Docker container, or use a GitHub Actions runner — you are on Linux.

| Area | Why Linux |
| ---- | --------- |
| Cloud (Azure, AWS, GCP) | Most VMs and PaaS run Linux |
| Containers | Docker/Kubernetes images are Linux-based |
| DevOps tools | Jenkins, agents, scripts assume bash |
| Cost | Free, open source, efficient on small VMs |

---

## Linux vs Windows (high level)

| | Linux | Windows |
|--|-------|---------|
| Kernel | Linux kernel | NT kernel |
| CLI | Bash/sh (primary for admins) | PowerShell + CMD |
| File paths | `/home/user/file` | `C:\Users\user\file` |
| Updates | Often no reboot for patches | Frequent reboots |
| Server share | Dominant in cloud | Common in corporate desktop/AD |

---

## Distributions (distros)

A **distribution** = Linux kernel + package manager + default tools.

| Family | Examples | Package tool | Common in |
| ------ | -------- | ------------ | --------- |
| Debian/Ubuntu | Ubuntu, Debian | `apt` | Cloud VMs, WSL, dev laptops |
| RHEL/CentOS | RHEL, Rocky, Alma | `dnf`/`yum` | Enterprise servers |
| SUSE | openSUSE | `zypper` | Enterprise |
| Arch | Arch, Manjaro | `pacman` | Power users |

**For this course:** use **Ubuntu 22.04 LTS** (WSL or VM).

---

## Core concepts to remember

1. **Everything is a file** — configs, devices, even processes (`/proc`).
2. **Multi-user** — many users; permissions matter.
3. **CLI-first for admins** — GUI is optional on servers.
4. **Small composable tools** — `ls`, `grep`, `awk` piped together.

---

## Knowledge check

1. Why do DevOps engineers need Linux even if they write .NET on Windows?
2. Name two Ubuntu package commands (`apt` family).
3. What is a Linux distribution?

➡️ Next: [02 — Linux Architecture](./02-Linux-Architecture.md)
