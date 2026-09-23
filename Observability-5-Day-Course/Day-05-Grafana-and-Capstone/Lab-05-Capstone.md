# Lab 05 — Capstone: observe a failing service

**Time:** 90 minutes

You will simulate an incident on the lab stack, investigate with **metrics + logs**, document findings, and optionally connect to **Azure Monitor**.

---

## Scenario

**Story:** Checkout errors spiked after a “deploy.” You must prove whether the problem is **saturation** (CPU) or **application errors** (logs).

---

## Part A — Baseline dashboard (20 min)

1. Ensure stack is up: `docker compose up -d` in `sample-stack/`.
2. Create dashboard **Obs Capstone** with:
   - **Stat or gauge:** CPU busy % (Prometheus query from Day 5 lesson)
   - **Time series:** `up{job="node"}`
   - **Logs panel or stat:** LogQL count of `{job="demo"} |= "ERROR"` over 5m
3. Save and snapshot the healthy state (screenshot).

✅ **Checkpoint:** Three panels, two datasources.

---

## Part B — Simulate deploy + failure (15 min)

Append logs as if a bad release happened:

```bash
echo "$(date -Iseconds) INFO deploy version=2.0.0" >> logs/app.log
for i in 1 2 3 4 5; do echo "$(date -Iseconds) ERROR checkout failed code=503" >> logs/app.log; done
echo "$(date -Iseconds) WARN retry storm detected" >> logs/app.log
```

Optional load (WSL/Linux) to bump CPU briefly:

```bash
stress --cpu 2 --timeout 30s
```

If `stress` is missing, skip — logs alone are enough for the story.

✅ **Checkpoint:** ERROR count panel rises; note whether CPU panel moved much.

---

## Part C — Investigation worksheet (25 min)

Fill in:

| Question | Your answer | Evidence (panel/query) |
| -------- | ----------- | ------------------------ |
| User-visible symptom? | | |
| Error golden signal? | | |
| Saturation golden signal? | | |
| Likely root cause class (code/config/infra)? | | |
| First rollback or mitigation step? | | |

Use **Explore** to run:

```logql
{job="demo"} |= "deploy"
```

and

```promql
rate(node_cpu_seconds_total[1m])
```

✅ **Checkpoint:** Root cause class is **application/errors**, not CPU — unless your stress test dominated (explain if so).

---

## Part D — Azure connection (20 min, optional)

If you completed Day 2:

1. Open the **metric alert** you created.
2. Write how the same symptom would appear in Azure (which metric or table).
3. Compare email alert (Azure) vs looking at Grafana (PLG).

No Azure? Write two sentences on how you **would** wire Azure Monitor as a Grafana datasource in production (conceptual).

✅ **Checkpoint:** You stated one difference between platform metrics and app logs.

---

## Part E — Cleanup (10 min)

```bash
docker compose down
```

Optional: delete `rg-obs-<yourname>` if it was lab-only.

---

## Deliverables (present to instructor)

1. Dashboard screenshot during incident simulation.
2. Completed investigation worksheet.
3. **30-second verbal summary:** metrics you trust first, logs second, and why.

---

## Bonus

- Add a Grafana **alert rule** on ERROR log rate (Grafana unified alerting).
- Read [Resources/Useful-Links.md](../Resources/Useful-Links.md) and pick one cert or doc to continue.

**Congratulations — you finished the Observability 5-Day Course.**
