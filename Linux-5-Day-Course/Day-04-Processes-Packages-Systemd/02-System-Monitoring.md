# 02 — System Monitoring

**Learning objectives**

- Read load, memory, and disk at a glance
- Follow logs with `journalctl` and `tail -f`
- Use a simple “why is it slow?” checklist

---

## CPU & memory at a glance

```bash
top
htop
uptime                # load averages: 1, 5, 15 min
nproc                 # CPU cores
lscpu
free -h               # RAM and swap
```

**Load average** ≈ average runnable processes. Rule of thumb: sustained load **greater than the number of cores** → investigate.

`free -h`: watch **available** (not only “free”). Linux uses idle RAM for cache — that is normal.

---

## Disk usage

```bash
df -h                 # filesystem free space
du -sh /var/log       # directory size
du -h --max-depth=1 ~
```

Full disk (`/` at 100%) breaks apps, logs, and package installs.

---

## Logs

```bash
journalctl -xe                    # recent systemd logs
journalctl -u nginx -f            # follow nginx unit
tail -f /var/log/syslog             # Debian/Ubuntu
tail -n 50 /var/log/auth.log        # SSH / sudo attempts
dmesg | tail                        # kernel messages
```

On some Ubuntu versions, `syslog` is replaced by the journal only — `journalctl` still works.

---

## Useful one-liners

```bash
# Top 5 CPU processes
ps aux --sort=-%cpu | head -6

# Top 5 memory processes
ps aux --sort=-%mem | head -6

# Open files / connections (may need sudo)
sudo lsof -i :80
ss -tulpn | grep LISTEN
```

---

## When something is slow

1. `top` / `htop` — CPU or memory hog?
2. `df -h` — disk full?
3. `journalctl -u <service>` — app errors?
4. `ss -tulpn` — port already in use?

---

## Knowledge check

1. What does `uptime` show besides how long the machine has been on?
2. `df` vs `du`?
3. How do you follow nginx logs live?

<details>
<summary>Answers</summary>

1. Load averages (1, 5, 15 minutes).
2. `df` = free space on filesystems; `du` = size of a directory.
3. `journalctl -u nginx -f` or `tail -f /var/log/nginx/access.log`.

</details>

➡️ Next: [03 — Package Management](./03-Package-Management.md)
