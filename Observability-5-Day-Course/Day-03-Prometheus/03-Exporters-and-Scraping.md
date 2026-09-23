# 03 — Exporters and scraping

**Learning objectives**

- Define an **exporter**
- Edit `prometheus.yml` safely and reload
- Know where application metrics come from in real apps

---

## Exporters

Programs that expose `/metrics` in Prometheus text format.

| Exporter | Metrics |
| -------- | ------- |
| **node_exporter** | CPU, memory, disk, network (host) |
| **mysql_exporter** | Database stats |
| **blackbox_exporter** | Probe URLs from outside |

Our compose file runs **node_exporter** as service `node-exporter:9100`.

---

## Scrape config (lab file)

```yaml
scrape_configs:
  - job_name: node
    static_configs:
      - targets: ["node-exporter:9100"]
```

- **job_name** becomes label `job="node"`.
- **targets** must be reachable **from Prometheus container** (Docker DNS name).

---

## Add a second target (exercise)

Duplicate the job block with a wrong target on purpose:

```yaml
      - targets: ["node-exporter:9199"]
```

Reload Prometheus:

```bash
docker compose exec prometheus kill -HUP 1
```

Or restart: `docker compose restart prometheus`

Check **Targets** — one UP, one DOWN. Fix the port back to `9100`.

---

## Application metrics

Production apps often:

- Use a **client library** (Go, Java, .NET) to expose `/metrics`
- Or sidecar with an exporter

You expose **business metrics** (orders placed) the same way as CPU — counters and histograms with labels.

---

## Alertmanager (awareness)

Prometheus evaluates **alert rules** and sends firing alerts to **Alertmanager** for routing (silence, group, notify). Azure action groups play a similar role.

---

## Knowledge check

1. Default path exporters expose?
2. Why use Docker service name in `targets`?
3. job_name shows up as which label?

<details>
<summary>Answers</summary>

1. `/metrics`.
2. Prometheus runs inside Compose network — `localhost` would mean the Prometheus container itself.
3. `job`.

</details>

➡️ Lab: [Lab 03 — Prometheus](./Lab-03-Prometheus.md)
