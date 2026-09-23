# 02 — Metrics and PromQL

**Learning objectives**

- Run queries in the Prometheus **Graph** UI
- Use `up`, `rate()`, and label matchers
- Avoid common beginner mistakes with counter vs gauge

---

## Open the UI

http://localhost:9090/graph

Start the stack if needed:

```bash
cd Observability-5-Day-Course/sample-stack
docker compose up -d
```

---

## Query 1 — `up`

```promql
up
```

| Value | Meaning |
| ----- | ------- |
| 1 | Target healthy |
| 0 | Scrape failed |

Add labels:

```promql
up{job="node"}
```

---

## Query 2 — instant vs range

- **Instant query:** value at one timestamp (Graph tab executes instant by default).
- **Range query:** `[5m]` window for functions like `rate`.

```promql
rate(node_cpu_seconds_total[5m])
```

`node_cpu_seconds_total` is a **counter** (CPU seconds accumulated). `rate` converts to per-second speed.

---

## Query 3 — aggregation

```promql
sum by (mode) (rate(node_cpu_seconds_total[5m]))
```

Groups CPU time by mode (user, system, idle, …).

---

## Matchers

| Syntax | Meaning |
| ------ | ------- |
| `metric{job="node"}` | label equals |
| `metric{job!="prometheus"}` | not equal |
| `metric{mode=~"idle\|iowait"}` | regex |

---

## Beginner mistakes

| Mistake | Fix |
| ------- | --- |
| `rate()` on a gauge | Use `rate` on counters only |
| No data | Check time range; check targets UP |
| Huge cardinality | Too many unique label combos — simplify labels |

---

## PromQL vs KQL

Both aggregate time-based data. PromQL is built for Prometheus text metrics; KQL fits Azure tables. Grafana can query both.

---

## Knowledge check

1. What type is `node_cpu_seconds_total`?
2. What does `rate(...[5m])` approximate?
3. Why is `up` a good first alert?

<details>
<summary>Answers</summary>

1. Counter.
2. Per-second increase averaged over the last 5 minutes.
3. It directly means Prometheus cannot scrape — target down or misconfigured.

</details>

➡️ Next: [03 — Exporters and scraping](./03-Exporters-and-Scraping.md)
