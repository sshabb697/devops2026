# Lab 01 — First look at logs and metrics

**Time:** 60 minutes

Use **WSL**, Linux, or macOS. Windows-only users can use WSL for `journalctl`; otherwise skip Part B and use Part C only.

---

## Part A — Metrics without a tool (15 min)

1. Open a terminal.
2. Run:

```bash
uptime
free -h
df -h
```

3. Write down one **golden signal** each command relates to (latency / traffic / errors / saturation).

✅ **Checkpoint:** You labeled at least two commands with a golden signal.

---

## Part B — Follow logs (15 min)

If `systemd` is available:

```bash
journalctl -n 30 --no-pager
journalctl -f
```

Press **Ctrl+C** to stop following.

In another terminal, generate an event (example):

```bash
logger "obs-lab test message from $(whoami)"
```

✅ **Checkpoint:** You saw your test line in the journal.

---

## Part C — HTTP check (15 min)

If you have any local web server or Docker from the Docker course:

```bash
curl -s -o /dev/null -w "HTTP %{http_code} in %{time_total}s\n" http://localhost:8080/
```

Run three times. Note **latency** (time_total) and **errors** (non-2xx code).

No server? Use a public endpoint once (read-only):

```bash
curl -s -o /dev/null -w "HTTP %{http_code} in %{time_total}s\n" https://learn.microsoft.com/
```

✅ **Checkpoint:** You recorded three timings.

---

## Part D — Incident role-play (15 min)

Partner or solo — fill this table for a fictional outage “checkout is slow”:

| Step | Pillar | What you would check |
| ---- | ------ | -------------------- |
| 1 | Metric | |
| 2 | Log | |
| 3 | Trace | |

✅ **Checkpoint:** Metric step mentions error rate or latency; log step mentions searching ERROR lines.

---

## Deliverables

- Screenshot or notes: three `curl` timings **or** journal test line.
- One paragraph: “Monitoring vs observability in my own words.”

➡️ Tomorrow: [Day 2 — Azure Monitor](../Day-02-Azure-Monitor/README.md)
