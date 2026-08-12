# 02 — DNS & Troubleshooting

---

## What DNS does

Maps **names → IP addresses** (and more: MX, CNAME, TXT).

```bash
nslookup google.com
dig google.com
dig google.com +short
host github.com
```

---

## Resolver config

```bash
cat /etc/resolv.conf
resolvectl status                 # systemd-resolved (Ubuntu)
```

---

## Troubleshooting flow

```
Can you ping 8.8.8.8?
  NO  → check cable/VPN, ip route, gateway, cloud NSG
  YES → Can you ping google.com?
          NO  → DNS: resolv.conf, dig, corporate DNS
          YES → Is the *service* up? ss -tulpn, systemctl, curl :port
```

---

## Useful commands

```bash
traceroute google.com
tracepath google.com
mtr google.com                    # if installed

curl -v http://localhost:80
telnet host 22                    # test TCP port (legacy)
nc -zv host 443                   # modern port test
```

---

## `/etc/hosts` override

```bash
cat /etc/hosts
# 127.0.0.1   localhost
# 192.168.1.10 myinternalapp.local
```

Useful in labs before DNS exists.

---

## Real incident pattern

> "SSH works by IP but not hostname" → DNS or `/etc/hosts`  
> "Site loads locally but not remotely" → bind address, firewall, NSG  
> "Connection refused" → service down or wrong port  
> "Connection timed out" → firewall blocking

➡️ Next: [03 — Disk & Storage](./03-Disk-Storage.md)
