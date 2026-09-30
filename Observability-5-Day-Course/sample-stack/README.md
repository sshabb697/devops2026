# Sample stack — observable application deployment

Local lab for **Days 3–5**. It deploys a small checkout API with Prometheus,
Loki, Grafana Alloy, and Grafana. Everything runs in Docker.

```text
checkout-api  <-- HTTP traffic --  load-generator
    |
    +-- /metrics <--- Prometheus ----> Grafana dashboard
    |
    +-- JSON log ---> Alloy ---> Loki ---> Grafana Explore
```

## Start

```bash
cd Observability-5-Day-Course/sample-stack
docker compose up -d
docker compose ps
```

Open **Grafana → Dashboards → Course Examples → Checkout Service Overview**.
The dashboard is provisioned automatically; no import is required.

| Service | URL |
| ------- | --- |
| Grafana | http://localhost:3000 (`admin` / `admin`) |
| Prometheus | http://localhost:9090 |
| Checkout API | http://localhost:8080 |
| Demo metrics | http://localhost:8080/metrics |
| Health endpoint | http://localhost:8080/health |
| Checkout endpoint | http://localhost:8080/checkout |
| Intentional error | http://localhost:8080/error |
| Alloy UI | http://localhost:12345 |
| Loki ready | http://localhost:3100/ready |

## Generate a healthy baseline

The traffic generator runs in Docker, so the command is the same in PowerShell,
Bash, and macOS terminals:

```bash
docker compose run --rm load-generator --requests 40 --interval-ms 100
```

It calls `/checkout`, which creates both Prometheus metrics and JSON logs. Wait
for one Prometheus scrape (up to 15 seconds), then inspect the dashboard.

## Generate an incident

Simulate a slow release where every fourth checkout returns HTTP 503:

```bash
docker compose run --rm load-generator --requests 60 --error-every 4 --delay-ms 600 --interval-ms 100
```

Expected evidence:

- request rate splits into HTTP `200` and `503`
- p95 checkout latency rises toward `1s`
- HTTP 5xx error rate rises toward `25%`
- Loki logs contain `level="ERROR"`, `status=503`, and the application version

## Useful queries

Grafana → **Explore**:

- Prometheus request rate: `sum by (status) (rate(demo_http_requests_total[1m]))`
- Prometheus p95 latency: `histogram_quantile(0.95, sum by (le) (rate(demo_http_request_duration_seconds_bucket{route="/checkout"}[5m])))`
- Loki errors: `{job="demo", service="checkout-api", level="ERROR"} | json`
- Loki slow requests: `{job="demo"} | json | duration_ms > 500`

Prometheus scrapes `demo-app:8080/metrics` (job `demo-app`) plus itself and
node-exporter. Alloy tails `logs/app.log`, parses JSON, and sends it to Loki.

## Simulate a versioned deployment

Bash:

```bash
APP_VERSION=2.0.0 docker compose up -d --force-recreate demo-app
```

PowerShell:

```powershell
$env:APP_VERSION = "2.0.0"
docker compose up -d --force-recreate demo-app
```

New logs carry `version="2.0.0"`. Reset the variable before recreating version
`1.0.0` (`unset APP_VERSION` in Bash or `Remove-Item Env:APP_VERSION` in
PowerShell).

## Stop

```bash
docker compose down
```

Add `-v` only if you want to wipe Grafana’s saved dashboards (this compose does not use a named volume by default).

## Files

| Path | Purpose |
| ---- | ------- |
| `docker-compose.yml` | Services and ports |
| `demo-app/server.py` | Checkout API, Prometheus metrics, JSON logs |
| `load-generator.py` | Repeatable healthy and failing traffic |
| `prometheus/prometheus.yml` | Scrape config |
| `loki/loki-config.yaml` | Single-node Loki |
| `alloy/config.alloy` | Tails JSON logs, extracts labels, pushes to Loki |
| `grafana/provisioning/datasources/datasources.yml` | Prometheus + Loki |
| `grafana/provisioning/dashboards/` | Course dashboard provider and JSON |
