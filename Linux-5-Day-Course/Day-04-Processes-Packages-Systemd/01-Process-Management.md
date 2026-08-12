# 01 — Process Management

![Linux process management](../images/linux-process-management.png)

**Learning objectives**

- List processes and find a PID
- Run jobs in the background
- Stop a process with SIGTERM, then SIGKILL only if needed

---

## What is a process?

A **running instance** of a program. Each process has a **PID** (Process ID).

```bash
ps                    # snapshot of your session
ps aux                # all processes (BSD style)
ps -ef                # all processes (SysV style)
top                   # live view (q to quit)
htop                  # friendlier top (install if needed)
```

---

## Key columns in `ps aux`

| Column | Meaning |
| ------ | ------- |
| USER | Who started it |
| PID | Process ID |
| %CPU / %MEM | Resource usage |
| STAT | State (R=running, S=sleep, Z=zombie) |
| COMMAND | Program name |

```bash
ps aux | grep nginx
pgrep -a nginx
```

---

## Foreground vs background

```bash
sleep 300             # blocks terminal
sleep 300 &           # runs in background
echo $!               # PID of last background job
jobs                  # list background jobs
fg %1                 # bring job 1 to foreground
bg %1                 # resume stopped job in background
```

Stop with **Ctrl+Z**, then `bg` or `kill`.

Closing the terminal can kill background jobs. For long work: `nohup cmd &` or a systemd service.

---

## Signals & kill

```bash
kill 1234             # SIGTERM (graceful) — try this first
kill -9 1234          # SIGKILL (force) — last resort
killall nginx
pkill -f "python app"
```

| Signal | Number | Use |
| ------ | ------ | --- |
| SIGTERM | 15 | Ask process to stop (default `kill`) |
| SIGKILL | 9 | Force kill (cannot be ignored; no cleanup) |
| SIGHUP | 1 | Reload config (many daemons) |

Prefer `systemctl stop nginx` for services — it is cleaner than `kill`.

---

## Process tree

```bash
pstree
pstree -p             # show PIDs
systemctl status ssh  # service → main PID
```

Parent **PID 1** on modern Linux is **systemd** (replaces old `init`).

---

## Knowledge check

1. What is a PID?
2. Difference between `kill` and `kill -9`?
3. How do you start a command in the background?

<details>
<summary>Answers</summary>

1. Process ID — unique number for a running program.
2. `kill` = SIGTERM (graceful). `kill -9` = SIGKILL (force, no cleanup).
3. Add `&` at the end, e.g. `sleep 60 &`.

</details>

➡️ Next: [02 — System Monitoring](./02-System-Monitoring.md)
