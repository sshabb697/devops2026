# Lab 05A — Bucket, upload, versioning

**Time:** 15 minutes

> Bucket names are **globally unique**. Use something like `aws-class-<yourname>-<ddmmyy>`.

---

## Part A — Create a bucket (5 min)

**Console:**
1. **S3 → Create bucket**.
2. Name: `aws-class-amy-051026` (make yours unique).
3. Region: your class Region. Leave **Block all public access ON** for now.
4. Add tag **Project = aws-class**. Create.

**CLI (alternative):**
```bash
aws s3 mb s3://aws-class-amy-051026
```

---

## Part B — Upload and turn on versioning (6 min)

1. Open the bucket → **Properties → Bucket Versioning → Edit → Enable**. Save.
2. Upload a file:
   ```bash
   echo "version one" > note.txt
   aws s3 cp note.txt s3://aws-class-amy-051026/
   ```
3. Change it and upload again:
   ```bash
   echo "version two" > note.txt
   aws s3 cp note.txt s3://aws-class-amy-051026/
   ```

---

## Part C — See the versions (4 min)

1. In the console, open the bucket, toggle **Show versions** (top of the object list).
2. You'll see **two versions** of `note.txt`.
3. Delete `note.txt` → notice a **delete marker** appears, but the versions are still there to restore.

```bash
aws s3api list-object-versions --bucket aws-class-amy-051026 --prefix note.txt \
  --query "Versions[].[Key,VersionId,IsLatest]" --output table
```

---

## If you get stuck

| Problem | Fix |
| ------- | --- |
| "Bucket already exists" | Name isn't unique — add more to it. |
| Can't see versions | Enable versioning **before** uploading; toggle **Show versions**. |

---

## Deliverables

- [ ] Bucket created, tagged `Project=aws-class`
- [ ] Versioning enabled; two versions of `note.txt`
- [ ] Understood the delete marker

➡️ Next: [02 — S3 website vs EBS disks](./02-Website-and-EBS.md)
