# 01 — S3 object storage

**Learning objectives**

- Understand **S3** as unlimited file storage
- Know buckets, objects, keys, and versioning

---

## One-sentence idea

S3 is an **infinite online folder** where you store files and get a web address for each one.

---

## Analogy: a giant cloakroom

You hand in a coat (file) and get a ticket (the object **key**). The cloakroom (S3) can hold unlimited coats, never loses one (11 nines of durability), and you can collect yours from anywhere in the world.

- **Bucket** = the cloakroom. Names are **globally unique** across all of AWS.
- **Object** = one file you store.
- **Key** = the object's full name/path, e.g. `images/logo.png`.

```text
s3://aws-class-amy-2026/        ← bucket (unique name)
 ├── index.html                 ← object (key = index.html)
 └── images/logo.png            ← object (key = images/logo.png)
```

---

## Why S3 is everywhere

- **Durable:** AWS copies your object across multiple AZs automatically.
- **Cheap:** pennies per GB per month.
- **Scales infinitely:** no "disk full".
- Used for: backups, static websites, data lakes, logs, build artifacts.

---

## Versioning

With **versioning on**, every overwrite keeps the old copy. Delete by accident? Restore the previous version. It's an undo button for your files.

```text
upload index.html (v1)
upload index.html (v2)   ← v1 still kept
delete index.html        ← adds a "delete marker"; v1 and v2 recoverable
```

---

## Storage classes (cost vs access speed)

| Class | Use for |
| ----- | ------- |
| **Standard** | Frequently used files (websites, active data) |
| **Standard-IA** | Infrequent access, cheaper storage |
| **Glacier** | Archives you rarely read (cheapest) |

Lifecycle rules can move old objects to cheaper classes automatically.

---

## Knowledge check

1. Why must bucket names be globally unique?
2. What does versioning protect you from?

<details>
<summary>Answers</summary>

1. S3 bucket names form part of a global URL namespace shared by every AWS account.
2. Accidental overwrites and deletions — you can restore a previous version.

</details>

➡️ Next: [Lab 05A](./Lab-05A-Bucket-and-Versioning.md)
