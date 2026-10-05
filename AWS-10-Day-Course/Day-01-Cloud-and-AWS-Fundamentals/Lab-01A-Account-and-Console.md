# Lab 01A — Account, console, and Regions

**Time:** 15 minutes

> If you already have an account, skip Part A and just do B and C.

---

## Part A — Open an AWS account (if needed) (7 min)

1. Go to <https://aws.amazon.com/free/> → **Create a Free Account**.
2. Enter email, account name, password.
3. Add card details (AWS may place a small temporary hold).
4. Choose the **Basic support — Free** plan.

> The email + password you just made is the **root user**. We will barely use it — it is too powerful for daily work (more on Day 2).

---

## Part B — Tour the console (4 min)

1. Sign in at <https://console.aws.amazon.com/>.
2. Top-right: note the **Region selector** (e.g. *Ireland (eu-west-1)*). **Write your Region down.**
3. Top-left: the **Services** menu — this is the list of 200+ services.
4. In the search bar, type `EC2`, `S3`, `IAM` — see how search jumps you to any service.

---

## Part C — Find your account ID (4 min)

1. Click your account name (top-right) → **Account**.
2. Note your **12-digit Account ID**. You'll use it later (e.g. for ECR).

```text
My Region:     ___________________
My Account ID: ___________________
```

---

## If you get stuck

| Problem | Fix |
| ------- | --- |
| Card declined | Use a different card; prepaid cards often fail. |
| Verification stuck | AWS sometimes takes a few hours — use the shared class account meanwhile. |
| Services look empty | Check the **Region** — resources are per-region. |

---

## Deliverables

- [ ] Logged into the console
- [ ] Wrote down Region + Account ID

➡️ Next: [02 — Regions, AZs, and billing](./02-Regions-AZs-and-Billing.md)
