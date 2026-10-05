# Lab 02B — A read-only user and an EC2 role

**Time:** 15 minutes

---

## Part A — Create a read-only user (6 min)

1. **IAM → Users → Create user**, name `viewer`.
2. Enable console access, set a password.
3. **Attach policies directly** → tick **ReadOnlyAccess**. Create.
4. Open a private/incognito window, sign in as `viewer`.
5. Try to **launch an EC2 instance** → it is blocked (no write permission). 
6. Browse around read-only — you can *see* but not *change*. Close the window.

> This is least privilege in action.

---

## Part B — Create an EC2 role for S3 (9 min)

We'll build the role now and attach it to a server on Day 3.

1. **IAM → Roles → Create role**.
2. Trusted entity: **AWS service** → **EC2**. Next.
3. Attach permissions: **AmazonS3ReadOnlyAccess**. Next.
4. Role name: `ec2-s3-read`. Create role.

```text
Who can use it?  EC2 instances (trust policy)
What can it do?  Read any S3 bucket (permissions policy)
```

Keep this role — Day 3 attaches it to your EC2 instance so the server reads S3 **without any keys on disk**.

---

## If you get stuck

| Problem | Fix |
| ------- | --- |
| `viewer` can still change things | Make sure you attached **ReadOnlyAccess**, not an admin policy. |
| No EC2 option under trusted entity | Choose **AWS service**, then pick **EC2** from the use-case list. |

---

## Deliverables

- [ ] `viewer` user exists and is blocked from launching EC2
- [ ] Role `ec2-s3-read` created (trusts EC2, allows S3 read)

➡️ Next day: [Day 3 — EC2 Compute](../Day-03-EC2-Compute/)
