# Lab 03A — Launch EC2 + deploy a web app

**Time:** 15 minutes
Uses the script [`user-data.sh`](./user-data.sh) to auto-install a web server.

---

## Part A — Launch the instance (8 min)

1. **EC2 → Instances → Launch instances**.
2. **Name:** `web-class`. Add tag **Project = aws-class**.
3. **AMI:** Amazon Linux 2023.
4. **Instance type:** `t2.micro` (or `t3.micro`) — *Free tier eligible*.
5. **Key pair:** Create new → name `class-key` → **.pem** → download it (keep it safe).
6. **Network settings → Edit** → Security group rules:
   - Allow **SSH (22)** from *My IP*.
   - **Add rule** → **HTTP (80)** from *Anywhere (0.0.0.0/0)*.
7. **Advanced details → IAM instance profile:** choose `ec2-s3-read` (from Day 2).
8. **Advanced details → User data:** paste the contents of [`user-data.sh`](./user-data.sh).
9. **Launch instance.**

---

## Part B — Open the web page (7 min)

1. Wait until **Instance state = Running** and **Status checks = 2/2**.
2. Select the instance → copy the **Public IPv4 address**.
3. Open `http://PUBLIC_IP` in a browser (http, not https).
4. You should see **"Hello from EC2 🎉"** with the Availability Zone.

> First boot takes 1–2 minutes while the script installs Apache. Refresh if it's not ready.

---

## If you get stuck

| Problem | Fix |
| ------- | --- |
| Page won't load | Did you add the **HTTP 80** rule? Check the security group. |
| Still blank after 3 min | Connect (Part B of Lab 03B) and run `sudo systemctl status httpd`. |
| Used https:// | Use **http://** — we didn't set up TLS. |

Leave the instance running for Lab 03B.

---

## Deliverables

- [ ] `web-class` instance Running, tagged `Project=aws-class`
- [ ] Web page visible in a browser
- [ ] Role `ec2-s3-read` attached

➡️ Next: [02 — Security groups, key pairs, instance types](./02-Security-Keys-Types.md)
