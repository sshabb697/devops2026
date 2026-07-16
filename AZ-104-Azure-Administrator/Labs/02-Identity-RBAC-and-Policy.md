# Lab 02 — Identity, RBAC & Policy

**Time:** 45–60 minutes  
**Goal:** Grant least-privilege access with a group, prove Contributor vs Reader, and apply a simple Azure Policy.

## Prerequisites

- Lab 01 complete (`rg-lab-<yourname>` exists)
- Permission to assign roles on your RG (Owner or User Access Administrator on that scope)
- **Ideal:** a second test user (classmate, guest, or alternate account). If you only have one user, follow the **Solo path** notes.

---

## Part A — Create a security group (10 min)

1. Search **Microsoft Entra ID** (or **Azure Active Directory**).
2. **Groups → New group**:
   - **Group type:** Security  
   - **Group name:** `grp-lab-<yourname>-contributors`  
   - **Membership type:** Assigned  
3. **Members:** add your second user (or yourself for Solo path).
4. **Create**.

✅ **Checkpoint:** Group exists under Entra ID → Groups.

---

## Part B — Assign Reader (15 min)

1. Open `rg-lab-<yourname>` → **Access control (IAM)**.
2. **Add → Add role assignment**.
3. Role: **Reader**.
4. Members: select group `grp-lab-<yourname>-contributors`.
5. **Review + assign**.

### Verify (two-user path)

1. Sign in to the portal as the **member** user (private window).
2. Open the RG — you should **see** it.
3. Try **Create** a storage account in that RG — it should **fail** (no permission).

### Solo path

1. On IAM → **View my access** / Role assignments — confirm Reader is listed for the group.
2. Instructor demo: show a volunteer hitting “Create” denied.

✅ **Checkpoint:** Reader can view, not create.

---

## Part C — Upgrade to Contributor (10 min)

1. IAM → remove the **Reader** assignment for the group (or leave it and add Contributor — Contributor is enough).
2. Add role assignment: **Contributor** to the same group on the same RG.
3. As the member user, create a cheap resource to prove access:
   - **Create a resource → Storage account** (or any free/cheap resource)
   - Name: `stlab<yourname>rbac` (must be globally unique, lowercase)
   - Region: same as RG · Redundancy: **LRS** · Leave public access defaults for now
4. Deploy successfully.

✅ **Checkpoint:** Contributor can create resources **inside that RG**.

---

## Part D — Scope lesson (5 min)

Discuss / verify:

- Does Contributor on the RG let you assign roles to other people?  
  → **No.** Only Owner / User Access Administrator can assign roles.
- Would you grant Contributor on the **subscription** for a single app team?  
  → Prefer **RG scope**.

---

## Part E — Azure Policy: require a tag (15 min)

1. Search **Policy** → **Definitions**.
2. Search built-in: **Require a tag on resources** (or **Require a tag and its value on resources**).
3. Select it → **Assign policy**:
   - **Scope:** `rg-lab-<yourname>` (not the whole subscription if you can avoid it)
   - **Tag Name:** `Env`
   - Create / assign (remediation optional — skip for lab)
4. Wait 1–2 minutes for assignment to take effect.
5. Try creating another storage account **without** tag `Env`:
   - Expected: **denied** or shown non-compliant (depending on effect / portal timing)
6. Create again **with** tag `Env=Lab` → should succeed.

> If Policy doesn’t block immediately, open **Policy → Compliance** for your assignment and discuss Audit vs Deny effects with the instructor.

✅ **Checkpoint:** Policy assignment exists on your RG for tag `Env`.

---

## Part F — Lock (optional, 5 min)

1. On a resource you care about (or the RG), add lock type **Delete**.
2. Attempt delete → blocked.
3. Remove lock before end of class if you need cleanup.

---

## Deliverables

- [ ] Security group created  
- [ ] RBAC: group has access on `rg-lab-<yourname>` only  
- [ ] Demonstrated view-only vs create  
- [ ] Policy assignment requiring `Env` tag  

## Cleanup notes

- Keep the RG and group for later labs.  
- You may delete the temporary storage accounts created in this lab to save cost.  
- Leave Policy assigned (helps Lab 03 remember tags) or remove if it blocks demos — instructor choice.

## Reflection

1. Why assign roles to **groups** instead of users?  
2. Contributor vs Owner — when is Owner justified?  
3. How does Policy help even when everyone is Contributor?

➡️ Next: [Lab 03 — Storage](./03-Storage-Blob-Files-SAS.md)
