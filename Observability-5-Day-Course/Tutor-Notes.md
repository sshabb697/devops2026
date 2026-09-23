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
| 4 | No logs in Loki | Alloy path wrong — `./logs` is mounted as `/var/log/demo` |
| 5 | Grafana “no data” | Time range, datasource URL, or Prometheus not scraping |
| 5 | Port 3000 in use | Change compose port mapping |

## Capstone grading (informal)

Student shows you:

1. One Grafana panel from **Prometheus** (metric).
2. One panel or Explore view from **Loki** (log line filter).
3. One sentence: “If this graph drops, I would check ___ first.”

## Extra reading for you

- [Google SRE Book — Monitoring](https://sre.google/sre-book/monitoring-distributed-systems/)
- [Prometheus docs — first steps](https://prometheus.io/docs/prometheus/latest/getting_started/)
- [Grafana Loki docs](https://grafana.com/docs/loki/latest/)
- [Azure Monitor overview](https://learn.microsoft.com/azure/azure-monitor/overview)

Student links: [Resources/Useful-Links.md](./Resources/Useful-Links.md)
