# Lab 06 — Monitor: Alerts & Backup

**Time:** 45–60 minutes  
**Goal:** Read metrics, create an alert with an action group, inspect Activity Log, and configure a Recovery Services vault (backup).

## Prerequisites

- Something to monitor: App Service from Lab 04 and/or a VM  
- If neither exists, create a quick App Service (Free/B1) first  

---

## Part A — Explore metrics (10 min)

1. Open your **App Service** or **VM**.
2. Left menu → **Metrics** (or **Monitoring → Metrics**).
3. Chart examples:
   - App Service: **Average Response Time** or **Http 2xx/5xx**
   - VM: **Percentage CPU**
4. Change time range to **Last 24 hours** / **Last 1 hour**.
5. **Pin to dashboard** (optional) — create a simple dashboard tile.

✅ **Checkpoint:** You can show a live metric chart for your resource.

---

## Part B — Action group (10 min)

1. Search **Monitor** → **Alerts → Action groups → Create**.
2. Basics:
   - RG: `rg-lab-<yourname>`
   - Name: `ag-lab-<yourname>`
   - Display name: `LabNotify`
3. **Notifications:** Email/SMS user → add **your email** → enable.
4. Review + create.

✅ **Checkpoint:** Action group exists and shows your email.

---

## Part C — Metric alert rule (15 min)

1. Monitor → **Alerts → Create → Alert rule**.
2. **Scope:** select your App Service or VM.
3. **Condition:**  
   - Signal: **Percentage CPU** (VM) or **Http Server Errors** / Response Time (App)  
   - For lab: use a threshold you can understand (e.g. CPU > 1% for 1 minute) — may fire in lab; that’s OK  
   - Or use **Activity Log** signal: Administrative → Delete (see Part D alternative)
4. **Actions:** attach `ag-lab-<yourname>`.
5. Alert rule name: `alert-lab-<yourname>-health`
6. Create.

Optional: generate a little load on the VM (`stress` / busy loop) to trigger — only if instructor wants noise.

✅ **Checkpoint:** Alert rule listed under Monitor → Alerts → Alert rules.

---

## Part D — Activity Log (10 min)

1. Open `rg-lab-<yourname>` → **Activity log**  
   (or Monitor → Activity log, filter by RG).
2. Find recent operations: Create, Write, Delete.
3. Open one event — note **Caller**, **Status**, **Resource**.
4. Discuss: how this helps “who deleted Prod?”

✅ **Checkpoint:** You identified at least one create/write event with a caller identity.

---

## Part E — Backup vault (15–20 min)

1. **Create a resource → Backup and Site Recovery** / **Recovery Services vault**.
2. Name: `rsv-lab-<yourname>` · RG + region same as labs.
3. Open vault → **Backup** (or **+ Backup**).
4. Configure:
   - Workload: **Azure**  
   - What to back up: **Virtual machine** (if you have a VM)  
   - Or **Azure Files** if you still have Lab 03 file share  
5. Select your VM / file share → choose/create a backup policy (default daily is fine for lab).
6. **Enable Backup**. Wait until item shows under **Backup items**.

> If VM backup isn’t available (agent/extension delay), walk through blades with instructor and mark “configured” when the vault + policy exist.

✅ **Checkpoint:** Recovery Services vault exists; at least one backup item or policy is configured.

---

## Part F — Restore mindset (discussion, 5 min)

Answer:

1. Difference between **Stop VM** and **Restore VM from backup**?  
2. When is **Site Recovery** needed instead of Backup?  
3. How often should a team **test** a restore?

---

## Deliverables

- [ ] Metric chart reviewed  
- [ ] Action group with email  
- [ ] Alert rule attached to action group  
- [ ] Activity Log inspected  
- [ ] Recovery Services vault created (+ backup enabled if possible)  

## Cleanup

- Disable or delete alert rules to avoid email spam.  
- Backup vaults can be annoying to delete if soft-delete is on — follow portal guidance; instructor may keep vaults until course end.

```bash
az monitor action-group list -g rg-lab-<yourname> -o table
```

## Reflection

1. What alert would your real team want on a customer-facing site?  
2. Why send diagnostics to Log Analytics in production?  
3. What’s one backup you should enable this month at work?

➡️ Next: [Lab 07 — Capstone](./07-Capstone-Mini-Stack.md)
