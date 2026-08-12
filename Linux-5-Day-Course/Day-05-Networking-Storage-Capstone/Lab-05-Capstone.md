# Lab 05 — Capstone Troubleshooting

**Time:** 90 minutes

Simulate a **junior admin on-call** scenario using everything from Days 1–5.

---

## Scenario

Your team deployed a small web app on a Linux VM. Users report:

1. Website not loading
2. SSH works from office but a cron backup failed
3. Disk alert at 95%

Work through each issue in order.

---

## Setup (instructor or self)

On your VM / WSL:

```bash
sudo apt update
sudo apt install -y nginx
sudo systemctl enable --now nginx
mkdir -p ~/linux-course/capstone
cd ~/linux-course/capstone
```

---

## Issue 1 — Website not loading (25 min)

**Investigate:**

```bash
systemctl status nginx
curl -I localhost
ss -tulpn | grep :80
sudo journalctl -u nginx -n 20
```

**Break it (practice):**

```bash
sudo systemctl stop nginx
curl -I localhost
```

**Fix:**

```bash
sudo systemctl start nginx
curl -I localhost
```

Document: What was wrong? What command proved it?

---

## Issue 2 — DNS / connectivity (25 min)

```bash
ping -c 3 8.8.8.8
ping -c 3 github.com
dig github.com +short
cat /etc/resolv.conf
```

Add a hosts entry for a fake internal name:

```bash
echo "127.0.0.1 myapp.local" | sudo tee -a /etc/hosts
curl -I http://myapp.local
```

**Cron check** — backup script every 5 min:

```bash
echo '#!/bin/bash' > ~/backup.sh
echo 'date >> ~/backup.log' >> ~/backup.sh
echo 'curl -sf http://myapp.local > /dev/null || echo FAIL >> ~/backup.log' >> ~/backup.sh
chmod +x ~/backup.sh
(crontab -l 2>/dev/null; echo "*/5 * * * * $HOME/backup.sh") | crontab -
sleep 330
cat ~/backup.log
```

---

## Issue 3 — Disk space (20 min)

```bash
df -h
dd if=/dev/zero of=~/linux-course/capstone/bigfile bs=1M count=200
df -h ~
du -sh ~/linux-course/capstone/*
```

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

If nginx runs as `www-data`, would it read your home file? (Usually no — good.)

Create proper shared config:

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
| Cron | `crontab -e`, log file |
| Disk full | `df`, `du`, cleanup |
| Permissions | `chmod`, `chown` |
| SSH (Day 3) | key login to VM |

---

## Course complete

You finished the **5-day Linux essentials** track.

**Next steps:** Azure VM admin (AZ-104), Docker, Ansible, or CKA/Linux+ certification prep.
