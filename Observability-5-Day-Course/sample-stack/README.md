# Sample stack — Prometheus, Loki, Alloy, Grafana

Local lab for **Days 3–5**. Everything runs in Docker.

```text
demo-app  --metrics-->  Prometheus  -->  Grafana
    |                                      ^
    +-- log file -->  Alloy  -->  Loki  ---+
```

## Start

```bash
cd Observability-5-Day-Course/sample-stack
docker compose up -d
docker compose ps
```

| Service | URL |
| ------- | --- |
| Grafana | http://localhost:3000 (`admin` / `admin`) |
| Prometheus | http://localhost:9090 |
| Demo app | http://localhost:8080 |
| Demo metrics | http://localhost:8080/metrics |
| Demo error log | http://localhost:8080/error |
| Alloy UI | http://localhost:12345 |
| Loki ready | http://localhost:3100/ready |

## Make data

Open the demo app a few times (browser or `curl http://localhost:8080/`). Each hit appends `logs/app.log`. Alloy ships that file to Loki.

Prometheus scrapes `demo-app:8080/metrics` (job `demo-app`) plus itself and node-exporter.

Grafana → **Explore**:

- Prometheus: `demo_requests_total`
- Loki: `{job="demo"}`

## Stop

```bash
docker compose down
```

Add `-v` only if you want to wipe Grafana’s saved dashboards (this compose does not use a named volume by default).

## Files

| Path | Purpose |
| ---- | ------- |
| `docker-compose.yml` | Services and ports |
| `demo-app/server.py` | Hello page, `/metrics`, log lines |
| `prometheus/prometheus.yml` | Scrape config |
| `loki/loki-config.yaml` | Single-node Loki |
| `alloy/config.alloy` | Tails `./logs/*.log` and pushes to Loki |
| `grafana/provisioning/datasources/datasources.yml` | Prometheus + Loki |
