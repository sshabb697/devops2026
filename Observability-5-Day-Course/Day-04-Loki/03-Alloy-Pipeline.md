# 03 — Grafana Alloy (the collector)

**Learning objectives**

- Say what **Grafana Alloy** does in one sentence
- Read the lab file `alloy/config.alloy`
- Explain discover → process → write in an Alloy pipeline
- Know Alloy **pushes** logs to Loki

Promtail (older agent) did the same job. Grafana now recommends **Alloy**. Concepts match: find files, add labels, push.

---

## One-sentence idea

Alloy is the collector and processing pipeline. It discovers log files, parses
their JSON, adds a few useful labels, and sends the result to Loki. Grafana
queries Loki; it does not read the files directly.

```text
checkout-api writes JSON to logs/app.log
  │
  ▼
Alloy discover → parse → label ──push──► Loki ◄──query── Grafana
```

---

## The lab config (River language)

Alloy configs use **River**, not YAML. File: `sample-stack/alloy/config.alloy`.

```river
local.file_match "demo" {
  path_targets = [{
    __path__ = "/var/log/demo/*.log",
    job      = "demo",
    host     = "lab",
  }]
}

loki.source.file "demo" {
  targets    = local.file_match.demo.targets
  forward_to = [loki.process.demo.receiver]
}

loki.process "demo" {
  stage.json {
    expressions = {
      level   = "level",
      service = "service",
      version = "version",
    }
  }

  stage.labels {
    values = {
      level   = "",
      service = "",
      version = "",
    }
  }

  forward_to = [loki.write.default.receiver]
}

loki.write "default" {
  endpoint {
    url = "http://loki:3100/loki/api/v1/push"
  }
}
```

| Piece | Meaning |
| ----- | ------- |
| `local.file_match` | Which files to watch |
| `__path__` | Path **inside the Alloy container** |
| `job`, `host` | Static Loki labels added during discovery |
| `stage.json` | Extract fields from each JSON log line |
| `stage.labels` | Promote selected fields to stream labels |
| `loki.write` | Push URL |

Compose mounts `./logs` → `/var/log/demo` in Alloy, and the demo app writes the same folder as `/logs`.

## Labels versus parsed fields

Use labels for bounded values such as `service`, `level`, and deployment
`version`. Do **not** label request IDs, customer IDs, raw URLs, or
`duration_ms`: each unique label set creates a Loki stream and can cause a
cardinality explosion.

The full JSON body remains queryable without making every field a label:

```logql
{job="demo", level="ERROR"} | json | status >= 500
```

```logql
{job="demo"} | json | duration_ms > 500
```

The selector uses indexed labels first. `| json` then parses matching log
lines, and the final expression filters parsed fields.

---

## Alloy UI

http://localhost:12345 — Alloy’s own page. Use it if logs never arrive: component graph should show `loki.source.file` and `loki.write`.

---

## Troubleshooting

| Symptom | Check |
| ------- | ----- |
| No streams | `docker compose logs alloy` |
| Wrong job | Labels in `config.alloy` vs LogQL `{job="demo"}` |
| Empty file | Hit http://localhost:8080 so the app writes a line |
| Windows | Write into repo `logs/`, not a random `C:\` path |

```bash
curl -s http://localhost:3100/ready
curl -s http://localhost:8080/
```

---

## Knowledge check

1. Does Prometheus pull logs from Alloy?
2. Why is `service` a reasonable label but `duration_ms` is not?
3. What does `stage.json` do before `stage.labels`?
4. Is Alloy config YAML?

<details>
<summary>Answers</summary>

1. No. Alloy **pushes** logs to Loki. Prometheus **pulls** metrics (Day 3).
2. `service` has a small bounded set; durations can have almost unlimited values.
3. It extracts values from each structured log line so selected values can be promoted.
4. No — River (`.alloy`).

</details>

➡️ Next: [Lab 04](./Lab-04-Loki.md)
