# 04 — Cron Jobs

Schedule commands to run automatically.

**Learning objectives**

- Read a five-field crontab line
- Add a user cron job
- Know why cron jobs “work in the terminal but fail in cron”

---

## crontab format

```
* * * * *  command
│ │ │ │ │
│ │ │ │ └── day of week (0-7, Sun=0 or 7)
│ │ │ └──── month (1-12)
│ │ └────── day of month (1-31)
│ └──────── hour (0-23)
└────────── minute (0-59)
```

Examples:

```bash
0 2 * * *   /home/user/backup.sh      # daily 2:00 AM
*/5 * * * * /home/user/healthcheck.sh # every 5 minutes
0 0 * * 0   /home/user/weekly.sh      # Sunday midnight
```

---

## User crontab

```bash
crontab -l              # list
crontab -e              # edit (opens vi/nano)
```

Add line:

```
*/2 * * * * date >> ~/cron-test.log
```

Wait 2 minutes, then:

```bash
cat ~/cron-test.log
```

Remove: `crontab -e` and delete the line, or `crontab -r` (deletes **all** your cron jobs).

---

## Why cron jobs fail (gotchas)

Cron does **not** load your interactive `.bashrc`. `$PATH` is short.

| Problem | Fix |
| ------- | --- |
| `command not found` | Use full paths (`/usr/bin/date`, `/home/you/backup.sh`) |
| Script not executable | `chmod +x backup.sh` |
| No output | Redirect: `>> ~/cron.log 2>&1` |
| Wrong user | Root cron vs user cron are different |

```
*/5 * * * * /home/you/backup.sh >> /home/you/backup.log 2>&1
```

---

## System cron

```bash
ls /etc/cron.d/
ls /etc/cron.daily/
cat /etc/crontab
```

---

## Modern alternative: systemd timers

Used on many servers (Day 4). Cron is still everywhere — know both.

---

## Knowledge check

1. What does `0 2 * * *` mean?
2. Why use full paths in cron?
3. How do you list your jobs?

<details>
<summary>Answers</summary>

1. 02:00 every day.
2. Cron’s `PATH` is minimal — `backup.sh` may not be found.
3. `crontab -l`

</details>

➡️ Next: [Lab 03](./Lab-03-Permissions-SSH.md)
