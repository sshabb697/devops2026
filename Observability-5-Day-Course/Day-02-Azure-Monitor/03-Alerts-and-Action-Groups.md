# 03 — Alerts and action groups

**Learning objectives**

- Create an **action group** (email notification)
- Create a **metric alert rule**
- Describe **Activity log alerts** vs **metric alerts**

---

## Action group

An **action group** is *who to notify*:

- Email, SMS, voice
- Webhook, ITSM, Logic App
- Azure app push

Create once, reuse on many alert rules.

---

## Metric alert rule

Flow:

```text
Signal (metric) → Condition (threshold + duration) → Action group → Alert fired
```

Example: **Percentage CPU** > 80% for 5 minutes on a VM.

Symptom-based alerts align with **golden signals** (errors, latency) better than random CPU thresholds — but CPU is easy for a first lab.

---

## Activity log alerts

Use when you care about **management operations**:

- Delete resource group
- Stop VM
- Change NSG rule

Query table: **AzureActivity**. Good for security and “who broke prod?”

---

## Smart detection (awareness)

Application Insights includes **Smart Detection** for anomalies (failure rates, dependency issues). You do not configure every rule manually — know it exists so you are not surprised by auto-created alerts.

---

## Alert noise

| Problem | Fix |
| ------- | --- |
| Alert fires every night | Raise threshold or narrow hours |
| Alert never fires | Threshold too high; wrong resource |
| Too many emails | Route to ticket system; tune severity |

---

## Map to Prometheus (Day 3)

Prometheus **Alertmanager** routes firing alerts — same idea as action groups + alert rules, different UI.

---

## Knowledge check

1. Action group vs alert rule — which holds your email?
2. Name one metric alert and one activity log alert use case.
3. Why alert on HTTP 5xx instead of only CPU?

<details>
<summary>Answers</summary>

1. Action group holds notification targets; alert rule references it.
2. Metric: high CPU; Activity: resource deleted.
3. HTTP 5xx reflects user-visible errors; CPU can be high while users are fine (or vice versa).

</details>

➡️ Lab: [Lab 02 — Azure Monitor](./Lab-02-Azure-Monitor.md)
