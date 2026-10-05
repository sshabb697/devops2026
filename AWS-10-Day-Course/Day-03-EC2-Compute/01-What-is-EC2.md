# 01 — What is EC2?

**Learning objectives**

- Know what an **EC2 instance** is
- Understand AMI, instance type, and the pieces you pick when launching

---

## One-sentence idea

EC2 is a **virtual computer you rent by the hour** in AWS.

---

## Analogy: renting a laptop

You don't buy a laptop to use for one afternoon — you rent one. EC2 is renting a computer in Amazon's data centre: pick the **operating system**, the **size**, press go, and it's yours in two minutes. Give it back (terminate) and you stop paying.

**EC2** = *Elastic Compute Cloud*. "Elastic" because you can get 1 or 1,000 of them on demand.

---

## What you choose when you launch

| Choice | What it means | Class value |
| ------ | ------------- | ----------- |
| **AMI** | The disk image = OS + pre-installed software | Amazon Linux 2023 |
| **Instance type** | CPU + memory size | `t2.micro` / `t3.micro` (Free Tier) |
| **Key pair** | SSH key to log in | `class-key` |
| **Security group** | A firewall: which ports are open | allow 22 (SSH) + 80 (web) |
| **User data** | A script that runs on first boot | install a web server |

---

## The web-app pattern (today's lab)

```text
Internet ──▶ Security group (allow 80) ──▶ EC2 instance ──▶ web server (Apache) ──▶ index.html
```

We use **user data** so the server installs Apache and writes a web page **automatically** on first boot — no manual setup.

---

## Instance lifecycle

- **Running** — billed for compute.
- **Stopped** — no compute charge (small EBS disk charge remains). Great for overnight.
- **Terminated** — gone forever, disk deleted, no charge.

> For class: **stop** at end of day; **terminate** at end of the week.

---

## Knowledge check

1. What does an AMI give you?
2. What's the difference between **stopped** and **terminated**?

<details>
<summary>Answers</summary>

1. A pre-built disk image: the operating system plus any bundled software.
2. Stopped can be started again (disk kept, little/no charge); terminated is permanently deleted.

</details>

➡️ Next: [Lab 03A](./Lab-03A-Launch-and-Deploy.md)
