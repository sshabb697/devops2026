# 01 — Container lifecycle

**Learning objectives**

- Inspect logs and run a shell inside a container
- Remove containers safely

---

## Everyday commands

```bash
docker ps
docker ps -a
docker logs hello
docker logs -f hello
docker exec -it hello sh
docker inspect hello
docker stats
```

Inside Alpine nginx, the shell is often `sh`, not `bash`.

```bash
docker exec hello ls /usr/share/nginx/html
```

---

## Stop vs kill vs rm

| Command | Meaning |
| ------- | ------- |
| `docker stop` | SIGTERM, then SIGKILL after timeout |
| `docker kill` | Immediate SIGKILL |
| `docker rm` | Delete a **stopped** container |
| `docker rm -f` | Stop and delete |

Prefer `stop` then `rm` in class so you see the states.

---

## Knowledge check

1. `logs` vs `exec`?
2. Does `docker stop` delete the container?

<details>
<summary>Answers</summary>

1. `logs` reads output. `exec` runs a new command inside a running container.
2. No — it still shows in `docker ps -a` until `rm`.

</details>

➡️ Next: [02 — Ports](./02-Ports.md)
