# Challenge 09 (Optional) — Automation & Cost Awareness

**Time:** 40–50 minutes  
**You will learn:** Read Azure costs, create an **Automation Account** runbook, and schedule a practical task (deallocate a lab VM to save money).

> The original trainingdays Challenge 9 used a full “email me yesterday’s cost” solution. This version keeps the **same learning goals** (Automation + cost) with steps you can finish in one lab session.

---

## Part A — Review yesterday’s / this month’s cost (10 min)

1. Portal → **Cost Management + Billing** → **Cost analysis**.
2. Scope: your subscription.
3. View: **This month** (or Last 7 days).
4. Group by **Resource group** and by **Service name**.
5. Optional: create a **Budget** with email alert at 80% of a training limit.

✅ **Checkpoint:** You can point to your most expensive lab RG.

---

## Part B — Create an Automation Account (10 min)

1. **+ Create a resource → Automation → Create**.

| Field | Value |
| ----- | ----- |
| Name | `aa-d1-<yourname>` |
| Resource group | `rg-d1-<yourname>-auto` (new) |
| Region | `<region>` |
| Managed identity | **System assigned** enabled |

2. After create: **Identity → System assigned → Azure role assignments → Add**.
3. Role: **Virtual Machine Contributor** (or Contributor) on `rg-d1-<yourname>` (scope of the VM you will stop).

✅ **Checkpoint:** Automation Account exists; identity can manage your lab VM RG.

---

## Part C — Create a runbook to deallocate a VM (15 min)

1. Automation Account → **Process Automation → Runbooks → Create a runbook**.
2. Name: `Stop-LabVM` · Runbook type: **PowerShell** · Create.
3. Edit and paste:

```powershell
param(
  [string]$ResourceGroupName = "rg-d1-<yourname>",
  [string]$VMName = "vm-d1-<yourname>-01"
)

Connect-AzAccount -Identity
Stop-AzVM -ResourceGroupName $ResourceGroupName -Name $VMName -Force
Write-Output "Requested deallocate for $VMName in $ResourceGroupName"
```

4. **Save → Publish**.
5. **Start** the runbook (use parameters if you parameterized names).
6. Open **Jobs** → watch output until Completed.
7. Confirm in portal: VM state is **Stopped (deallocated)**.

✅ **Checkpoint:** Runbook stopped your VM without using the VM blade.

---

## Part D — Schedule it (optional, 5 min)

1. Runbook → **Schedules → Add a schedule**.
2. Create schedule: e.g. daily at 20:00 local / training end time.
3. Link to `Stop-LabVM`.

Now lab VMs won’t burn money overnight if someone forgets.

---

## Part E — Cost + Automation takeaway

| Habit | Tool |
| ----- | ---- |
| See what costs money | Cost analysis + tags |
| Cap spending | Budgets + alerts |
| Recurring ops (start/stop) | Automation runbooks + schedules |
| Avoid secrets in scripts | Managed identity |

---

## Deliverables

- [ ] Reviewed Cost analysis  
- [ ] Automation Account + managed identity role  
- [ ] Published runbook deallocated a VM  
- [ ] (Optional) Schedule linked  

## Cleanup

```bash
az group delete -n rg-d1-<yourname>-auto --yes --no-wait
```

Start your VM again if you still need it for other labs.

---

## Done with Day 1 challenges?

Return to [Day 1 README](./README.md) · continue [Module labs](../README.md) · or [Azure DevOps course](../../../Azure-DevOps-6-Day-Course/).
