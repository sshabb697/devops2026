# Lab 04 — Compose and push

**Time:** 70 minutes

---

## Part A — Compose stack (30 min)

```bash
cd Docker-5-Day-Course/sample-app/stack
docker compose up -d --build
docker compose ps
docker compose logs
```

Open **http://localhost:8080**

Expected: campus hello page. Redis runs without a published port (only on `appnet`).

```bash
docker compose exec cache redis-cli ping
```

Expected: `PONG`

```bash
docker compose down
```

---

## Part B — Tag for a registry (20 min)

```bash
cd ../
docker images | grep campus-hello
docker tag campus-hello:1.0 YOURUSER/campus-hello:1.0
docker images | grep campus-hello
```

Optional if you have a Hub account:

```bash
docker login
docker push YOURUSER/campus-hello:1.0
```

---

## Part C — Recreate from Compose (20 min)

```bash
cd stack
docker compose up -d
curl -I http://localhost:8080
docker compose down
```

---

## Deliverables

- [ ] Stack up with web + cache
- [ ] `redis-cli ping` → PONG
- [ ] Image tagged as `YOURUSER/campus-hello:1.0`
- [ ] (Optional) pushed to Hub

➡️ **Day 5:** [Ops and capstone](../Day-05-Ops-Security-Capstone/README.md)
