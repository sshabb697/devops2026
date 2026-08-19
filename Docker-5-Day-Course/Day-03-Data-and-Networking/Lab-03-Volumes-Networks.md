# Lab 03 — Persist and connect

**Time:** 60 minutes

If `campus-hello:1.0` is missing, rebuild from `sample-app` (Day 2 lab).

---

## Part A — Logs and exec (15 min)

```bash
docker rm -f hello 2>/dev/null || true
docker run -d -p 8080:80 --name hello campus-hello:1.0
docker logs hello
docker exec hello ls /usr/share/nginx/html
docker inspect hello --format "{{.State.Status}}"
```

---

## Part B — Volume (25 min)

```bash
docker rm -f volweb volweb2 2>/dev/null || true
docker volume create lab03data
docker run -d --name volweb -p 8083:80 -v lab03data:/usr/share/nginx/html nginx:alpine
docker exec volweb sh -c 'echo LAB03 > /usr/share/nginx/html/index.html'
curl http://localhost:8083
docker rm -f volweb
docker run -d --name volweb2 -p 8083:80 -v lab03data:/usr/share/nginx/html nginx:alpine
curl http://localhost:8083
```

Expected: both curls show `LAB03`.

Cleanup:

```bash
docker rm -f volweb2 hello
docker volume rm lab03data
```

---

## Part C — Network (20 min)

```bash
docker network create lab03net
docker run -d --name web --network lab03net campus-hello:1.0
docker run --rm --network lab03net curlimages/curl:8.5.0 curl -sI http://web
```

Expected: HTTP 200 from `http://web` (no localhost).

```bash
docker rm -f web
docker network rm lab03net
```

---

## Deliverables

- [ ] Used `logs` and `exec`
- [ ] Volume survived `docker rm`
- [ ] Curl by **container name** on a user network

➡️ **Day 4:** [Compose and registry](../Day-04-Compose-and-Registry/README.md)
