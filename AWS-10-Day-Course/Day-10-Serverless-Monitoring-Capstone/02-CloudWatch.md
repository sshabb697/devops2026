# 02 — CloudWatch monitoring

**Learning objectives**

- Know what **CloudWatch** collects: metrics, logs, alarms
- Understand why monitoring matters in DevOps

---

## One-sentence idea

CloudWatch is the **dashboard and alarm system** for everything running in your AWS account.

---

## The three things CloudWatch gives you

| Feature | What it is | Example |
| ------- | ---------- | ------- |
| **Metrics** | Numbers over time | EC2 CPU %, Lambda invocations, RDS connections |
| **Logs** | Text output from services | Lambda `print()`s, app logs, VPC flow logs |
| **Alarms** | Watch a metric, act when it crosses a line | CPU > 80% for 5 min → email / auto-scale |

You already used all three: the **billing alarm** (Day 1), **Lambda logs** (Lab 10A), and now metrics.

---

## Why monitor?

> "You can't fix what you can't see."

Monitoring answers: Is the app up? Is it slow? Is something about to fail? Without it, the first sign of trouble is an angry customer.

```text
Metric crosses threshold ─▶ Alarm fires ─▶ SNS email / auto-scale / Lambda fix
```

---

## Alarm anatomy

An alarm watches **one metric** and has:
- A **threshold** (e.g. CPU > 80%).
- A **period** (e.g. over 5 minutes) so a one-second spike doesn't page you.
- An **action** (notify via SNS, trigger Auto Scaling, run a Lambda).

```bash
aws cloudwatch describe-alarms --query "MetricAlarms[].[AlarmName,StateValue]" --output table
```

---

## Beyond basics (good to know)

- **Dashboards:** one screen of graphs for your whole system.
- **Logs Insights:** query logs with a simple language.
- **Container/Lambda Insights:** deeper metrics for ECS/EKS/Lambda.

(For a full monitoring deep-dive, see the [Observability 5-Day Course](../../Observability-5-Day-Course/).)

---

## Knowledge check

1. Name the three core things CloudWatch provides.
2. Why does an alarm use a "period" instead of firing instantly?

<details>
<summary>Answers</summary>

1. Metrics, logs, and alarms.
2. To avoid false alarms from brief spikes — it checks the metric stays over the threshold for a set time.

</details>

➡️ Next: [Lab 10B](./Lab-10B-Capstone-and-Teardown.md)
