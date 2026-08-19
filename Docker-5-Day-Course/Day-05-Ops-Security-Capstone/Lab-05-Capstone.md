# Lab 05 — Capstone troubleshooting

**Time:** 90 minutes

You are on-call. The campus hello stack is “down.” Work the issues in order. Write: **symptom → command → fix**.

---

## Setup

```bash
cd Docker-5-Day-Course/sample-app/stack
docker compose down
docker compose up -d --build
curl -I http://localhost:8080
```

Baseline: HTTP 200.

---

## Issue 1 — Port clash (20 min)

```bash
docker compose down
docker run -d --name blocker -p 8080:80 nginx:alpine
docker compose up -d
docker compose ps
docker compose logs
```

Expected: web fails to bind 8080.

**Fix:** remove the blocker, start the stack again.

```bash
docker rm -f blocker
docker compose up -d
curl -I http://localhost:8080
```

---

## Issue 2 — Wrong name / stale container (20 min)

```bash
docker run -d --name hello -p 8090:80 nginx:alpine
```

This is **default nginx**, not campus-hello. Browser on 8090 shows the wrong page.

**Fix:** remove it and run your image:

```bash
docker rm -f hello
docker run -d --name hello -p 8090:80 campus-hello:1.0
curl -s http://localhost:8090 | head
docker rm -f hello
```

Expected: campus HTML, not default nginx.

---

## Issue 3 — Volume (20 min)

Create data, destroy container, prove volume:

```bash
docker volume create capstone
docker run -d --name cvol -p 8084:80 -v capstone:/usr/share/nginx/html nginx:alpine
docker exec cvol sh -c 'echo CAPSTONE > /usr/share/nginx/html/index.html'
docker rm -f cvol
docker run -d --name cvol2 -p 8084:80 -v capstone:/usr/share/nginx/html nginx:alpine
curl http://localhost:8084
docker rm -f cvol2
docker volume rm capstone
```

Expected: `CAPSTONE` after recreate.

---

## Issue 4 — Logs and exec (15 min)

```bash
cd Docker-5-Day-Course/sample-app/stack
docker compose up -d
docker compose logs web --tail 20
docker compose exec web ls /usr/share/nginx/html
docker compose exec cache redis-cli ping
docker compose down
```

---

## Final checklist

| Skill | You used |
| ----- | -------- |
| Run official image | nginx |
| Build Dockerfile | campus-hello |
| Ports | `-p` / Compose |
| Volume | named volume |
| Network / Compose | stack + redis |
| Logs | `compose logs` / `docker logs` |
| Registry concept | tag (and optional push) |

---

## Course complete

You finished the **5-day Docker** track.

Keep [Command-Cheat-Sheet.md](../Command-Cheat-Sheet.md) open on the job.
