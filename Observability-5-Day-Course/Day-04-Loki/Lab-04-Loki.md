# Lab 04 — Loki and Alloy

**Time:** 60 minutes  
Folder: `Observability-5-Day-Course/sample-stack`

---

## Part A — Health checks (10 min)

```bash
cd Observability-5-Day-Course/sample-stack
docker compose up -d
curl -s http://localhost:3100/ready
docker compose logs alloy --tail 30
```

Expected: Loki prints `ready`. Alloy logs show no crash loop.

Open http://localhost:12345 — Alloy UI loads.

---

## Part B — Generate structured logs (15 min)

Run healthy traffic, then one intentional failure:

```bash
docker compose run --rm load-generator --requests 20 --interval-ms 100
docker compose run --rm load-generator --requests 4 --error-every 4 --delay-ms 600
```

Inspect the source file. Each line is a JSON object with the same fields:

```bash
docker compose exec demo-app tail -n 3 /logs/app.log
```

Look for `timestamp`, `level`, `service`, `version`, `route`, `status`, and
`duration_ms`.

Wait about 10 seconds. Alloy pushes new lines to Loki.

---

## Part C — Query in Grafana (20 min)

1. http://localhost:3000 → **Explore** → datasource **Loki**.
2. Show the stream: `{job="demo", service="checkout-api"}`
3. Use the indexed level label: `{job="demo", level="ERROR"}`
4. Parse fields and find slow requests:

```logql
{job="demo"} | json | duration_ms > 500
```

5. Find server failures by parsed status:

```logql
{job="demo"} | json | status >= 500
```

Expand a result and distinguish **stream labels** from **parsed fields**.

---

## Part D — Count lines (10 min)

```logql
sum by (version) (count_over_time({job="demo", level="ERROR"}[10m]))
```

Run failing traffic again. The count for version `1.0.0` goes up.

---

## Part E — Stop Alloy (5 min)

```bash
docker compose stop alloy
docker compose run --rm load-generator --requests 5
```

The new line is in `logs/app.log` but **not** in Grafana yet.

```bash
docker compose start alloy
```

Wait, then refresh Explore. The line appears. Path: **app file → Alloy → Loki → Grafana**.

---

## Deliverables

- [ ] ERROR filter shows the failed checkout line
- [ ] A slow-request query returns `duration_ms > 500`
- [ ] You can say Alloy discovers and parses; Loki stores; Grafana queries

➡️ Tomorrow: [Day 5 — Grafana and capstone](../Day-05-Grafana-and-Capstone/README.md)
