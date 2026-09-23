# 01 — Prometheus architecture

**Learning objectives**

- Explain **pull** vs **push** for metrics
- Name Prometheus components: server, TSDB, scrape config, **Alertmanager** (optional)
- Read the **Targets** page

---

## What Prometheus is

Prometheus is an open source **metrics** database and scraper. It is the de facto standard in Kubernetes and many cloud-native stacks.

It answers: “What number changed over time, broken down by labels?”

---

## Pull model

```text
┌─────────────┐   HTTP GET /metrics   ┌──────────────┐
│ Prometheus  │ ────────────────────► │ node-exporter │
│  (scraper)  │ ◄──────────────────── │  (target)     │
└─────────────┘   text exposition     └──────────────┘
```

**Pull:** Prometheus visits targets on a schedule (`scrape_interval`).

**Push** (exceptions): short-lived jobs use **Pushgateway** — not day-one detail.

Azure Monitor is mostly **push/ingest** from agents — different transport, same golden signals.

---

## Data model

Each sample:

```text
metric_name{label="value"} 123.45 1710000000
```

Metric name + labels identify a **time series**.

---

## Components in our lab stack

| Piece | Role |
| ----- | ---- |
| `prometheus` | Scrapes and stores metrics |
| `node-exporter` | Exposes host CPU, memory, disk |
| `prometheus.yml` | Lists jobs and targets |

Grafana **queries** Prometheus; it does not scrape for you.

---

## Targets health

Open http://localhost:9090/targets

| State | Meaning |
| ----- | ------- |
| UP | Last scrape succeeded |
| DOWN | Network, wrong port, or target stopped |

Fix config before writing fancy queries.

---

## Retention

Prometheus stores data locally (TSDB). Default retention is limited — long-term storage uses remote write (out of scope for beginners).

---

## Knowledge check

1. Who initiates the HTTP request — Prometheus or the app?
2. What file lists scrape jobs in our lab?
3. Does Prometheus store logs?

<details>
<summary>Answers</summary>

1. Prometheus (pull).
2. `sample-stack/prometheus/prometheus.yml`.
3. No — use Loki for logs (Day 4).

</details>

➡️ Next: [02 — Metrics and PromQL](./02-Metrics-and-PromQL.md)
