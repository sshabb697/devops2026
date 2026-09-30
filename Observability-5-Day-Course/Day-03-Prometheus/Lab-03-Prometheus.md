# Lab 03 — Prometheus

**Time:** 60 minutes

---

## Part A — Start stack (10 min)

```bash
cd Observability-5-Day-Course/sample-stack
docker compose up -d
docker compose ps
curl -s http://localhost:9090/-/healthy
```

Expected: `Prometheus Server is Healthy.`

---

## Part B — Targets (10 min)

1. Open http://localhost:9090/targets
2. Confirm jobs **prometheus**, **node**, and **demo-app** are **UP**.
3. Open http://localhost:8080/metrics — you should see `demo_up`.

If DOWN: `docker compose logs prometheus` and check `prometheus/prometheus.yml`.

In Graph, also try:

```promql
demo_up
```

Generate realistic checkout traffic:

```bash
docker compose run --rm load-generator --requests 40 --interval-ms 100
```

Wait up to 15 seconds for the next scrape, then query:

```promql
sum by (status) (demo_http_requests_total)
```

The total should rise and status `200` should be present.

✅ **Checkpoint:** Screenshot of all targets UP.

---

## Part C — PromQL (25 min)

In **Graph**, run each query and note what you see:

```promql
up
```

```promql
sum by (status) (rate(demo_http_requests_total[1m]))
```

```promql
histogram_quantile(
	0.95,
	sum by (le) (
		rate(demo_http_request_duration_seconds_bucket{route="/checkout"}[5m])
	)
)
```

These are two RED signals: **rate** and **duration**. Generate slow traffic and
run the p95 query again:

```bash
docker compose run --rm load-generator --requests 30 --delay-ms 600 --interval-ms 100
```

Switch time range to **1h** if the graph looks flat.

✅ **Checkpoint:** You explain why a counter needs `rate()` and what p95 means.

---

## Part D — Raw metrics (10 min)

```bash
curl -s http://localhost:9100/metrics | head -n 30
```

Find one line starting with `# HELP` and one `node_` counter line.

✅ **Checkpoint:** You match a line from curl to a name in the Prometheus UI dropdown.

---

## Part E — Break and fix (5 min)

1. Stop node exporter: `docker compose stop node-exporter`
2. Reload targets page — **node** should go DOWN.
3. Start it: `docker compose start node-exporter`

✅ **Checkpoint:** You saw `up{job="node"}` drop to 0 then return to 1.

---

## Deliverables

- Screenshot: checkout request rate, p95 latency, and targets page.
- Written answer: pull vs push in your own words.

➡️ Tomorrow: [Day 4 — Loki](../Day-04-Loki/README.md)
