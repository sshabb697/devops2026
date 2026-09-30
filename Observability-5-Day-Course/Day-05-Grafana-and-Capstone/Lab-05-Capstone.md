# Lab 05 — Capstone: investigate a bad application deployment

**Time:** 90 minutes

You will establish a healthy baseline, deploy version `2.0.0`, generate a
checkout incident, prove the affected release with **metrics + logs**, and
verify a rollback.

---

## Scenario

**Story:** Customers report slow and failed checkouts after version `2.0.0` was
released. Determine the impact, identify the affected version, and recommend a
rollback using evidence rather than timing alone.

---

## Part A — Deploy and baseline (15 min)

From `Observability-5-Day-Course/sample-stack`:

```bash
docker compose up -d
docker compose run --rm load-generator --requests 40 --interval-ms 100
```

Wait up to 15 seconds, then open **Grafana → Dashboards → Course Examples →
Checkout Service Overview**. Set the time range to **Last 15 minutes**.

Record the healthy baseline:

| Signal | Baseline observation |
| ------ | -------------------- |
| Request status | |
| Checkout p95 latency | |
| HTTP 5xx error rate | |
| Current version from logs | |

✅ **Checkpoint:** The dashboard uses Prometheus and Loki and mostly shows HTTP 200.

---

## Part B — Deploy version 2.0.0 (15 min)

Use the command for your shell.

**Bash:**

```bash
APP_VERSION=2.0.0 docker compose up -d --force-recreate demo-app
```

**PowerShell:**

```powershell
$env:APP_VERSION = "2.0.0"
docker compose up -d --force-recreate demo-app
```

Generate slow traffic with a predictable 25% failure rate:

```bash
docker compose run --rm load-generator --requests 60 --error-every 4 --delay-ms 600 --interval-ms 100
```

Wait for the next Prometheus scrape, then refresh the dashboard.

✅ **Checkpoint:** HTTP 503, p95 latency, and 5xx error rate all rise.

---

## Part C — Investigate in Explore (25 min)

### 1. Quantify impact with Prometheus

```promql
sum by (status) (rate(demo_http_requests_total[1m]))
```

```promql
100 *
sum(rate(demo_http_requests_total{status=~"5.."}[5m]))
/
clamp_min(sum(rate(demo_http_requests_total[5m])), 0.001)
```

```promql
histogram_quantile(
   0.95,
   sum by (le) (
      rate(demo_http_request_duration_seconds_bucket{route="/checkout"}[5m])
   )
)
```

### 2. Identify the release with Loki

```logql
{job="demo", level="ERROR", version="2.0.0"} | json
```

Find slow checkout requests from the same version:

```logql
{job="demo", version="2.0.0"} | json | route="/checkout" | duration_ms > 500
```

Count errors by version:

```logql
sum by (version) (count_over_time({job="demo", level="ERROR"}[5m]))
```

✅ **Checkpoint:** Both metrics and logs show user impact; logs identify version `2.0.0`.

---

## Part D — Decide and roll back (20 min)

Complete the incident record before changing the system:

| Question | Your evidence-based answer |
| -------- | -------------------------- |
| What was the user-visible symptom? | |
| What was the approximate 5xx percentage? | |
| Which version produced the errors? | |
| Did latency and errors change together? | |
| Why is rollback safer than scaling in this scenario? | |

Reset the version and recreate the application.

**Bash:**

```bash
unset APP_VERSION
docker compose up -d --force-recreate demo-app
```

**PowerShell:**

```powershell
Remove-Item Env:APP_VERSION
docker compose up -d --force-recreate demo-app
```

Generate healthy traffic:

```bash
docker compose run --rm load-generator --requests 40 --interval-ms 100
```

Verify that new logs show version `1.0.0`, new requests return `200`, and the
error rate falls as the five-minute query window moves forward.

✅ **Checkpoint:** You can distinguish recovery from historical errors still inside the query window.

---

## Part E — Azure connection (optional)

If you completed Day 2:

1. Open the **metric alert** you created.
2. Identify the Azure metric or Application Insights table that would show the same 5xx symptom.
3. Compare alert notification in Azure with investigation in Grafana.

No Azure? Write two sentences on how you **would** wire Azure Monitor as a Grafana datasource in production (conceptual).

---

## Part F — Cleanup (5 min)

```bash
docker compose down
```

Optional: delete `rg-obs-<yourname>` if it was lab-only.

---

## Deliverables (present to instructor)

1. Dashboard screenshots before failure, during failure, and after rollback.
2. Completed incident record with one PromQL and one LogQL query as evidence.
3. **30-second incident summary:** impact, affected version, action, and recovery signal.

---

## Bonus

- Add a Grafana alert when the 5xx percentage is above 5% for two minutes.
- Add a dashboard variable for the Loki `version` label.
- Read [Resources/Useful-Links.md](../Resources/Useful-Links.md) and pick one cert or doc to continue.

**Congratulations — you finished the Observability 5-Day Course.**
