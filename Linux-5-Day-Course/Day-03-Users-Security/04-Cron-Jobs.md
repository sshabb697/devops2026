# 04 — Cron Jobs

Schedule commands to run automatically.

---

## crontab format

```
* * * * *  command
│ │ │ │ │
│ │ │ │ └── day of week (0-7, Sun=0)
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

Remove: `crontab -e` and delete the line.

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

➡️ Next: [Lab 03](./Lab-03-Permissions-SSH.md)
