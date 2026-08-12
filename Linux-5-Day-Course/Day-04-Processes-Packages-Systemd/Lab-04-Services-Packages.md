# Lab 04 — Services & Packages

**Time:** 60 minutes

---

## Part A — Process detective (15 min)

```bash
# Start a background process
sleep 600 &
echo $! > /tmp/lab_pid.txt
cat /tmp/lab_pid.txt

ps aux | grep sleep
kill $(cat /tmp/lab_pid.txt)
ps aux | grep sleep
```

Find top CPU process:

```bash
ps aux --sort=-%cpu | head -6
```

---

## Part B — Install and run nginx (30 min)

```bash
sudo apt update
sudo apt install -y nginx
systemctl status nginx
curl -I localhost
```

If status is not active:

```bash
sudo journalctl -u nginx -n 30
sudo ss -tulpn | grep :80
```

Practice service control:

```bash
sudo systemctl stop nginx
curl -I localhost                    # should fail
sudo systemctl start nginx
sudo systemctl enable nginx
systemctl is-enabled nginx
```

---

## Part C — Monitoring drill (15 min)

```bash
df -h
free -h
uptime
journalctl -xe | tail -20
```

Simulate log follow (open second terminal optional):

```bash
sudo tail -f /var/log/nginx/access.log
# in another terminal: curl localhost
```

---

## Deliverables

- [ ] Killed a process by PID
- [ ] Installed nginx with apt
- [ ] Started/stopped/enabled nginx with systemctl
- [ ] Read logs with journalctl
- [ ] Checked disk and memory

➡️ **Day 5:** [Networking & Storage](../Day-05-Networking-Storage-Capstone/README.md)
