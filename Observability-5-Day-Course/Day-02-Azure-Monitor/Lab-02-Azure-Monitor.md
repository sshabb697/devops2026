# Lab 02 — Azure Monitor

**Time:** 60–90 minutes  
**Goal:** Chart metrics, run KQL, create an action group and metric alert.

## Prerequisites

- `az login`
- Resource group `rg-obs-<yourname>` (create below if needed)
- At least one resource: **Linux VM**, **App Service**, or **Storage account**

---

## Part A — Resource group (10 min)

```bash
az group create --name rg-obs-<yourname> --location eastus
```

Deploy or reuse any small resource in that group.

✅ **Checkpoint:** Resource visible in Portal under the RG.

---

## Part B — Metrics chart (15 min)

1. Open your resource → **Monitoring → Metrics**.
2. Add a chart:
   - **VM:** Percentage CPU
   - **App Service:** Http Server Errors or Response Time
   - **Storage:** Availability or Success E2E Latency
3. Set time range **Last 1 hour**.
4. Optional: **Pin to dashboard**.

✅ **Checkpoint:** Screenshot of a metric chart with a title you understand.

---

## Part C — Log Analytics query (20 min)

1. **Monitor → Logs** (select or create workspace in the same RG).
2. Run:

```kql
AzureActivity
| where ResourceGroup == "rg-obs-<yourname>"
| where TimeGenerated > ago(7d)
| project TimeGenerated, OperationName, Caller, ActivityStatus
| order by TimeGenerated desc
| take 25
```

3. Save query as **Obs-Lab-Activity** (optional).

✅ **Checkpoint:** You see your own create/deploy operations.

---

## Part D — Action group (10 min)

1. **Monitor → Alerts → Action groups → Create**.
2. Name: `ag-obs-<yourname>` · Display name: `ObsLabNotify`.
3. **Email** → your address → enable.
4. Create.

✅ **Checkpoint:** Action group lists your email.

---

## Part E — Metric alert (20 min)

1. **Monitor → Alerts → Create → Alert rule**.
2. **Scope:** your VM / App Service / storage account.
3. **Condition:** pick a signal you charted in Part B.  
   Lab-friendly threshold: CPU **>** 1% for 1 minute (may fire — that is OK) or Http 5xx **>** 0 if you can generate a test error.
4. **Actions:** select `ag-obs-<yourname>`.
5. Name: `alert-obs-<yourname>-metric`.
6. Create.

✅ **Checkpoint:** Alert rule appears under **Alert rules**.

---

## Part F — Activity log (10 min)

1. Open `rg-obs-<yourname>` → **Activity log**.
2. Find a **Create** or **Write** operation you performed today.
3. Note **Caller** and **Status**.

Optional alert: **Monitor → Alerts** → signal type **Activity log** → operation **Delete resource** (do not delete prod — discussion only).

✅ **Checkpoint:** You explain one Activity log row in plain English.

---

## Deliverables

- Screenshot: Metrics chart + KQL results.
- One sentence: which **golden signal** your alert protects.

➡️ Tomorrow: [Day 3 — Prometheus](../Day-03-Prometheus/README.md)
