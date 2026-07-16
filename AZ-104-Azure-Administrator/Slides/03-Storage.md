---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section { font-size: 28px; }
  h1 { color: #0078d4; }
  h2 { color: #106ebe; }
  table { font-size: 22px; }
  code { font-size: 18px; }
footer: Azure Cloud Essentials | 03 Storage
---

# Module 03
## Storage

Store, upload, share, and protect data without creating a security mess

---

# Daily storage tasks

- App needs a place for uploads / reports / backups
- Team needs a shared drive in the cloud
- Partner needs a **temporary** download link
- Move lots of files quickly (AzCopy)
- Stop someone browsing your blobs from the internet

---

# Storage account = starting point

Almost everything hangs off a **storage account**:

```
  Storage account
  ├── Blob containers   → objects / files for apps
  ├── File shares       → SMB/NFS “network drive”
  ├── Queues / Tables   → simple messaging / structured data
  └── Config            → redundancy, network, encryption
```

For most labs: **General-purpose v2 (StorageV2)**.

---

# Redundancy — pick for the business, not habit

| Option | Survives… | Typical use |
|--------|-----------|-------------|
| **LRS** | Disk failures in one DC | Dev/test, cheap |
| **ZRS** | Datacenter failure in region | Important in-region apps |
| **GRS / GZRS** | Regional issues | Higher durability / DR stories |

More copies → more durable → usually **more cost**.

---

# Blob storage (most common for apps)

```
  Container  (like a folder with access rules)
      │
      └── Blobs  (the actual files)
```

Use for: images, documents, logs, static assets, backup dumps.

**Access tiers:** Hot (frequent) → Cool / Cold → Archive (rare, slow to restore)

Lifecycle rules = “move old blobs to cheaper tiers automatically.”

---

# Azure Files (shared folders)

- Feels like a traditional file share (`\\server\share`)
- Mount on Windows/Linux VMs
- Good for lift-and-shift, shared config, department files
- Can use identity-based access in real orgs

Don’t use Files when the app expects object storage APIs — use **Blob**.

---

# How to share access safely

| Method | When |
|--------|------|
| **Account keys** | Break-glass / admin only — rotate if leaked |
| **SAS URL** | Temporary, limited permission link |
| **Entra ID + RBAC data roles** | People/apps in your directory |
| **Private endpoint + firewall** | Prod: keep off public internet |

**Never** paste account keys into chat, tickets, or Git.

---

# SAS — the practical sharing tool

A SAS is a URL that expires and has limited rights (read / write / list…).

Good pattern:

1. Upload to a private container  
2. Generate SAS: **read-only**, expires in hours/days  
3. Send the link  
4. Prefer **stored access policy** so you can revoke  

---

# Tools you’ll actually use

| Tool | Job |
|------|-----|
| Portal | Upload a few files, create containers |
| Storage Explorer | Browse like a desktop app |
| **AzCopy** | Bulk copy / sync between places |
| CLI | Scripted setup |

```bash
azcopy copy "./reports" "https://acct.blob.core.windows.net/reports?<SAS>" --recursive
```

---

# Demo (20 min)

1. Create StorageV2 account (LRS for lab)  
2. Private container → upload a file  
3. Generate short-lived **read SAS** → open in private window  
4. Create a **file share** and show mount instructions  
5. Discuss: what changes for Prod (firewall / private endpoint)?  

---

# Scenarios

1. Marketing needs 20 GB of videos for a campaign this week only  
2. App stores user uploads; old files rarely read after 90 days  
3. Security says “no public storage endpoints in Prod”

---

# Summary

- Blob for objects; Files for SMB shares  
- Choose redundancy and tiers for **risk vs cost**  
- Share with **SAS or RBAC**, not permanent keys  
- Lock down network for production data  

---

# Next

➡️ **Module 04 — Compute**

Where should this application run?
