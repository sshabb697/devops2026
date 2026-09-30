# 02 — Dashboards and Explore

**Learning objectives**

- Build a panel from PromQL and from LogQL
- Read and modify a provisioned service dashboard
- Import a community dashboard safely
- Use variables (introduction)

---

## Start with the reference dashboard

Open **Dashboards → Course Examples → Checkout Service Overview**. It is
provisioned from `sample-stack/grafana/provisioning/dashboards/` and contains:

| Panel | Datasource | Signal |
| ----- | ---------- | ------ |
| Request rate by status | Prometheus | Rate and errors |
| Checkout p95 latency | Prometheus | Duration |
| HTTP 5xx error rate | Prometheus | Errors |
| Application logs | Loki | Request context |

Generate data if the panels are empty:

```bash
docker compose run --rm load-generator --requests 40 --error-every 5 --delay-ms 300
```

Open each panel menu → **Edit** and read its query before building your own.

---

## Panel from Prometheus

1. **Dashboards → New → New dashboard → Add visualization**
2. Datasource: **Prometheus**
3. Query:

```promql
sum by (status) (rate(demo_http_requests_total[1m]))
```

4. Panel title: **Checkout request rate**
5. Save dashboard as **Obs Lab — Metrics**

---

## Panel from Loki

Add second panel:

1. **Add → Visualization**
2. Datasource: **Loki**
3. Query:

```logql
sum by (version) (count_over_time({job="demo", level="ERROR"}[5m]))
```

4. Title: **ERROR logs by version**

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

Mark deploy times on graphs (vertical lines). In production, deployment
pipelines can write annotations automatically so operators can correlate a
signal change with a release without guessing.

---

## Knowledge check

1. Can one dashboard mix Prometheus and Loki panels?
2. Why review imported dashboard queries?
3. Why group errors by application version?

<details>
<summary>Answers</summary>

1. Yes — each panel picks its datasource.
2. They may reference metrics you do not expose or wrong job names.
3. To see whether failures started or increased with a particular release.

</details>

➡️ Next: [03 — Unified observability](./03-Unified-Observability.md)
