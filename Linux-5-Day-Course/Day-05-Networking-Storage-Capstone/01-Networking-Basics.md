# 01 — Networking Basics

![Linux networking basics](../images/linux-networking-basics.png)

**Learning objectives**

- Find your IP and default gateway
- Test connectivity with ping and curl
- List listening ports with `ss`

---

## IP address & interfaces

```bash
ip addr show
ip a
hostname -I
```

Common interface names: `eth0`, `ens33`, `wlan0`, `lo` (loopback `127.0.0.1`).

WSL often uses `eth0` with a virtual IP. Cloud VMs use `eth0` or `ens*`.

---

## Routing

```bash
ip route
ip route show default
```

Default gateway = router that forwards traffic to the internet.

---

## Test connectivity

```bash
ping -c 4 8.8.8.8              # reach Google DNS (ICMP)
ping -c 4 google.com
curl -I https://example.com
```

| Result | Meaning |
| ------ | ------- |
| ping IP works, name fails | Likely **DNS** issue |
| ping fails entirely | Routing, firewall, or host down |
| curl works | HTTP/TCP path OK |

Some networks block ICMP (`ping`). Then try `curl` or `nc`.

---

## Ports & listeners

```bash
ss -tulpn
sudo ss -tulpn | grep LISTEN
sudo lsof -i :22
sudo lsof -i :80
```

| Port | Typical service |
| ---- | --------------- |
| 22 | SSH |
| 80 | HTTP |
| 443 | HTTPS |
| 3306 | MySQL |
| 5432 | PostgreSQL |

`ss` replaced `netstat` on modern Linux.

---

## Firewall (awareness)

```bash
# Ubuntu (ufw)
sudo ufw status
sudo ufw allow 22/tcp

# RHEL (firewalld)
sudo firewall-cmd --list-all
```

Cloud: also check **NSG / security groups** in Azure/AWS — the OS firewall can be open while the cloud still blocks traffic.

---

## Knowledge check

1. Command to show IP addresses?
2. Ping IP works, ping name fails — what is likely broken?
3. How do you see what is listening on port 80?

<details>
<summary>Answers</summary>

1. `ip a` or `ip addr show`
2. DNS
3. `sudo ss -tulpn | grep :80` or `sudo lsof -i :80`

</details>

➡️ Next: [02 — DNS & Troubleshooting](./02-DNS-Troubleshooting.md)
