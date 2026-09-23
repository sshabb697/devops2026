# Observability 5-Day Course

Hands-on observability for **absolute beginners**. Docker demos use **Prometheus**, **Loki**, **Grafana Alloy**, and **Grafana**. Day 2 adds **Azure Monitor** if you have an Azure account.

> Focus: **see metrics and logs on your laptop** — not every vendor feature.

Inspired by the ideas in [observability-zero-to-hero](https://github.com/iam-veeramalla/observability-zero-to-hero/) (Kubernetes, EFK, Jaeger). This course stays on **Docker** and the Grafana stack so beginners can finish without a cloud cluster. Map: [Resources/From-Zero-To-Hero.md](./Resources/From-Zero-To-Hero.md).

Print or keep open: **[Command Cheat Sheet](./Command-Cheat-Sheet.md)**

---

## What you will be able to do

By the end of the week you can:

1. Explain **metrics, logs, and traces** and when each helps during an incident.
2. Use **Azure Monitor** to view metrics, run a simple **KQL** query, and create an alert.
3. Run **Prometheus**, understand scrape targets, and write basic **PromQL**.
4. Ship logs to **Loki** with **Grafana Alloy** and search them with **LogQL**.
5. Build a **Grafana** dashboard that combines Azure or Prometheus metrics with Loki logs.

| Day | Topic | Outcome |
| --- | ----- | ------- |
| [Day 1](./Day-01-Observability-Fundamentals/) | Concepts, golden signals, first hands-on | Speak the language of SRE and ops |
| [Day 2](./Day-02-Azure-Monitor/) | Azure Monitor, Log Analytics, alerts | Observe Azure resources in the Portal |
| [Day 3](./Day-03-Prometheus/) | Prometheus model, PromQL, exporters | Run metrics locally |
| [Day 4](./Day-04-Loki/) | Loki, labels, Alloy, LogQL | Centralize and query logs |
| [Day 5](./Day-05-Grafana-and-Capstone/) | Grafana, dashboards, capstone | One pane of glass for metrics + logs |

---

## Prerequisites

- [Linux 5-Day Course](../Linux-5-Day-Course/) **or** comfort with a terminal (`cd`, `grep`, `curl`)
- [Docker 5-Day Course](../Docker-5-Day-Course/) **or** ability to run `docker compose up`
- For Day 2: **Azure subscription** + [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) (`az login`)
- 8 GB RAM recommended for the local PLG stack
- Optional: one small **Azure VM** or **App Service** from [AZ-104](../AZ-104-Azure-Administrator/) labs to monitor

---

## How to study

1. Read each **lesson** (objectives, diagrams, knowledge checks).
2. Type every **command** and Portal step yourself.
3. Finish the **lab** at the end of each day.
4. Use the **cheat sheet** when you forget syntax.

Each day is **5–6 hours**.

**If something fails:** check time range on charts, whether the container is running (`docker ps`), and whether you are querying the right **label** or **resource**.

---

## Course layout

```
Observability-5-Day-Course/
├── README.md
├── Command-Cheat-Sheet.md
├── Tutor-Notes.md
├── Resources/
├── sample-stack/          # demo app + Prometheus + Alloy + Loki + Grafana
├── Day-01-Observability-Fundamentals/
├── Day-02-Azure-Monitor/
├── Day-03-Prometheus/
├── Day-04-Loki/
└── Day-05-Grafana-and-Capstone/
```

---

## Connects to other courses in this repo

| Before / after | Course |
| -------------- | ------ |
| Terminal + services | [Linux 5-Day](../Linux-5-Day-Course/) |
| Containers for the lab stack | [Docker 5-Day](../Docker-5-Day-Course/) |
| Azure resources to monitor | [AZ-104 Azure Administrator](../AZ-104-Azure-Administrator/) |
| Kubernetes probes & logs | [Kubernetes 10-Day](../Kubernetes-10-Day-Course/) |
| Deploy infra with code | [Terraform 5-Day](../Terraform-5-Day-Course/) |

---

## Local lab stack (Days 3–5)

From `sample-stack/`:

```bash
docker compose up -d
```

| URL | Default login |
| --- | ------------- |
| Grafana http://localhost:3000 | `admin` / `admin` (change on first login) |
| Prometheus http://localhost:9090 | — |
| Demo app http://localhost:8080 | — |
| Alloy http://localhost:12345 | — |
| Loki http://localhost:3100/ready | — |

See [sample-stack/README.md](./sample-stack/README.md) for details and teardown.
