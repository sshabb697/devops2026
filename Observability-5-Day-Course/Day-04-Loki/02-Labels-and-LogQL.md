# 02 — Labels and LogQL

**Learning objectives**

- Write a **log stream selector**
- Filter lines with `\|=`, `\|~`, `\!=`
- Parse and filter JSON fields
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

## Parse structured JSON

The checkout API writes one JSON object per line. Alloy promotes `level`,
`service`, and `version` to labels, while request values remain in the log body.

Filter with a label first, then parse the remaining fields:

```logql
{job="demo", level="ERROR"} | json | status >= 500
```

Find slow requests without turning duration into a high-cardinality label:

```logql
{job="demo"} | json | duration_ms > 500
```

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
4. Run `docker compose run --rm load-generator --requests 5` and refresh.

---

## LogQL vs KQL

| KQL | LogQL |
| --- | ----- |
| `where Level == "ERROR"` | `{job="demo", level="ERROR"}` |
| `where StatusCode >= 500` | `{job="demo"} \| json \| status >= 500` |
| `summarize count() by bin(...)` | `count_over_time(...[5m])` |

---

## Knowledge check

1. Must LogQL always start with `{` ?
2. What query shows only indexed ERROR lines for the demo job?
3. What does `count_over_time` return?

<details>
<summary>Answers</summary>

1. Yes — a stream selector (or metric query derived from one).
2. `{job="demo", level="ERROR"}`.
3. A number of log lines per label set over the range window.

</details>

➡️ Next: [03 — Grafana Alloy](./03-Alloy-Pipeline.md)
