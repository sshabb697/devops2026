# 02 — Dashboards and Explore

**Learning objectives**

- Build a panel from PromQL and from LogQL
- Import a community dashboard safely
- Use variables (introduction)

---

## Panel from Prometheus

1. **Dashboards → New → New dashboard → Add visualization**
2. Datasource: **Prometheus**
3. Query:

```promql
100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)
```

4. Panel title: **CPU busy %**
5. Save dashboard as **Obs Lab — Metrics**

---

## Panel from Loki

Add second panel:

1. **Add → Visualization**
2. Datasource: **Loki**
3. Query:

```logql
sum(count_over_time({job="demo"} |= "ERROR" [5m]))
```

4. Title: **ERROR log lines (5m)**

Save dashboard again.

---

## Import dashboard (optional)

Community dashboards assume specific exporters.

1. **Dashboards → New → Import**
2. ID **1860** (Node Exporter Full) — works if `node-exporter` is UP
3. Select Prometheus datasource when asked

Review imported queries before trusting them in production.

---

## Variables (preview)

Edit dashboard settings → **Variables**:

- Name: `job`
- Type: Query
- Datasource Prometheus
- Query: `label_values(up, job)`

Use `$job` in queries: `up{job="$job"}`.

Skip if time is short — concept only.

---

## Annotations (awareness)

Mark deploy times on graphs (vertical lines). Helps correlate latency spikes with releases.

---

## Knowledge check

1. Can one dashboard mix Prometheus and Loki panels?
2. Why review imported dashboard queries?
3. What golden signal is ERROR log count closest to?

<details>
<summary>Answers</summary>

1. Yes — each panel picks its datasource.
2. They may reference metrics you do not expose or wrong job names.
3. Errors.

</details>

➡️ Next: [03 — Unified observability](./03-Unified-Observability.md)
