# 01 — What is observability?

**Learning objectives**

- Contrast **monitoring** and **observability**
- Describe what a beginner should optimize for first: **fast answers**, not more dashboards
- Name the main audience: developers, ops, and on-call engineers

---

## The problem in class

Production is slow. The manager asks: “Is it the database, the network, or our new release?”

If you only know “CPU looks fine,” you might guess wrong and waste an hour.

**Observability** means you can **ask new questions** with the data you already collected — without redeploying the app for every guess.

---

## Monitoring vs observability (simple version)

| Monitoring | Observability |
| ---------- | ------------- |
| “We watch known things” | “We can investigate unknown things” |
| Fixed dashboards and alerts | Flexible queries across metrics, logs, traces |
| “Disk 90% full” alert | “Which customer requests fail only on API v2 after 14:00?” |

You need **both**. Monitoring catches known failures. Observability helps when symptoms are new or weird.

---

## A useful analogy

**Monitoring** is like smoke alarms in a building — they fire for known dangers.

**Observability** is like security cameras + access logs — you can replay *what happened* when nobody knows why the alarm went off.

---

## What “good” looks like for beginners

1. **One place** to check health (even if that is still three tabs at first).
2. **Logs** that include a **request id** or **correlation id** when possible.
3. **Metrics** on latency, errors, and traffic — not 500 custom graphs on day one.
4. **Runbooks**: “If alert X fires, check Y then Z.”

---

## Azure vs open source (preview)

This week you will see two worlds that often coexist:

| Area | Azure-native | Open source (this course) |
| ---- | ------------ | ------------------------- |
| Metrics | Azure Monitor metrics | **Prometheus** |
| Logs | Log Analytics / App Insights | **Loki** |
| Dashboards | Azure workbooks, Grafana on Azure | **Grafana** |

Many teams export Azure metrics to Grafana or run Prometheus in Kubernetes **and** use Azure Monitor for the platform. You are learning patterns that transfer.

---

## Knowledge check

1. Can monitoring exist without observability?
2. Why are logs alone not enough for every problem?
3. Who needs observability besides “the ops person”?

<details>
<summary>Answers</summary>

1. Yes — many teams only have basic alerts; they struggle with novel failures.
2. Logs are rich but expensive to search at scale; metrics summarize trends quickly.
3. Developers need traces and logs to debug code; product needs error rates; finance cares about uptime.

</details>

➡️ Next: [02 — Three pillars](./02-Three-Pillars.md)
