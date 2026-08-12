# Lab 05 — Capstone Troubleshooting

**Time:** 90 minutes

Simulate a **junior admin on-call** scenario using everything from Days 1–5.

Write short notes as you go: **symptom → command that proved it → fix**.

---

## Scenario

Your team deployed a small web app on a Linux VM. Users report:

1. Website not loading
2. Internal name `myapp.local` does not resolve
3. Disk alert at 95%
4. Web files have the wrong owner

Work through each issue in order.

---

## Setup

On your VM / WSL:

```bash
sudo apt update
sudo apt install -y nginx
sudo systemctl enable --now nginx
mkdir -p ~/linux-course/capstone
cd ~/linux-course/capstone
```

Confirm baseline:

```bash
curl -I localhost
```

---

## Issue 1 — Website not loading (20 min)

**Investigate:**

```bash
systemctl status nginx --no-pager
curl -I localhost
ss -tulpn | grep :80
sudo journalctl -u nginx -n 20 --no-pager
```

**Break it (practice):**

```bash
sudo systemctl stop nginx
curl -I localhost
```

Expected: connection refused.

**Fix:**

```bash
sudo systemctl start nginx
curl -I localhost
```

Document: What was wrong? What command proved it?

---

## Issue 2 — DNS / connectivity (20 min)

```bash
ping -c 3 8.8.8.8
ping -c 3 example.com
dig example.com +short
cat /etc/resolv.conf
```

If IP ping works and name fails, you have a DNS problem. If both work, continue.

Add a hosts entry for a fake internal name:

```bash
echo "127.0.0.1 myapp.local" | sudo tee -a /etc/hosts
curl -I http://myapp.local
```

Expected: nginx responds for `myapp.local`.

**Backup script (run now — do not wait 5 minutes):**

```bash
cat <<'EOF' > ~/backup.sh
#!/bin/bash
date >> ~/backup.log
curl -sf http://myapp.local > /dev/null || echo FAIL >> ~/backup.log
EOF
chmod +x ~/backup.sh
~/backup.sh
cat ~/backup.log
```

Optional cron (every 5 minutes) — use full path:

```bash
(crontab -l 2>/dev/null; echo "*/5 * * * * $HOME/backup.sh >> $HOME/backup.log 2>&1") | crontab -
crontab -l
```

---

## Issue 3 — Disk space (20 min)

```bash
df -h
dd if=/dev/zero of=~/linux-course/capstone/bigfile bs=1M count=200
df -h ~
du -sh ~/linux-course/capstone/*
```

Expected: `bigfile` is about 200 MB.

**Fix:**

```bash
rm ~/linux-course/capstone/bigfile
df -h ~
```

Optional: `sudo journalctl --vacuum-size=200M`

---

## Issue 4 — Permissions audit (20 min)

```bash
mkdir -p ~/linux-course/capstone/web
echo "hello" > ~/linux-course/capstone/web/index.html
chmod 640 ~/linux-course/capstone/web/index.html
ls -l ~/linux-course/capstone/web/
```

If nginx runs as `www-data`, it usually **cannot** read files under your home directory. That is correct.

Create a proper web root:

```bash
sudo mkdir -p /var/www/capstone
echo "Capstone OK" | sudo tee /var/www/capstone/index.html
sudo chown -R www-data:www-data /var/www/capstone
sudo chmod -R 755 /var/www/capstone
ls -la /var/www/capstone/
```

---

## Final checklist

| Skill | Command / concept used |
| ----- | ---------------------- |
| Service down | `systemctl`, `journalctl` |
| Port listening | `ss`, `curl` |
| DNS | `dig`, `/etc/hosts` |
| Cron | script + optional `crontab` |
| Disk full | `df`, `du`, cleanup |
| Permissions | `chmod`, `chown` |
| SSH (Day 3) | key login to VM (optional) |

---

## Course complete

You finished the **5-day Linux essentials** track.

Keep using the [Command Cheat Sheet](../Command-Cheat-Sheet.md) on the job.

**Next steps:** Azure VM admin (AZ-104), Docker, Ansible, or Linux+ / CKA prep.
