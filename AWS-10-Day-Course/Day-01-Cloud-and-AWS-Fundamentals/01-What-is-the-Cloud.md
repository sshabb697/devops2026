# 01 — What is the cloud? Why AWS?

**Learning objectives**

- Explain **public cloud** vs owning your own servers
- Know the three big cloud ideas: **on-demand**, **pay-as-you-go**, **managed**
- Know what AWS is and why DevOps engineers use it

---

## One-sentence idea

The cloud is **renting someone else's computers by the hour** instead of buying your own.

---

## Everyday analogy: electricity

You don't build a power station to boil a kettle — you plug into the grid and **pay for what you use**. AWS is the grid for computing: servers, storage, databases, and networking, available in minutes and billed by the hour (or second).

| You used to… | In the cloud you… |
| ------------ | ----------------- |
| Buy a physical server (weeks, big upfront cost) | Launch a server in **2 minutes**, pay per hour |
| Guess how big to make it | **Scale up or down** any time |
| Fix the hardware yourself | AWS runs the **managed** service |
| Pay even when it's idle | **Stop it** and stop paying |

---

## Private vs public cloud

- **Private cloud:** servers your company owns, in your own data centre. You control everything — and you pay for everything, idle or not.
- **Public cloud (AWS):** shared, huge, global. You rent a slice. Someone else buys the buildings, power, and cooling.

Companies move to public cloud for **speed**, **global reach**, and turning big upfront costs into **small monthly costs**.

---

## What is AWS?

**Amazon Web Services** is the largest public cloud, with **200+ services**. You will only touch a handful in this course — the ones DevOps engineers use daily:

- **Compute:** EC2 (servers), Lambda (functions), ECS/EKS (containers)
- **Storage:** S3 (files), EBS (disks)
- **Network:** VPC (private network), Route 53 (DNS), ELB (load balancer)
- **Database:** RDS (managed SQL)
- **DevOps:** CloudFormation (IaC), CodePipeline (CI/CD), CloudWatch (monitoring)

---

## Knowledge check

1. What does "pay-as-you-go" mean?
2. Give one reason a company moves from private to public cloud.

<details>
<summary>Answers</summary>

1. You pay only for the resources you actually use, by the hour/second — stop them and the bill stops.
2. Speed to launch, global reach, no big upfront hardware cost, or less hardware maintenance.

</details>

➡️ Next: [Lab 01A](./Lab-01A-Account-and-Console.md)
