# 02 — Log Analytics and KQL

**Learning objectives**

- Run a **KQL** query in the Portal
- Use `where`, `project`, `summarize`, and `take`
- Read results from **AzureActivity** and **Perf** tables

---

## Open Logs

1. Portal → **Monitor** → **Logs**.
2. If prompted, pick a **Log Analytics workspace** (create one in the lab if needed).
3. Close sample queries — you will type your own.

KQL reads top to bottom like a pipeline:

```kql
TableName
| where TimeGenerated > ago(24h)
| take 10
```

---

## Query 1 — Recent control-plane events

```kql
AzureActivity
| where TimeGenerated > ago(1d)
| project TimeGenerated, OperationName, ActivityStatus, Caller, ResourceGroup
| order by TimeGenerated desc
| take 20
```

**What you learn:** who did what to Azure resources (not inside the VM OS).

---

## Query 2 — VM CPU (if VM sends Perf data)

```kql
Perf
| where ObjectName == "Processor"
| where CounterName == "% Processor Time"
| where InstanceName == "_Total"
| summarize AvgCPU = avg(CounterValue) by bin(TimeGenerated, 5m)
| order by TimeGenerated desc
```

If empty: your VM may not have **Azure Monitor Agent** / diagnostics — use **Metrics** blade for CPU in the lab instead.

---

## Query 3 — Filter and search

```kql
AzureActivity
| where OperationName has "write"
| where ActivityStatus == "Succeeded"
| summarize count() by ResourceGroup
```

| Operator | Meaning |
| -------- | ------- |
| `\|` | Pipe to next step |
| `where` | Filter rows |
| `project` | Choose columns |
| `summarize` | Aggregate |
| `ago(1h)` | Time window |
| `bin(TimeGenerated, 5m)` | 5-minute buckets |

---

## KQL vs LogQL (preview)

Later this week **Loki** uses **LogQL**. Both filter label/key fields then aggregate. KQL is richer for Azure tables; LogQL is optimized for log streams `{job="demo"}`.

---

## Knowledge check

1. What does `take 10` do?
2. Why use `bin(TimeGenerated, 5m)`?
3. AzureActivity vs Perf — which is guest OS CPU?

<details>
<summary>Answers</summary>

1. Returns only 10 rows after previous steps.
2. Groups metrics into 5-minute time buckets for charts.
3. Perf (when agent installed); AzureActivity is control-plane audit.

</details>

➡️ Next: [03 — Alerts and action groups](./03-Alerts-and-Action-Groups.md)
