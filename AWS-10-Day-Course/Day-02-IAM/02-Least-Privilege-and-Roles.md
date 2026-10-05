# 02 — Least privilege and roles

**Learning objectives**

- Apply the **least-privilege** principle
- Understand why **roles** are safer than long-lived access keys

---

## One-sentence idea

Give every user and service the **smallest set of permissions** it needs — nothing more.

---

## Least privilege in practice

A person who only reads reports doesn't need delete powers. Start from **zero** and add only what's needed.

| Job | Give them |
| --- | --------- |
| Views dashboards | `ReadOnlyAccess` |
| Manages S3 only | `AmazonS3FullAccess` |
| App server reading one bucket | A **role** with `s3:GetObject` on that bucket |

If someone needs more later, add it. This limits the blast radius if a password or key leaks.

---

## Why roles beat access keys

An **access key** is a username+password for code. If it leaks (committed to GitHub, left in a script), an attacker has long-term access.

A **role** gives **temporary** credentials that AWS rotates automatically. Nothing to leak.

### The classic example: EC2 reading S3

**Bad:** store an access key on the EC2 server so your app can read S3.
**Good:** attach an **IAM role** to the EC2 instance. The app gets temporary keys automatically — no secrets on disk.

```text
EC2 instance ──assumes──▶ Role "ec2-s3-read" ──allows──▶ s3:GetObject on my-bucket
```

---

## Policy types you'll meet

- **AWS managed** — ready-made by AWS (`AmazonS3ReadOnlyAccess`). Easiest to start.
- **Customer managed** — your own reusable JSON policy.
- **Inline** — attached directly to one user/role (avoid for anything shared).

---

## Knowledge check

1. Why is a role safer than putting an access key on a server?
2. You have a user who only needs to look at billing. What do you give them?

<details>
<summary>Answers</summary>

1. Roles provide temporary, auto-rotated credentials — there is no long-lived secret to leak.
2. Read-only billing permissions (least privilege) — not admin.

</details>

➡️ Next: [Lab 02B](./Lab-02B-ReadOnly-and-Role.md)
