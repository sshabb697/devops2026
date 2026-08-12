# 02 — System Monitoring

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

**Load average** ≈ average runnable processes. Rule of thumb: sustained load > number of cores → investigate.

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

➡️ Next: [03 — Package Management](./03-Package-Management.md)
