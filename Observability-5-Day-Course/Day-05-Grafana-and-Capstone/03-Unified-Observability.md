# 03 — Unified observability

**Learning objectives**

- Tie **Azure Monitor**, **Prometheus**, **Loki**, and **Grafana** into one story
- Describe a simple incident workflow across tools
- Know sensible **next steps** after this course

---

## Two worlds, one workflow

| Step | Azure (Day 2) | PLG (Days 3–5) |
| ---- | ------------- | -------------- |
| Is user impact? | App Insights / App Service 5xx | `rate()` on HTTP counters, Loki ERROR logs |
| Is infrastructure saturated? | VM CPU metric | node_exporter + Grafana |
| Who changed config? | Activity log / AzureActivity | Git + CI logs (often Loki) |
| Dashboard | Azure workbooks or Grafana AMG | Self-hosted Grafana |

Many enterprises run **Grafana on Azure** with datasources for Monitor, Prometheus, and Loki.

---

## Example incident narrative

1. **Alert** fires: HTTP 5xx rate high (Azure metric alert or Grafana alert).
2. Open **Grafana dashboard** — latency and errors up; CPU normal.
3. **Explore → Loki** — `{app="api"} |= "timeout"` spikes after 14:05.
4. **Azure Activity log** — no infra changes; check **deployment pipeline** at 14:04.
5. Roll back release; watch metrics return green.

Observability is the **thread** between tools.

---

## Traces and beyond

When logs and metrics are not enough:

- **Application Insights** application map
- **Grafana Tempo** or **Jaeger** for traces
- **OpenTelemetry** as one SDK to export all three signals

---

## Cost and retention hygiene

- Sample debug logs in prod
- Keep label cardinality low
- Set retention on Loki and Prometheus; archive to storage if required
- Use Azure **budget alerts** on Log Analytics ingestion

---

## What's next in this repo

| Goal | Course |
| ---- | ------ |
| Run workloads that expose metrics | [Kubernetes 10-Day](../Kubernetes-10-Day-Course/) |
| Automate Azure monitoring as code | [Terraform 5-Day](../Terraform-5-Day-Course/) |
| CI/CD and deployment markers | [Azure DevOps 6-Day](../Azure-DevOps-6-Day-Course/) |

---

## Knowledge check

1. Name all four tools you used this week (plus Azure Monitor).
2. Why check Activity log during an app-only outage?
3. One reason to adopt OpenTelemetry?

<details>
<summary>Answers</summary>

1. Azure Monitor, Prometheus, Loki, Grafana (+ **Alloy** as the log shipper).
2. Rule out someone stopping VM or changing firewall; narrows blame.
3. Single instrumentation for metrics, logs, and traces to many backends.

</details>

➡️ Capstone: [Lab 05 — Capstone](./Lab-05-Capstone.md)
