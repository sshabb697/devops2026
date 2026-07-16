# Lab 03 — Storage: Blob, SAS & Azure Files

**Time:** 45–60 minutes  
**Goal:** Create a storage account, upload blobs, share with a short-lived SAS, and create a file share.

## Prerequisites

- `rg-lab-<yourname>` from Lab 01  
- Remember tags: at least `Env=Lab`, `Owner=<yourname>`

---

## Part A — Create a storage account (10 min)

1. **Create a resource → Storage account**.
2. Basics:
   - Resource group: `rg-lab-<yourname>`
   - Name: `stlab<yourname>01` (globally unique, 3–24 chars, lowercase letters/numbers only)
   - Region: `<region>`
   - Performance: **Standard**
   - Redundancy: **LRS** (cheap for lab)
3. Tags: `Env=Lab`, `Owner=<yourname>`
4. **Review + create → Create**. Open the resource.

✅ **Checkpoint:** Storage account Overview shows status **Available**.

---

## Part B — Blob container & upload (10 min)

1. Storage account → **Containers → + Container**.
2. Name: `labfiles` · Public access level: **Private** (no anonymous access).
3. Open `labfiles` → **Upload** a small file (e.g. a `.txt` or image).
4. Open the blob → note you **cannot** anonymously browse it without auth.

✅ **Checkpoint:** File listed in container `labfiles`.

---

## Part C — Generate a SAS URL (15 min)

1. Click the uploaded blob → **Generate SAS**.
2. Settings:
   - Permissions: **Read** only  
   - Start time: now (or −5 minutes for clock skew)  
   - Expiry: **1–2 hours** from now  
3. **Generate SAS token and URL**.
4. Copy the **Blob SAS URL**.
5. Open a **private/incognito** browser window → paste URL → file downloads or displays.
6. Optional: wait or edit expiry to the past, regenerate invalid SAS — show it fails.

✅ **Checkpoint:** Private blob is reachable **only** with a valid SAS.

---

## Part D — Azure Files share (15 min)

1. Storage account → **File shares → + File share**.
2. Name: `teamshare` · Access tier: Transaction optimized / default · Create.
3. Open `teamshare` → **Upload** a file.
4. Click **Connect** — show the Windows or Linux mount snippet (do not require students to mount if lab PCs block it).
5. Discuss when you’d use **Files** vs **Blob** at work.

✅ **Checkpoint:** File share exists with at least one file.

---

## Part E — Soft skills / security (5 min)

Answer with your instructor:

1. Why not email the **storage account key** to a vendor?  
2. What would you change for **Prod**? (firewall, private endpoint, disable key access, shorter SAS, stored access policy)

Optional stretch:

- Storage account → **Networking** → set public access to **Selected networks** or discuss **Private endpoint** blade (create only if instructor approves cost/time).

---

## Optional CLI (AzCopy mindset)

From Cloud Shell (after creating a SAS for the container or using login):

```bash
az storage account show -g rg-lab-<yourname> -n stlab<yourname>01 -o table
az storage container list --account-name stlab<yourname>01 --auth-mode login -o table
```

> `--auth-mode login` needs appropriate RBAC data role; if it fails, use Portal only — that’s fine for this lab.

---

## Deliverables

- [ ] StorageV2 account (LRS)  
- [ ] Private container + uploaded blob  
- [ ] Working short-lived read SAS  
- [ ] File share `teamshare`  

## Cleanup

Delete the storage account if you need to save quota/cost; or keep for Lab 07 capstone.

```bash
az storage account delete -g rg-lab-<yourname> -n stlab<yourname>01 --yes
```

## Reflection

1. Blob vs File share — one example each from your job.  
2. Three settings you would tighten before Prod.  
3. How does SAS support “least privilege”?

➡️ Next: [Lab 04 — Compute](./04-Compute-VM-and-App-Service.md)
