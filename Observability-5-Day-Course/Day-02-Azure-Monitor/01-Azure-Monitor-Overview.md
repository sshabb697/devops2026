# 01 — Azure Monitor overview

**Learning objectives**

- Navigate **Azure Monitor** in the Portal
- Name the parts: **metrics**, **logs**, **Activity log**, **Application Insights**
- Connect Day 1 golden signals to Azure blades

---

## What Azure Monitor is

Azure Monitor is Microsoft’s **platform observability** service. It collects:

- **Platform metrics** — CPU, disk, HTTP errors (automatic for many resources)
- **Resource logs** — diagnostic logs you enable per service
- **Activity log** — who created, changed, or deleted resources (control plane)
- **Application telemetry** — via **Application Insights** (app-level metrics, traces, exceptions)

Think of it as “observe Azure and apps running on Azure.”

---

## Portal map

```text
Azure Portal
└── Monitor
    ├── Metrics          → charts (golden signals)
    ├── Logs             → Log Analytics / KQL
    ├── Alerts           → rules + action groups
    ├── Activity log     → subscription operations
    └── Workbooks        → combined views (optional)
```

From any resource (VM, App Service, storage):

**Monitoring → Metrics** and **Monitoring → Logs** are the same data, scoped to that resource.

---

## Log Analytics workspace

**Logs** live in a **Log Analytics workspace** (a database for KQL queries).

- Some resources **send** logs to a workspace when you enable **Diagnostic settings**.
- Without a workspace link, **Logs** may be empty even though **Metrics** work.

You will query the workspace in the next lesson.

---

## Application Insights (app lens)

For code you own (web APIs, functions):

- Automatic request counts, failures, dependencies
- **Live Metrics** for quick debugging
- **Distributed tracing** (maps to the “traces” pillar)

Link an App Insights resource to your app (SDK or auto-instrumentation). Day 2 lab uses **platform metrics**; App Insights is the stretch goal if you already deployed an app in AZ-104 or DevOps course.

---

## Metrics vs logs in Azure

| | Metrics | Logs |
| - | ------- | ---- |
| Cost model | Cheaper at scale for trends | Richer; ingestion priced per GB |
| Query | Metrics explorer, limited dimensions | Full **KQL** |
| Best for | Alerts on CPU, HTTP 5xx | “Show me exception stack traces” |

---

## Knowledge check

1. Where do you see **who deleted a resource**?
2. Why might Metrics work but Logs be empty?
3. Which service adds request-level tracing for your code?

<details>
<summary>Answers</summary>

1. Activity log (and often AzureActivity table in Log Analytics).
2. Diagnostic settings not sending logs to a workspace.
3. Application Insights.

</details>

➡️ Next: [02 — Log Analytics and KQL](./02-Log-Analytics-and-Queries.md)
