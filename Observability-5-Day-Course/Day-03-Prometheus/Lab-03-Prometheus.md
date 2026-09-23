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
3. Open http://localhost:8080/metrics — you should see `demo_requests_total`.

If DOWN: `docker compose logs prometheus` and check `prometheus/prometheus.yml`.

In Graph, also try:

```promql
demo_requests_total
```

Refresh http://localhost:8080 a few times and run the query again. The number should rise.

✅ **Checkpoint:** Screenshot of all targets UP.

---

## Part C — PromQL (25 min)

In **Graph**, run each query and note what you see:

```promql
up
```

```promql
rate(node_cpu_seconds_total{mode="idle"}[5m])
```

```promql
100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)
```

Last query approximates **CPU busy %** (lab math — good enough for learning).

Switch time range to **1h** if the graph looks flat.

✅ **Checkpoint:** You explain what `rate` does in one sentence.

---

## Part D — Raw metrics (10 min)

```bash
curl -s http://localhost:9100/metrics | head -n 30
```

Find one line starting with `# HELP` and one counter line.

✅ **Checkpoint:** You match a line from curl to a name in the Prometheus UI dropdown.

---

## Part E — Break and fix (5 min)

1. Stop node exporter: `docker compose stop node-exporter`
2. Reload targets page — **node** should go DOWN.
3. Start it: `docker compose start node-exporter`

✅ **Checkpoint:** You saw `up{job="node"}` drop to 0 then return to 1.

---

## Deliverables

- Screenshot: CPU busy graph + targets page.
- Written answer: pull vs push in your own words.

➡️ Tomorrow: [Day 4 — Loki](../Day-04-Loki/README.md)
