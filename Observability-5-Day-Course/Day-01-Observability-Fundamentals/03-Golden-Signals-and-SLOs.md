# 03 — Golden signals and simple SLOs

**Learning objectives**

- Name the **four golden signals** (Google SRE)
- Relate **SLI**, **SLO**, and **SLA** without jargon overload
- Connect signals to Azure Monitor and Prometheus later this week

---

## Four golden signals

| Signal | Question | Example metric |
| ------ | -------- | -------------- |
| **Latency** | How long do requests take? | Response time p95 |
| **Traffic** | How much load? | Requests per second |
| **Errors** | How many fail? | HTTP 5xx rate |
| **Saturation** | How full is the system? | CPU, disk queue, thread pool |

If you only remember four things for dashboards, remember these.

---

## SLI, SLO, SLA (beginner)

| Term | Plain English | Example |
| ---- | ------------- | ------- |
| **SLI** | Something you measure | “Successful HTTP requests / total” |
| **SLO** | Target you aim for internally | “99.9% success over 30 days” |
| **SLA** | Contract with customers | “99.5% or we credit you” |

**SLO** drives alerting: burn error budget slowly → ticket; burn fast → page someone.

You do not need legal SLAs in lab — you need **clear numbers** so alerts mean something.

---

## Error budgets (one sentence)

If your SLO is 99.9% monthly, you can “spend” about 0.1% failures on deploys and experiments. Observability shows whether you are **burning budget too fast**.

---

## Alerting hygiene

Bad alert: “CPU > 50%” with no context — noisy.

Better alert: “HTTP 5xx rate > 1% for 5 minutes **and** traffic > baseline” — symptom-based.

Even better: tie to an SLO (“error budget burn rate high”).

You will create a **simple metric alert** on Azure in Day 2.

---

## Map to this week’s tools

| Signal | Azure Monitor | PLG stack |
| ------ | ------------- | --------- |
| Latency | App Insights, App Service metrics | Prometheus histograms, Grafana panels |
| Traffic | Request count metrics | `rate(http_requests_total[5m])` |
| Errors | Failed requests, exceptions | Counter + log `{level="ERROR"}` |
| Saturation | VM CPU, disk | `node_exporter` CPU / memory |

---

## Knowledge check

1. Name all four golden signals.
2. Which signal tells you “we need more servers soon”?
3. SLI vs SLO — which is the target?

<details>
<summary>Answers</summary>

1. Latency, traffic, errors, saturation.
2. Saturation (and sometimes latency rising under load).
3. SLO is the target; SLI is the measured indicator.

</details>

➡️ Lab: [Lab 01 — First look at logs and metrics](./Lab-01-First-Look-at-Logs-and-Metrics.md)
