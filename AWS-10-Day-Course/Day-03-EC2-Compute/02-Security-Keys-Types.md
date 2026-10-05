# 02 — Security groups, key pairs, and instance types

**Learning objectives**

- Understand a **security group** as a firewall
- Know what a **key pair** is for
- Read an **instance type** name

---

## One-sentence idea

A **security group** controls which traffic reaches your instance; a **key pair** proves it's really you logging in.

---

## Security groups = a firewall around the instance

A security group is a list of **allow** rules. Anything not allowed is blocked.

| Rule | Port | Source | Meaning |
| ---- | ---- | ------ | ------- |
| SSH | 22 | My IP | Only *you* can log in |
| HTTP | 80 | 0.0.0.0/0 | Anyone can view the website |

> **Never** open SSH (22) to `0.0.0.0/0`. Bots scan the internet for open SSH ports constantly. Restrict it to **My IP**.

Security groups are **stateful**: if you allow traffic in, the reply is automatically allowed out.

---

## Key pairs

SSH uses two keys:

- **Public key** — AWS keeps this on the instance.
- **Private key** (`class-key.pem`) — *you* keep this. Anyone with it can log in, so protect it.

```bash
# Linux / macOS — lock down the file first
chmod 400 class-key.pem
ssh -i class-key.pem ec2-user@PUBLIC_IP
```

On Windows PowerShell, use the EC2 **Connect** button or `icacls` to fix permissions.

---

## Reading an instance type

```text
t3.micro
│ │  └── size (nano < micro < small < medium < large …)
│ └───── generation (3 = 3rd gen)
└─────── family (t = burstable/cheap, m = general, c = compute, r = memory)
```

- `t2`/`t3.micro` — tiny, Free Tier, perfect for class.
- `m5.large` — balanced, for real apps.
- `c6g.xlarge` — compute-heavy.

---

## Knowledge check

1. Why should SSH (22) be limited to *My IP*?
2. What happens if you lose your `.pem` private key?

<details>
<summary>Answers</summary>

1. Open SSH to the world invites brute-force attacks from bots scanning the internet.
2. You can't SSH in with it anymore — you'd attach the volume elsewhere or recreate the instance. Keep the key safe.

</details>

➡️ Next: [Lab 03B](./Lab-03B-SSH-and-Explore.md)
