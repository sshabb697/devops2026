# Tutor Notes — AWS 10-Day Course

Notes for the person **teaching** the class. Students do not need this file.

---

## Before Day 1

- Make sure every student can open an AWS account (needs email + card). Have a **backup shared account** with IAM users ready for anyone who cannot.
- Set a **billing alarm** in the shared account (Day 1 lab) so a forgotten NAT Gateway does not become a £100 surprise.
- Decide one **Region** for the whole class (e.g. `eu-west-1` Ireland or `us-east-1`). Mixing regions is the #1 cause of "my resource disappeared".

---

## The three money traps (repeat daily)

1. **NAT Gateway** (Day 4) — ~$0.045/hour even when idle. Delete it.
2. **RDS / EC2 left running** (Days 3, 6) — stop or terminate at end of day.
3. **EKS control plane** (Day 9) — ~$0.10/hour. Delete the cluster same day.

End **every** class with 5 minutes of cleanup. Day 10 has the master checklist.

---

## Pacing

| Day | Watch out for |
| --- | ------------- |
| 1 | Account sign-up delays; have the shared account ready. |
| 2 | Don't let students use the **root** user for labs — make an admin IAM user first. |
| 3 | SSH key permissions on Windows (`icacls`) / `chmod 400` on Linux/mac. |
| 4 | VPC wizard vs manual — use the wizard first time. **Extension:** Lab 04C needs non-overlapping CIDRs (`10.1` vs `10.2`). Lab 04D needs **two AZs** for ALB — `class-vpc` wizard already has 2 public subnets. Delete ALB before target group. |
| 5 | Bucket names are **globally unique** — add initials + date. |
| 6 | RDS takes ~10 min to create. Start it early, teach CLI while it builds. |
| 7 | CloudFormation YAML indentation errors. Validate before deploy. |
| 8 | CodeCommit is deprecated for new accounts — use GitHub source instead. |
| 9 | ECS Fargate vs EC2 launch type; EKS node group size = 1. |
| 10 | Leave 20 min for the **teardown** at the end. |

---

## Teaching rhythm

Lesson (10m) → Lab (15m) → Lesson (10m) → Lab (15m) → Recap (10m).
Keep lessons as **stories + one diagram**. Students remember the lunchbox/hotel analogies, not the service names.
