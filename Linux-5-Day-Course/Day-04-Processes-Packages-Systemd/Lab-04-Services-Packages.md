# Lab 04 — Services & Packages

**Time:** 60 minutes

WSL note: nginx usually works. If `systemctl` is limited, use `sudo service nginx start` or a full VM.

---

## Part A — Process detective (15 min)

```bash
sleep 600 &
echo $! > /tmp/lab_pid.txt
cat /tmp/lab_pid.txt

ps aux | grep sleep
kill "$(cat /tmp/lab_pid.txt)"
ps aux | grep sleep
```

Expected: after `kill`, that PID is gone (grep may only show the grep line itself).

Find top CPU process:

```bash
ps aux --sort=-%cpu | head -6
```

---

## Part B — Install and run nginx (30 min)

```bash
sudo apt update
sudo apt install -y nginx
systemctl status nginx --no-pager
curl -I localhost
```

Expected: HTTP `200` or `301`/`302` from nginx.

If status is not active:

```bash
sudo journalctl -u nginx -n 30 --no-pager
sudo ss -tulpn | grep :80
```

Practice service control:

```bash
sudo systemctl stop nginx
curl -I localhost                    # should fail (connection refused)
sudo systemctl start nginx
sudo systemctl enable nginx
systemctl is-enabled nginx
```

Expected after stop: `curl` fails. After start: `curl` works. `is-enabled` → `enabled`.

---

## Part C — Monitoring drill (15 min)

```bash
df -h
free -h
uptime
journalctl -xe --no-pager | tail -20
```

Optional second terminal:

```bash
sudo tail -f /var/log/nginx/access.log
# in another terminal: curl localhost
```

You should see a new access line.

---

## Deliverables

- [ ] Killed a process by PID
- [ ] Installed nginx with apt
- [ ] Started/stopped/enabled nginx with systemctl
- [ ] Read logs with journalctl
- [ ] Checked disk and memory

➡️ **Day 5:** [Networking & Storage](../Day-05-Networking-Storage-Capstone/README.md)
