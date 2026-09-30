# Observability Command Cheat Sheet

Commands for **class labs**. Azure Portal steps are in the day labs.

---

## Day 1 — Logs and metrics on a machine

| Command | What it does |
| ------- | ------------ |
| `journalctl -u nginx -n 50` | Last 50 lines for a systemd service |
| `journalctl -f` | Follow logs (Ctrl+C to stop) |
| `tail -f /var/log/syslog` | Follow a log file (path varies by distro) |
| `top` / `htop` | Live CPU/memory per process |
| `df -h` | Disk use |
| `free -h` | Memory summary |
| `curl -s -o /dev/null -w "%{http_code}\n" http://localhost/` | HTTP status code only |

---

## Day 2 — Azure CLI (Monitor basics)

| Command | What it does |
| ------- | ------------ |
| `az login` | Sign in |
| `az group create -n rg-obs-lab -l eastus` | Resource group for labs |
| `az monitor metrics list --resource <resource-id> --metric "Percentage CPU"` | CLI metrics sample |
| `az monitor activity-log list -g rg-obs-lab --offset 1d` | Recent control-plane events |

**KQL (Log Analytics)** — run in Portal → Logs:

```kql
AzureActivity
| where TimeGenerated > ago(1h)
| take 20
```

```kql
Perf
| where ObjectName == "Processor" and CounterName == "% Processor Time"
| summarize avg(CounterValue) by bin(TimeGenerated, 5m)
```

---

## Day 3 — Prometheus

| Command / URL | What it does |
| ------------- | ------------ |
| `docker compose up -d` | Start stack from `sample-stack/` |
| http://localhost:9090/targets | Scrape health |
| http://localhost:9090/graph | PromQL UI |

**PromQL starters:**

| Query | Meaning |
| ----- | ------- |
| `up` | 1 = target reachable, 0 = down |
| `node_cpu_seconds_total` | CPU time counters (needs node_exporter) |
| `rate(node_cpu_seconds_total[5m])` | Per-second rate over 5 minutes |
| `sum by (instance) (up)` | Up status grouped by instance |
| `sum by (status) (rate(demo_http_requests_total[1m]))` | Checkout request rate by HTTP status |
| `histogram_quantile(0.95, sum by (le) (rate(demo_http_request_duration_seconds_bucket[5m])))` | p95 request latency |

---

## Day 4 — Loki and Alloy

| Command / URL | What it does |
| ------------- | ------------ |
| http://localhost:3100/ready | Loki health |
| http://localhost:12345 | Alloy UI |
| http://localhost:8080 | Checkout API (writes a JSON log line) |
| http://localhost:8080/metrics | Prometheus metrics from the checkout API |
| http://localhost:8080/checkout | Healthy checkout request |
| http://localhost:8080/checkout?fail=true&delay_ms=600 | Slow HTTP 503 checkout |

**LogQL starters:**

| Query | Meaning |
| ----- | ------- |
| `{job="demo"}` | All streams with label `job=demo` |
| `{job="demo", level="ERROR"}` | Error streams using an indexed label |
| `{job="demo"} \| json \| duration_ms > 500` | Slow requests from parsed JSON |
| `sum by (version) (count_over_time({job="demo", level="ERROR"}[5m]))` | Errors by application version |

---

## Day 5 — Grafana

| Item | Notes |
| ---- | ----- |
| URL | http://localhost:3000 |
| Add Prometheus | Configuration → Data sources → Prometheus → URL `http://prometheus:9090` (from inside Compose network) or `http://host.docker.internal:9090` from host-only setups |
| Add Loki | URL `http://loki:3100` |
| Explore | Pick datasource → run PromQL or LogQL |
| Course dashboard | Dashboards → Course Examples → Checkout Service Overview |
| Community dashboard | New → Import → ID **1860** (Node Exporter Full) if node_exporter is running |

**Teardown:**

```bash
cd sample-stack
docker compose down
```

---

## Glossary (one line each)

| Term | Meaning |
| ---- | ------- |
| Metric | Number over time (CPU %, request count) |
| Log | Text event with timestamp |
| Trace | Path of one request across services |
| Scrape | Prometheus pulling metrics from a target |
| Label | Key/value that identifies a metric or log stream |
| Alert | Rule that notifies humans when something crosses a threshold |
