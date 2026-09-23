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

## Part B — Generate logs (15 min)

The demo app writes `logs/app.log` for you:

```bash
curl -s http://localhost:8080/
curl -s http://localhost:8080/
curl -s http://localhost:8080/error
```

Or open those URLs in a browser.

Wait about 10 seconds. Alloy pushes new lines to Loki.

---

## Part C — Query in Grafana (20 min)

1. http://localhost:3000 → **Explore** → datasource **Loki**.
2. Query: `{job="demo"}`
3. Query: `{job="demo"} |= "ERROR"`

You should see `payment timeout` from `/error`.

---

## Part D — Count lines (10 min)

```logql
sum(count_over_time({job="demo"}[10m]))
```

Hit `/` again. Run the query again. The number goes up.

---

## Part E — Stop Alloy (5 min)

```bash
docker compose stop alloy
curl -s http://localhost:8080/
```

The new line is in `logs/app.log` but **not** in Grafana yet.

```bash
docker compose start alloy
```

Wait, then refresh Explore. The line appears. Path: **app file → Alloy → Loki → Grafana**.

---

## Deliverables

- [ ] ERROR filter shows the payment line
- [ ] You can say Alloy pushes; Loki stores; Grafana queries

➡️ Tomorrow: [Day 5 — Grafana and capstone](../Day-05-Grafana-and-Capstone/README.md)
