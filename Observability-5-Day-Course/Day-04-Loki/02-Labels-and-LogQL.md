# 02 — Labels and LogQL

**Learning objectives**

- Write a **log stream selector**
- Filter lines with `\|=`, `\|~`, `\!=`
- Run a simple **metric query** from logs

---

## Stream selector

Every LogQL query starts with labels:

```logql
{job="demo"}
```

Only logs with `job="demo"` (from the Alloy config).

Add labels:

```logql
{job="demo", host="lab"}
```

---

## Line filters

| Filter | Meaning |
| ------ | ------- |
| `\|= "ERROR"` | Contains string |
| `\!= "DEBUG"` | Does not contain |
| `\|~ "timeout\|failed"` | Regex match |
| `\|~ "(?i)error"` | Case-insensitive regex |

Example:

```logql
{job="demo"} |= "ERROR"
```

---

## Parse (awareness)

JSON logs can use `| json | level="ERROR"` — requires structured lines. Our demo file is plain text; string filter is enough today.

---

## Metric queries from logs

Count lines per stream over 5 minutes:

```logql
count_over_time({job="demo"}[5m])
```

Useful for “error spike” panels in Grafana.

---

## Try in Grafana Explore

1. http://localhost:3000 → **Explore**
2. Datasource **Loki**
3. Query `{job="demo"}` → **Run query**
4. Append to `logs/app.log` (see sample-stack README) and refresh.

---

## LogQL vs KQL

| KQL | LogQL |
| --- | ----- |
| `where Message has "ERROR"` | `{job="demo"} |= "ERROR"` |
| `summarize count() by bin(...)` | `count_over_time(...[5m])` |

---

## Knowledge check

1. Must LogQL always start with `{` ?
2. What query shows only ERROR lines for demo job?
3. What does `count_over_time` return?

<details>
<summary>Answers</summary>

1. Yes — a stream selector (or metric query derived from one).
2. `{job="demo"} |= "ERROR"`.
3. A number of log lines per label set over the range window.

</details>

➡️ Next: [03 — Grafana Alloy](./03-Alloy-Pipeline.md)
