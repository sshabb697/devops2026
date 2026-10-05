# 02 — S3 website hosting vs EBS disks

**Learning objectives**

- Know when to use **S3** vs **EBS**
- Understand S3 **static website hosting**

---

## One-sentence idea

**S3** stores whole files you fetch by URL; **EBS** is a hard disk you attach to one EC2 instance.

---

## Object storage (S3) vs block storage (EBS)

| | S3 (object) | EBS (block) |
| - | ----------- | ----------- |
| Looks like | A web folder of files | A hard drive |
| Attached to | Nothing — accessed over HTTP | **One** EC2 instance at a time |
| Good for | Websites, backups, data lakes | OS disk, databases, app files |
| Scales | Infinite, automatic | Fixed size you choose (resizable) |
| Access | From anywhere with permission | Only the instance it's mounted to |

**Analogy:** S3 is a **library** you request books from; EBS is the **hard drive inside your laptop**.

---

## EBS quick facts

- Every EC2 instance boots from an EBS **root volume**.
- You can attach extra volumes for data.
- **Snapshots** back up a volume to S3; you can restore or copy them across AZs.
- EBS lives in **one AZ** — a snapshot is how you move data to another AZ.

---

## S3 static website hosting

S3 can serve HTML/CSS/JS straight to browsers — **no server to manage**.

To make it work you:
1. Enable **Static website hosting** (set `index.html` and `error.html`).
2. Allow **public read** (turn off "Block public access" + add a bucket policy).
3. Share the website endpoint URL.

```text
Browser ─▶ http://BUCKET.s3-website-REGION.amazonaws.com ─▶ index.html
```

Great for landing pages, docs, and single-page apps — cheap and scales to any traffic.

---

## Knowledge check

1. You need a disk for a database on EC2 — S3 or EBS?
2. What two things must you enable to serve a public website from S3?

<details>
<summary>Answers</summary>

1. EBS — it behaves like a local disk attached to the instance.
2. Static website hosting + public read access (disable Block Public Access and add a bucket policy).

</details>

➡️ Next: [Lab 05B](./Lab-05B-Static-Website.md)
