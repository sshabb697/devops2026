# 01 — Troubleshooting

**Learning objectives**

- Follow a fixed order: daemon → name/port → logs → inspect
- Map common errors to fixes

---

## Order of checks

1. Is Docker running? `docker info`
2. Is the container running? `docker ps -a`
3. Logs: `docker logs name` or `docker compose logs`
4. Port: `docker port name` and try curl
5. Inspect: mounts, env, network

```bash
docker ps -a
docker logs --tail 50 mynginx
docker inspect mynginx --format "{{.State.Status}} {{.State.Error}}"
docker compose logs -f
```

---

## Common errors

| Symptom | Likely cause | What to try |
| ------- | ------------ | ----------- |
| Cannot connect to daemon | Desktop not started | Start Docker Desktop |
| Port already allocated | Another container or app | `docker ps`, change `-p` |
| Name already in use | Old container | `docker rm -f name` |
| Image not found | Typo or not built | `docker images`, rebuild |
| Connection refused | Process not listening / wrong port | `docker logs`, `docker exec ss` or curl inside |
| Page is old HTML | Ran old container/image | Recreate with `--build` |

---

## Disk

```bash
docker system df
```

Do not `docker system prune -a` on a shared lab machine unless the instructor says so.

---

## Knowledge check

1. First command when `docker run` fails with “daemon”?
2. Connection refused vs port already allocated?

<details>
<summary>Answers</summary>

1. `docker info` / start Desktop.
2. Refused = nothing listening on that host port. Allocated = something else already bound that port.

</details>

➡️ Next: [02 — Security](./02-Security-Basics.md)
