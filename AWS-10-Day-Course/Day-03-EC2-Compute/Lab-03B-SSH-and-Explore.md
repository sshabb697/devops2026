# Lab 03B — SSH in and explore

**Time:** 15 minutes
Uses the instance from Lab 03A.

---

## Part A — Connect (6 min)

**Easiest:** select the instance → **Connect** → **EC2 Instance Connect** → **Connect** (browser terminal, no key needed).

**With your key (terminal):**
```bash
# Linux / macOS
chmod 400 class-key.pem
ssh -i class-key.pem ec2-user@PUBLIC_IP
```
On Windows, use the browser **Connect** button if SSH gives a permissions error.

---

## Part B — Look around (5 min)

```bash
whoami                      # ec2-user
cat /etc/os-release         # Amazon Linux 2023
systemctl status httpd      # the web server is running
curl localhost              # the HTML your user-data wrote
```

---

## Part C — Prove the IAM role works (4 min)

Because you attached the `ec2-s3-read` role, the server can read S3 with **no keys stored**:

```bash
aws s3 ls                   # lists your buckets using temporary role credentials
```

If you have no buckets yet, it returns nothing — that's fine; it didn't error with "access denied".

---

## End of day — STOP the instance 💸

```text
EC2 → Instances → select web-class → Instance state → Stop instance
```

Stopping avoids compute charges overnight. (Terminate at the end of the week.)

---

## If you get stuck

| Problem | Fix |
| ------- | --- |
| SSH permission denied | Use **EC2 Instance Connect** in the browser. |
| `aws s3 ls` says access denied | Confirm the `ec2-s3-read` role is attached to the instance. |

---

## Deliverables

- [ ] Connected to the instance
- [ ] Saw `httpd` running and the role let you run `aws s3 ls`
- [ ] **Stopped** the instance

➡️ Next day: [Day 4 — Networking (VPC)](../Day-04-Networking-VPC/)
