# 04 — Systemd Services

**systemd** is PID 1 on most modern Linux distros. It starts services, mounts disks, and manages targets (like old runlevels).

---

## Essential commands

```bash
systemctl status ssh
systemctl status nginx

sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
sudo systemctl reload nginx

sudo systemctl enable nginx        # start on boot
sudo systemctl disable nginx
sudo systemctl is-enabled nginx
sudo systemctl is-active nginx
```

---

## List units

```bash
systemctl list-units --type=service
systemctl list-units --failed
systemctl list-unit-files | grep enabled
```

---

## Journal (logs)

```bash
journalctl -u nginx
journalctl -u nginx -n 50
journalctl -u nginx -f
journalctl --since "1 hour ago"
```

---

## Simple custom service (awareness)

`/etc/systemd/system/myapp.service`:

```ini
[Unit]
Description=My Demo App
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 /opt/myapp/server.py
Restart=on-failure
User=www-data

[Install]
WantedBy=multi-user.target
```

Enable it:

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now myapp
systemctl status myapp
```

---

## Runlevels → targets (legacy mapping)

| Old runlevel | systemd target |
| ------------ | -------------- |
| multi-user (3) | multi-user.target |
| graphical (5) | graphical.target |
| reboot (6) | reboot.target |

```bash
systemctl get-default
```

➡️ Next: [Lab 04](./Lab-04-Services-Packages.md)
