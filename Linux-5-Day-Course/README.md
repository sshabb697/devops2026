# Linux 5-Day Course

Hands-on Linux fundamentals for **DevOps, cloud, and sysadmin** work.

> Focus: **commands you use every day** on servers, VMs, containers, and CI/CD agents — not exam memorization.

Print or keep open: **[Command Cheat Sheet](./Command-Cheat-Sheet.md)**

---

## What you will be able to do

By the end of the week you can:

1. Navigate a Linux filesystem and edit files on a server with no GUI.
2. Find logs, filter errors, and chain commands with pipes.
3. Lock down files, create users, and log in with SSH keys.
4. Install packages, manage systemd services, and stop a runaway process.
5. Diagnose “site is down,” DNS failures, and a full disk.

| Day | Topic | Outcome |
| --- | ----- | ------- |
| [Day 1](./Day-01-Getting-Started/) | Fundamentals, setup, shell, FHS | Navigate Linux confidently |
| [Day 2](./Day-02-Files-and-Shell/) | Files, vi, search, I/O redirection | Manage files like an admin |
| [Day 3](./Day-03-Users-Security/) | Users, permissions, SSH, cron | Secure a Linux server |
| [Day 4](./Day-04-Processes-Packages-Systemd/) | Processes, packages, systemd | Run and manage services |
| [Day 5](./Day-05-Networking-Storage-Capstone/) | Network, storage, troubleshooting | Fix real server issues |

---

## Prerequisites

- A computer with **Windows, macOS, or Linux**
- Install **one** of:
  - **WSL2** (Windows) — recommended
  - **Ubuntu VM** (VirtualBox / Hyper-V)
  - Native Linux laptop
- No prior Linux experience required
- Use **Ubuntu 22.04 LTS** so commands match the labs

---

## How to study

1. Read the **lessons** for the day (concepts + diagrams).
2. Run every **command** in your terminal — do not just read.
3. Complete the **hands-on lab** at the end of each day.
4. Use the **cheat sheet** when you forget a flag.

Each day is designed for **5–6 hours** (mix of reading and labs).

**If a command fails:** read the error, check you are in the right directory (`pwd`), and whether you need `sudo`.

---

## Course layout

```
Linux-5-Day-Course/
├── README.md
├── Command-Cheat-Sheet.md
├── images/
├── Day-01-Getting-Started/
├── Day-02-Files-and-Shell/
├── Day-03-Users-Security/
├── Day-04-Processes-Packages-Systemd/
└── Day-05-Networking-Storage-Capstone/
```

---

## Connects to other courses in this repo

| After Linux… | Continue with… |
| ------------ | -------------- |
| Comfortable on CLI | [Azure DevOps 6-Day Course](../Azure-DevOps-6-Day-Course/) |
| Need cloud basics | [AZ-104 Azure Administrator](../AZ-104-Azure-Administrator/) |
| Deploy .NET apps | [.NET Deployment Workshop](../Azure-DevOps-6-Day-Course/DotNet-Deployment-Workshop/) |

---

## Course images

| Image | Used in |
| ----- | ------- |
| `images/linux-architecture-layers.png` | Day 1 — architecture |
| `images/linux-fhs-tree.png` | Day 1 — filesystem hierarchy |
| `images/linux-path-lookup.png` | Day 1 — how commands are found |
| `images/linux-wildcards.png` | Day 2 — globs (`*`, `?`) |
| `images/linux-find-tree.png` | Day 2 — find |
| `images/linux-hard-vs-symlink.png` | Day 2 — hard vs symbolic links |
| `images/linux-du-vs-df.png` | Day 2 — du vs df |
| `images/linux-file-types-lsl.png` | Day 2 — `ls -l` file types |
| `images/linux-vi-modes.png` | Day 2 — vi modes |
| `images/linux-tar-archive.png` | Day 2 — tar.gz |
| `images/linux-grep-filter.png` | Day 2 — grep |
| `images/linux-pipes-redirection.png` | Day 2 — pipes and redirection |
| `images/linux-file-permissions-rwx.png` | Day 3 — permissions |
| `images/linux-ssh-keys.png` | Day 3 — SSH keys |
| `images/linux-process-management.png` | Day 4 — processes |
| `images/linux-networking-basics.png` | Day 5 — networking |
| `images/linux-troubleshooting-flow.png` | Day 5 — diagnosis flow |
