# 02 — Regions, Availability Zones, and billing

**Learning objectives**

- Understand **Region** vs **Availability Zone (AZ)**
- Know why "resource not found" is usually a wrong-Region mistake
- Understand how AWS bills you and how to stay safe

---

## One-sentence idea

AWS is split into **Regions** (cities) and each Region has several **Availability Zones** (separate buildings) so one failure doesn't take you down.

---

## Analogy: a hotel chain

- **Region** = a city (e.g. *Ireland*, *N. Virginia*). You pick the city closest to your users.
- **Availability Zone** = a separate hotel building in that city, with its own power and internet.
- Spreading your app across **2+ AZs** means if one building loses power, the other keeps serving.

```text
Region: eu-west-1 (Ireland)
 ├── AZ eu-west-1a   (data centre A)
 ├── AZ eu-west-1b   (data centre B)
 └── AZ eu-west-1c   (data centre C)
```

> **Rule of thumb:** almost every "my resource disappeared!" problem is really "I'm looking in the wrong Region."

---

## How AWS bills you

- **By the hour or second** for most compute (EC2, RDS).
- **By the gigabyte** for storage (S3, EBS) and data transfer **out**.
- **Per request** for serverless (Lambda, S3 requests).
- **Free Tier** covers small amounts for 12 months (e.g. 750 hrs/month of a `t2.micro`/`t3.micro`).

### The three things that cause surprise bills
1. **Forgetting to stop** an EC2 instance or RDS database.
2. **NAT Gateways** (Day 4) — charged per hour even when idle.
3. **Data transfer out** at large scale.

Your defence: **billing alarms** (next lab) + **tag everything** + **delete at end of day**.

---

## Knowledge check

1. What's the difference between a Region and an AZ?
2. Why run an app across two AZs?

<details>
<summary>Answers</summary>

1. A Region is a geographic location (a city); an AZ is one isolated data centre inside that Region.
2. High availability — if one AZ fails, the app keeps running in the other.

</details>

➡️ Next: [Lab 01B](./Lab-01B-Billing-Alarm.md)
