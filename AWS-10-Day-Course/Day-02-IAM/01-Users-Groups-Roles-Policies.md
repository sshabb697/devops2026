# 01 — Users, groups, roles, and policies

**Learning objectives**

- Tell apart an IAM **user**, **group**, **role**, and **policy**
- Know why you should never do daily work as the **root** user

---

## One-sentence idea

IAM decides **who can do what** in your AWS account.

---

## Analogy: a building with keycards

- **Root user** = the building owner's master key. Opens everything. You lock it in a safe and almost never use it.
- **IAM user** = a named staff member with their own keycard (you, a teammate).
- **Group** = a team whose keycards all open the same doors (e.g. *Developers*).
- **Policy** = the list printed on the keycard: which doors it opens (permissions).
- **Role** = a **temporary visitor badge** that a person *or a service* can borrow for a task, then hand back.

---

## The four building blocks

| Thing | What it is | Example |
| ----- | ---------- | ------- |
| **User** | A person or app with a long-term identity | `dev-amy` |
| **Group** | A bucket of users sharing permissions | `developers` |
| **Policy** | JSON that says Allow/Deny on actions | `AmazonS3ReadOnlyAccess` |
| **Role** | Temporary permissions, assumed on demand | An EC2 instance reading S3 |

---

## A policy is just JSON

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": ["s3:GetObject"],
    "Resource": "arn:aws:s3:::my-bucket/*"
  }]
}
```

Reads as: **Allow** the action **get an object** on **any object in my-bucket**.

---

## Why not just use root?

Root can **close the account, change billing, delete everything**. If its password leaks, you lose the account. So:

1. Protect root with a strong password + **MFA**.
2. Create an **IAM admin user** for yourself.
3. Do all daily work as that user.

---

## Knowledge check

1. What's the difference between a user and a role?
2. Why attach policies to a **group** instead of each user?

<details>
<summary>Answers</summary>

1. A user is a long-term identity; a role is temporary permissions that a user or service assumes when needed.
2. Easier management — change the group's policy once and every member updates. Add/remove people by group membership.

</details>

➡️ Next: [Lab 02A](./Lab-02A-Create-Admin-User.md)
