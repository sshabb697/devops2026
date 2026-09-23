# 01 — Grafana basics

**Learning objectives**

- Navigate Grafana UI: Home, Explore, Dashboards, Connections
- Use pre-provisioned **Prometheus** and **Loki** datasources
- Understand org, user, and folder (lab uses defaults)

---

## What Grafana is

Grafana is a **visualization and exploration** front end. It does not store metrics or logs itself — it queries backends.

```text
Grafana ──► Prometheus (metrics)
        └──► Loki (logs)
        └──► Azure Monitor (optional plugin / production)
```

Same UI for all — that is why teams love it.

---

## First login

1. http://localhost:3000
2. User `admin` / password `admin`
3. Set a new password (local lab only)

Our compose file mounts `grafana/provisioning/datasources/datasources.yml` so you skip manual datasource setup.

Verify: **Connections → Data sources** — **Prometheus** (default) and **Loki**.

---

## Explore vs Dashboard

| Explore | Dashboard |
| ------- | --------- |
| Ad-hoc queries | Saved panels for the team |
| Great for incidents | Great for daily health checks |
| One person | Shared on wall monitors |

Start in **Explore** during incidents; promote stable queries to **Dashboards**.

---

## Time range

Top-right clock controls all panels. During labs use **Last 15 minutes** or **Last 1 hour**.

If you see flat lines, widen the range or generate fresh logs/metrics.

---

## Knowledge check

1. Where are metrics stored in our lab?
2. Default datasource in provisioning file?
3. Explore or dashboard for “quick one-off query”?

<details>
<summary>Answers</summary>

1. Prometheus TSDB inside the Prometheus container.
2. Prometheus.
3. Explore.

</details>

➡️ Next: [02 — Dashboards and Explore](./02-Dashboards-and-Explore.md)
