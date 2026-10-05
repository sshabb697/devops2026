# 02 — RDS managed databases

**Learning objectives**

- Understand what **RDS** manages for you
- Know the pieces: engine, instance class, subnet group, security

---

## One-sentence idea

RDS runs a **database for you** — backups, patching, and failover are Amazon's job, not yours.

---

## Analogy: a managed restaurant kitchen

Running your own database on EC2 is like cooking every meal yourself: you buy the ingredients, patch the oven, clean up. **RDS** is a managed kitchen — you just order the dish (a database) and the staff handle maintenance, backups, and replacements if the oven breaks.

### What RDS does for you
- **Automated backups** and point-in-time restore.
- **Patching** of the database engine.
- **Multi-AZ failover** — a standby copy in another AZ takes over if the primary fails.
- **Monitoring** via CloudWatch.

You still choose the data model and write the SQL.

---

## Choices when you create an RDS instance

| Choice | Meaning | Class value |
| ------ | ------- | ----------- |
| **Engine** | Database type | MySQL / PostgreSQL |
| **Templates** | Free tier / Prod / Dev | **Free tier** |
| **Instance class** | Size | `db.t3.micro` |
| **Storage** | Disk | 20 GB gp3 |
| **VPC / subnet group** | Where it lives | Private subnets ideally |
| **Public access** | Reachable from internet? | **No** for real apps |
| **Security group** | Who can connect | App servers only, port 3306/5432 |

---

## Where should a database live?

In a **private subnet**, reachable only by your app servers — never open the database port to the whole internet. For this class lab we may allow your IP briefly to test, then delete it.

```text
App EC2 (public subnet) ──port 3306──▶ RDS MySQL (private subnet)
          Internet ──✗── (no direct path to the database)
```

---

## Knowledge check

1. Name two things RDS manages that you'd otherwise do yourself.
2. Why keep a production database in a private subnet?

<details>
<summary>Answers</summary>

1. Backups, engine patching, Multi-AZ failover, monitoring (any two).
2. To keep it off the public internet — only app servers inside the VPC should reach it.

</details>

➡️ Next: [Lab 06B](./Lab-06B-Create-RDS.md)
