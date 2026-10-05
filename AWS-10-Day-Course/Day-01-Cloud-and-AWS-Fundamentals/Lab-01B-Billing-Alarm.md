# Lab 01B — Set a billing alarm

**Time:** 15 minutes
**Why:** This single alarm is the cheapest insurance you will ever set up. It emails you if your spend crosses a threshold.

---

## Part A — Turn on billing alerts (4 min)

1. Sign in, search **Billing and Cost Management**.
2. Left menu → **Billing preferences**.
3. Enable **Receive CloudWatch billing alerts** (older accounts) / **Alert preferences**. Save.

---

## Part B — Create the alarm (8 min)

Billing metrics live in the **N. Virginia (us-east-1)** Region — switch your Region selector to **us-east-1** first.

1. Search **CloudWatch** → **Alarms** → **Create alarm**.
2. **Select metric** → **Billing** → **Total Estimated Charge** → **USD** → Select metric.
3. Condition: **Greater than** `5` (USD). Click Next.
4. **Create a new SNS topic**, enter your email, **Create topic**.
5. Name the alarm `class-billing-over-5usd`. Create.
6. **Check your email** and click **Confirm subscription**.

---

## Part C — Prove it works (3 min)

- In CloudWatch → Alarms, your alarm shows **OK** (or *Insufficient data* until billing data arrives).
- You will get an email the moment estimated charges pass $5.

---

## If you get stuck

| Problem | Fix |
| ------- | --- |
| No Billing metric | Switch Region to **us-east-1**; wait a few hours after enabling alerts. |
| No confirmation email | Check spam; re-send from SNS → Subscriptions. |

---

## Deliverables

- [ ] Billing alerts enabled
- [ ] Alarm `class-billing-over-5usd` created
- [ ] Email subscription **confirmed**

➡️ Next day: [Day 2 — IAM](../Day-02-IAM/)
