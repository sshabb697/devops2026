# Lab 05B — Host a static website

**Time:** 15 minutes
Serves the files in [`site/`](./site/) (`index.html`, `error.html`) from S3.

---

## Part A — Enable website hosting (4 min)

1. Open your bucket → **Properties → Static website hosting → Edit → Enable**.
2. Index document: `index.html`; Error document: `error.html`. Save.
3. Copy the **Bucket website endpoint** URL shown there.

---

## Part B — Make it public (6 min)

1. **Permissions → Block public access → Edit** → untick **Block all public access**. Save, confirm.
2. **Permissions → Bucket policy → Edit** → paste (replace the bucket name):

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Sid": "PublicReadForWebsite",
    "Effect": "Allow",
    "Principal": "*",
    "Action": "s3:GetObject",
    "Resource": "arn:aws:s3:::aws-class-amy-051026/*"
  }]
}
```

3. Save.

---

## Part C — Upload the site and visit it (5 min)

```bash
aws s3 cp site/index.html s3://aws-class-amy-051026/
aws s3 cp site/error.html s3://aws-class-amy-051026/
# or, from the Day-05 folder:
aws s3 sync site/ s3://aws-class-amy-051026/
```

- Open the **website endpoint** URL → you see "Hello from Amazon S3".
- Visit a made-up path like `/nope` → you see your custom **404** page.

---

## End of day — delete the bucket 💸

```bash
aws s3 rb s3://aws-class-amy-051026 --force   # empties and removes it
```

---

## If you get stuck

| Problem | Fix |
| ------- | --- |
| **403 Forbidden** | Bucket policy missing/wrong bucket name, or Block Public Access still on. |
| Wrong URL | Use the **website endpoint**, not the plain object URL. |

---

## Deliverables

- [ ] Static website hosting enabled
- [ ] Public bucket policy applied
- [ ] Website + custom 404 both load
- [ ] Bucket deleted at end of day

➡️ Next day: [Day 6 — Databases + AWS CLI](../Day-06-Databases-and-CLI/)
