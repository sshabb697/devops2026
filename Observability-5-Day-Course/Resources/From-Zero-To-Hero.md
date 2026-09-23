# How this course relates to observability-zero-to-hero

Reference: [iam-veeramalla/observability-zero-to-hero](https://github.com/iam-veeramalla/observability-zero-to-hero/).

That repo is a **7-day Kubernetes** series (EKS, Helm, EFK, Jaeger, OpenTelemetry). This course is a **5-day Docker** series for people who are new to the words metrics and logs.

| Their day | Their tools | This course |
| --------- | ----------- | ----------- |
| 1 Concepts | Monitoring vs observability | [Day 1](../Day-01-Observability-Fundamentals/) |
| 2–3 Prometheus + PromQL | kube-prometheus-stack on EKS | [Day 3](../Day-03-Prometheus/) on Docker |
| 4 Custom metrics + alerts | Node.js + Alertmanager | Demo app `/metrics` + Grafana on [Day 5](../Day-05-Grafana-and-Capstone/) |
| 5 Logging | Elasticsearch, Fluent Bit, Kibana | [Day 4](../Day-04-Loki/) **Loki + Alloy** |
| 6 Tracing | Jaeger + OpenTelemetry | Not in the 5 days. Do their Day 6 after you are comfortable with metrics and logs. |
| 7 OpenTelemetry collector | One pipeline for all signals | Alloy is the collector we use for **logs**. Later, Alloy can also remote-write metrics. |

## Why Alloy, not Promtail or Fluent Bit

- **Promtail** is in maintenance mode. Grafana’s current agent is **[Alloy](https://grafana.com/docs/alloy/latest/)**.
- **Fluent Bit / Elasticsearch** (their Day 5) is a different stack. Loki keeps labels like Prometheus, which is easier as a second tool in the same week.
- **Docker Compose** lets every student run the demo without an EKS cluster.

## After this week

1. Their [day-2](https://github.com/iam-veeramalla/observability-zero-to-hero/tree/main/day-2) Helm install on a real cluster.
2. Traces: [Jaeger](https://www.jaegertracing.io/) or [Grafana Tempo](https://grafana.com/oss/tempo/).
3. Azure path already in this course: [Day 2 Azure Monitor](../Day-02-Azure-Monitor/).
