# Challenge 03 — Storage Account: Blobs, SAS & File Share

**Time:** 45–60 minutes  
**You will learn:** Create storage, upload a private blob, share it with SAS, use a stored access policy, and mount an Azure File share on your VM.

## Prerequisites

- Day 1 RG + VM from Challenges 00–01 (for file share mount)

---

## Part A — Create storage account (10 min)

1. **+ Create a resource → Storage account → Create**.
2. Values:

| Field | Value |
| ----- | ----- |
| Resource group | `rg-d1-<yourname>` |
| Storage account name | `std1<yourname>01` (globally unique, lowercase) |
| Region | `<region>` |
| Performance | Standard |
| Redundancy | **LRS** |
| Access tier | Hot |

3. Tags → **Review + create → Create**.

✅ **Checkpoint:** Storage account status is Available.

---

## Part B — Private container + upload (10 min)

1. Storage account → **Containers → + Container**.
2. Name: `secured` · Public access: **Private**.
3. Open `secured` → **Upload** a small file (e.g. `HelloWorld.txt`).
4. Open the blob → copy **URL**.
5. Paste the URL in a **private browser window**.

> **Expected:** Download fails — no anonymous access.

✅ **Checkpoint:** Blob exists; anonymous URL does not work.

---

## Part C — Shared Access Signature (10 min)

### Option 1 — SAS on the blob

1. Click the blob → **Generate SAS**.
2. Permissions: **Read** only · Expiry: 1–2 hours.
3. **Generate SAS token and URL** → copy **Blob SAS URL**.
4. Open SAS URL in a private window → file should download/display.

### Option 2 — Account SAS (portal)

1. Storage account → **Shared access signature**.
2. Allowed services: Blob · Allowed resource types: Service, Container, Object · Permissions: Read/List.
3. Set short expiry → **Generate SAS and connection string**.
4. Build URL: `https://std1....blob.core.windows.net/secured/HelloWorld.txt?<SAS token>`.

✅ **Checkpoint:** File opens with SAS; fails without it.

---

## Part D — Stored access policy (10 min)

Stored policies let you **change or revoke** access after issuing a SAS.

1. Container `secured` → **Access policy → + Add policy**.

| Field | Value |
| ----- | ----- |
| Identifier | `securedap` |
| Permissions | **Read** (start with Read; you can edit later) |
| Start / Expiry | Optional but recommended |

2. **Save**.
3. Generate a SAS that references this policy:
   - Portal: blob → Generate SAS → select policy if available  
   - Or use [Azure Storage Explorer](https://azure.microsoft.com/products/storage/storage-explorer/) → container → **Get Shared Access Signature** → choose policy `securedap`
4. Test the SAS URL.
5. Edit policy: remove Read → Save → refresh SAS URL → should fail.
6. Add Read back → works again.

✅ **Checkpoint:** You can revoke access by editing the policy (without regenerating every URL manually in an ideal workflow).

---

## Part E — Azure Files + mount on VM (15 min)

1. Storage account → **File shares → + File share**.
2. Name: `myfiles` → Create.
3. Upload a test file into the share.
4. Open `myfiles` → **Connect**.
5. Choose **Windows** or **Linux** tab → **Show script** → copy.
6. RDP/SSH to `vm-d1-<yourname>-01` and run the script in PowerShell (Windows) or bash (Linux).

✅ **Checkpoint:** Share appears as a drive (Windows) or mount point (Linux).

### Discuss

| Question | Typical answer |
| -------- | -------------- |
| Default quota? | Large (historically 5 TiB scale; check portal) |
| Auth in Connect script? | Storage account key (identity-based is better in Prod) |
| Survives reboot? | Usually yes for the generated mount |

---

## Deliverables

- [ ] Storage account + private container `secured`  
- [ ] Working short-lived SAS  
- [ ] Stored access policy demonstrated  
- [ ] File share created (mounted if VM allows)  

## Cleanup

Keep storage for Challenge 07 (CSE scripts) if you plan to do it; otherwise delete the storage account to save cost.

➡️ Next: [Challenge 04 — ARM Template](./challenge-04-arm-template.md)
