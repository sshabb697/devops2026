# 01 — Linux Fundamentals

**Learning objectives**

- Explain why Linux shows up in cloud, containers, and CI/CD
- Contrast Linux and Windows at a high level
- Define a **distribution** and pick Ubuntu for this course

---

## Why Linux for DevOps?

Linux powers most of the cloud, containers, and CI/CD agents. When you SSH into an Azure VM, run a Docker container, or use a GitHub Actions runner — you are on Linux.

| Area | Why Linux |
| ---- | --------- |
| Cloud (Azure, AWS, GCP) | Most VMs and PaaS run Linux |
| Containers | Docker/Kubernetes images are Linux-based |
| DevOps tools | Jenkins, agents, scripts assume bash |
| Cost | Free, open source, efficient on small VMs |

You can still **write .NET on Windows**. You still need Linux to **deploy, debug, and operate** the servers that run the app.

---

## Linux vs Windows (high level)

| | Linux | Windows |
|--|-------|---------|
| Kernel | Linux kernel | NT kernel |
| CLI | Bash/sh (primary for admins) | PowerShell + CMD |
| File paths | `/home/user/file` | `C:\Users\user\file` |
| Case | `App.conf` and `app.conf` are **different** files | Usually case-insensitive |
| Updates | Often no reboot for patches | Frequent reboots |
| Server share | Dominant in cloud | Common in corporate desktop/AD |

---

## Distributions (distros)

A **distribution** = Linux kernel + package manager + default tools + installer.

| Family | Examples | Package tool | Common in |
| ------ | -------- | ------------ | --------- |
| Debian/Ubuntu | Ubuntu, Debian | `apt` | Cloud VMs, WSL, dev laptops |
| RHEL/CentOS | RHEL, Rocky, Alma | `dnf`/`yum` | Enterprise servers |
| SUSE | openSUSE | `zypper` | Enterprise |
| Arch | Arch, Manjaro | `pacman` | Power users |

**For this course:** use **Ubuntu 22.04 LTS** (WSL or VM). Commands in labs assume `apt` and `systemctl`.

---

## Core concepts to remember

1. **Everything is a file** — configs, devices, even processes (`/proc`).
2. **Multi-user** — many users; permissions matter (Day 3).
3. **CLI-first for admins** — GUI is optional on servers.
4. **Small composable tools** — `ls`, `grep`, `awk` piped together (Day 2).

---

## Knowledge check

1. Why do DevOps engineers need Linux even if they write .NET on Windows?
2. Name two Ubuntu package commands (`apt` family).
3. What is a Linux distribution?

<details>
<summary>Answers</summary>

1. Cloud VMs, containers, and CI agents are usually Linux — you SSH in, read logs, and restart services there.
2. `apt update`, `apt install`, `apt upgrade`, `apt remove` (any two).
3. Kernel + package manager + default tools (Ubuntu, Debian, RHEL, …).

</details>

➡️ Next: [02 — Linux Architecture](./02-Linux-Architecture.md)
