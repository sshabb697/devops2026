# 04 — Systemd Services

**systemd** is PID 1 on most modern Linux distros. It starts services, mounts disks, and manages targets (like old runlevels).

**Learning objectives**

- Start, stop, restart, enable a service
- Read unit logs with `journalctl`
- Contrast `restart` vs `reload`

---

## Essential commands

```bash
systemctl status ssh
systemctl status nginx

sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx      # stop + start (brief downtime)
sudo systemctl reload nginx       # reread config if supported

sudo systemctl enable nginx        # start on boot
sudo systemctl disable nginx
sudo systemctl enable --now nginx  # enable + start in one step
sudo systemctl is-enabled nginx
sudo systemctl is-active nginx
```

`status` shows: running or failed, main PID, recent log lines.

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

After **editing** a unit file, always `daemon-reload`.

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

---

## Knowledge check

1. `enable` vs `start`?
2. When do you `daemon-reload`?
3. How do you see the last 50 nginx log lines?

<details>
<summary>Answers</summary>

1. `start` = now. `enable` = also on boot. `enable --now` does both.
2. After changing a `.service` file.
3. `journalctl -u nginx -n 50`

</details>

➡️ Next: [Lab 04](./Lab-04-Services-Packages.md)
