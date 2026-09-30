# Tutor notes (5 days)

## Before Day 1

- Students need a terminal (WSL on Windows is fine).
- No cloud required until Day 2.
- Set expectation: **observability is not “install a tool”** — it is questions you can answer when production misbehaves.

## Before Day 2

- Azure subscription + `az login`.
- Each student uses `rg-obs-<initials>` to avoid name clashes.
- If they have no VM/App Service, 15 minutes to deploy a **B1 Linux App Service** or reuse AZ-104 lab resources.

## Before Day 3

- Docker working: `docker compose version`.
- Pull images once on good Wi‑Fi: `cd sample-stack && docker compose pull`.
- Default Grafana password is `admin` — remind them to change it locally only.
- Start the stack once and confirm **Checkout Service Overview** appears under
	**Dashboards → Course Examples**.
- Run the healthy traffic command once so Prometheus and Loki are not empty at
	the start of class.

```bash
docker compose run --rm load-generator --requests 40 --interval-ms 100
```

## Teaching storyline for Days 3–5

Use the same checkout request throughout instead of unrelated tool demos:

1. **Day 3:** Prometheus shows request rate, HTTP status, and p95 latency.
2. **Day 4:** Alloy parses the request's JSON log and Loki filters by level,
	 version, status, and duration.
3. **Day 5:** Students deploy version `2.0.0`, generate a controlled incident,
	 correlate metrics with logs, roll back, and verify recovery.

Emphasize that `service`, `level`, and `version` are bounded labels. Keep
`duration_ms`, request IDs, and customer values in the JSON body to avoid Loki
stream-cardinality growth.

## Daily rhythm

1. Whiteboard the **question** (“Is the app slow or down?”) before the tool.
2. Labs — students click Portal and type commands; you do not drive every mouse click.
3. End of Day 2: optional `az group delete` if the RG was lab-only.
4. End of Day 5: `docker compose down` in `sample-stack`.

## Cost (Azure)

Metrics and Log Analytics ingestion can add up if students enable verbose diagnostics everywhere. Day 2 labs use **Metrics** and a **small KQL** sample — avoid turning on full VM Insights for the whole class unless budget allows.

## Common stalls

| Day | Stall | What you do |
| --- | ----- | ----------- |
| 1 | “Monitoring = observability” | Redirect to **unknown unknowns** — see Day 1 lesson |
| 2 | Empty Log Analytics | Wrong workspace linked to resource; pick workspace from resource **Diagnostic settings** |
| 2 | Alert never fires | Threshold too high; use a lab threshold that can fire once |
| 3 | All targets **DOWN** | Wrong service name in `prometheus.yml`; check `http://localhost:9090/targets` |
| 3 | PromQL `rate()` on gauge | Use `rate` on counters only; show `up` first |
| 3 | p95 panel has no data | Generate checkout traffic, wait one 15-second scrape, widen range to 15m |
| 4 | No logs in Loki | Alloy path wrong — `./logs` is mounted as `/var/log/demo` |
| 4 | JSON fields are missing | Expand a line, add `\| json`, and check `loki.process.demo` in the Alloy UI |
| 5 | Grafana “no data” | Time range, datasource URL, or Prometheus not scraping |
| 5 | Version remains `2.0.0` after rollback | Clear `APP_VERSION` in the current shell before recreating `demo-app` |
| 5 | Port 3000 in use | Change compose port mapping |

## Capstone grading (informal)

Student shows you:

1. Baseline, incident, and recovery screenshots from the Grafana dashboard.
2. One PromQL query proving impact and one LogQL query identifying version `2.0.0`.
3. A concise incident statement covering impact, affected version, rollback,
   and the signal used to verify recovery.

## Extra reading for you

- [Google SRE Book — Monitoring](https://sre.google/sre-book/monitoring-distributed-systems/)
- [Prometheus docs — first steps](https://prometheus.io/docs/prometheus/latest/getting_started/)
- [Grafana Loki docs](https://grafana.com/docs/loki/latest/)
- [Azure Monitor overview](https://learn.microsoft.com/azure/azure-monitor/overview)

Student links: [Resources/Useful-Links.md](./Resources/Useful-Links.md)
