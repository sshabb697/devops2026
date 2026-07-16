# Lab 01 — Portal, Resource Groups & Tags

**Time:** 45–60 minutes  
**Goal:** Get comfortable in the Azure Portal, create an organized resource group, use tags, and try Cloud Shell.

## Prerequisites

- Azure subscription
- Browser

---

## Part A — Portal tour (10 min)

1. Go to [https://portal.azure.com](https://portal.azure.com) and sign in.
2. Find these blades (search bar at the top is fine):
   - **Subscriptions** — note your subscription name
   - **Resource groups** — list (may be empty)
   - **All resources**
   - **Cost Management + Billing** (or **Cost Management**)
3. Pin **Resource groups** and **Cost Management** to the left menu (star / pin) if you use them often.

✅ **Checkpoint:** You know which subscription you are using.

---

## Part B — Create a resource group (10 min)

1. **Resource groups → Create**.
2. Fill in:
   - **Subscription:** your subscription
   - **Resource group:** `rg-lab-<yourname>`
   - **Region:** `<region>` (use the same region for all labs)
3. Open the **Tags** tab and add:

| Name | Value |
| ---- | ----- |
| Owner | `<yourname>` or your email |
| Env | Lab |
| Course | AzureEssentials |

4. **Review + create → Create**.
5. Open the RG when deployment finishes.

✅ **Checkpoint:** RG exists with three tags visible on the Overview / Tags blade.

---

## Part C — Cost awareness (10 min)

1. Open **Cost Management** → **Cost analysis** (scope = your subscription).
2. Change the view to last 7 days (or current month).
3. If available, group by **Resource group** or **Tag**.
4. Optional: **Budgets → Add** → create a small monthly budget (e.g. your training limit) with an email alert at 80%.

✅ **Checkpoint:** You can find where spend shows up (even if today’s amount is ~0).

---

## Part D — Cloud Shell (15 min)

1. In the portal, click the **Cloud Shell** icon (`>_`).
2. Choose **Bash** (or PowerShell — either works).
3. If prompted, create a storage account for Cloud Shell (accept defaults in a lab RG, or use the one Azure suggests).
4. Run:

```bash
az account show -o table
az group list -o table
az group show -n rg-lab-<yourname> -o jsonc
```

5. Add another tag from CLI:

```bash
az group update -n rg-lab-<yourname> --set tags.Project=Lab01
az group show -n rg-lab-<yourname> --query tags
```

✅ **Checkpoint:** CLI lists your RG and shows the new `Project` tag.

---

## Part E — Lock practice (optional, 5 min)

1. Open `rg-lab-<yourname>` → **Locks → Add**.
2. Name: `lab-delete-lock` · Type: **Delete**.
3. Try **Delete resource group** — it should fail or warn.
4. Remove the lock so later labs can clean up easily.

✅ **Checkpoint:** You saw how locks protect against accidental delete.

---

## Deliverables

- [ ] Resource group `rg-lab-<yourname>` in your region  
- [ ] Tags: Owner, Env, Course (+ Project from CLI)  
- [ ] Used Cloud Shell successfully  
- [ ] Know where Cost Management lives  

## Cleanup

**Keep** this RG for Labs 02–06 (reuse it).  
Only delete if your instructor says otherwise:

```bash
az group delete -n rg-lab-<yourname> --yes --no-wait
```

## Reflection

1. Why put Dev and Prod in different resource groups?  
2. What problem do tags solve for billing?  
3. When would you use a delete lock in real work?

➡️ Next: [Lab 02 — Identity, RBAC & Policy](./02-Identity-RBAC-and-Policy.md)
