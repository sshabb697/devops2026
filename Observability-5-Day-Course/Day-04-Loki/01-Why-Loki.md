# 01 — Why Loki?

**Learning objectives**

- Contrast **Loki** with “index everything” log systems
- Explain **label-based** log streams (like Prometheus labels)
- Place Loki in the PLG stack

---

## The log problem

Servers generate huge log volume. Indexing every word is expensive.

**Grafana Loki** stores logs cheaply by indexing **labels** (metadata), not full text by default.

```text
Grafana Alloy  ──push──►  Loki  ◄──query──  Grafana / LogQL
```

---

## Loki vs Azure Log Analytics

| | Azure Log Analytics | Loki |
| - | ------------------- | ---- |
| Query language | KQL | LogQL |
| Best fit | Azure-wide, many tables | Kubernetes / cloud-native stacks |
| Identity | Azure resource IDs | Custom labels (`job`, `namespace`, `pod`) |

Teams often use **both**: Azure platform logs in Monitor, app logs in Loki on AKS.

---

## Labels are contracts

Good labels:

```text
{job="demo", env="lab", host="student1"}
```

Bad labels (high cardinality):

```text
{user_id="991828373"}
```

Never use unbounded values as labels — it crashes performance (same rule as Prometheus).

---

## Components in our lab

| Service | Role |
| ------- | ---- |
| **alloy** | Tails files, adds labels, pushes to Loki |
| **loki** | Stores and serves queries |
| **grafana** | Explore UI (Day 5) |

Logs live in `./sample-stack/logs/*.log` on your machine.

---

## Knowledge check

1. What does Loki index heavily?
2. Why not label every log line with `order_id`?
3. Which agent ships logs in our stack?

<details>
<summary>Answers</summary>

1. Labels (metadata), not every token in the message.
2. Cardinality — too many unique series.
3. Grafana Alloy.

</details>

➡️ Next: [02 — Labels and LogQL](./02-Labels-and-LogQL.md)
