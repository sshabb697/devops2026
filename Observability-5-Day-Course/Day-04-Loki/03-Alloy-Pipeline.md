# 03 — Grafana Alloy (the collector)

**Learning objectives**

- Say what **Grafana Alloy** does in one sentence
- Read the lab file `alloy/config.alloy`
- Know Alloy **pushes** logs to Loki

Promtail (older agent) did the same job. Grafana now recommends **Alloy**. Concepts match: find files, add labels, push.

---

## One-sentence idea

Alloy is the **postman**. It reads log files and delivers them to Loki. Grafana is where you read the mail.

```text
demo-app writes logs/app.log
        │
        ▼
Grafana Alloy  ──push──►  Loki  ◄──query──  Grafana
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
| `job`, `host` | Loki **labels** you will query |
| `loki.write` | Push URL |

Compose mounts `./logs` → `/var/log/demo` in Alloy, and the demo app writes the same folder as `/logs`.

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
2. What label does `{job="demo"}` match?
3. Is Alloy config YAML?

<details>
<summary>Answers</summary>

1. No. Alloy **pushes** logs to Loki. Prometheus **pulls** metrics (Day 3).
2. The `job` label set in `config.alloy`.
3. No — River (`.alloy`).

</details>

➡️ Next: [Lab 04](./Lab-04-Loki.md)
