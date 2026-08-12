# 05 — Filesystem Hierarchy (FHS)

Linux stores everything under **/** (root). There are no `C:` and `D:` drives — one tree.

![Linux FHS tree](../images/linux-fhs-tree.png)

**Learning objectives**

- Name the directories you use every day as an admin
- Know where **config**, **logs**, and **home files** live

---

## Directories you use daily

| Path | Purpose | DevOps example |
| ---- | ------- | -------------- |
| `/` | Root of filesystem | — |
| `/home/<user>` | User home directories | Your code, SSH keys |
| `/root` | root user home | Admin-only |
| `/etc` | Configuration files | `nginx.conf`, `ssh/sshd_config` |
| `/var` | Variable data (logs, cache) | `/var/log`, web roots |
| `/var/log` | Log files | `syslog`, `auth.log` |
| `/tmp` | Temporary files | Often cleared on reboot |
| `/usr` | User programs & libraries | `/usr/bin`, `/usr/local` |
| `/opt` | Optional third-party apps | Commercial software |
| `/bin`, `/sbin` | Essential binaries | `ls`, `systemctl` |
| `/dev` | Device files | Disks, null device |
| `/proc` | Process/kernel info (virtual) | `cat /proc/cpuinfo` |
| `/sys` | Hardware/kernel info (virtual) | — |

On modern Ubuntu, `/bin` is often a **symlink** to `/usr/bin`. Same commands — do not panic.

---

## Explore on your machine

```bash
ls /
ls /etc | head
ls /var/log
ls -la ~
echo $HOME
```

`$HOME` is the same as `~` — usually `/home/<your-username>`.

---

## Config vs data vs logs (pattern)

```
/etc/myapp/config.yml     ← static configuration
/var/lib/myapp/           ← application data
/var/log/myapp/           ← logs
/tmp/                     ← short-lived temp
```

When troubleshooting: **config** in `/etc`, **errors** in `/var/log`.

---

## Knowledge check

1. Where are system logs usually stored?
2. Where is your home directory?
3. What lives under `/etc`?

<details>
<summary>Answers</summary>

1. `/var/log` (and `journalctl` for systemd).
2. `/home/<username>` (`echo $HOME`).
3. Configuration files (`sshd_config`, nginx, apt sources, …).

</details>

➡️ Next: [Lab 01 — Shell Navigation](./Lab-01-Shell-Navigation.md)
