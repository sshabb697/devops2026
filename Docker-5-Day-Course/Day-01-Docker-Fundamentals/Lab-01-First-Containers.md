# Lab 01 — First containers

**Time:** 60 minutes

Work in a terminal where `docker version` works.

---

## Part A — hello-world (10 min)

```bash
docker run --rm hello-world
```

Expected: a success message from Docker.

---

## Part B — nginx (25 min)

```bash
docker pull nginx
docker images
docker run -d -p 8080:80 --name mynginx nginx
docker ps
```

Open **http://localhost:8080**

Expected: nginx welcome page.

```bash
docker stop mynginx
docker ps
docker ps -a
docker start mynginx
```

Browser should work again after `start`.

```bash
docker stop mynginx
docker rm mynginx
docker ps -a
```

Expected: `mynginx` is gone.

---

## Part C — second image (15 min)

Run a second official image (httpd) on another host port so it does not clash with 8080:

```bash
docker run -d -p 8082:80 --name myhttpd httpd:2.4
docker ps
```

Open **http://localhost:8082**

Expected: “It works!”

```bash
docker stop myhttpd
docker rm myhttpd
```

---

## Part D — cleanup check (10 min)

```bash
docker ps -a
docker images
```

List what is still on disk. You may keep the `nginx` image for Day 2.

If you must wipe **stopped** containers you created in this lab:

```bash
docker rm mynginx myhttpd 2>/dev/null || true
```

---

## If you get stuck

| Error | Likely cause |
| ----- | ------------ |
| Port already allocated | Something uses 8080 — use `-p 8088:80` or `docker rm -f` the old name |
| Name already in use | `docker rm -f mynginx` then run again |
| Cannot connect to daemon | Start Docker Desktop |

---

## Deliverables

- [ ] `hello-world` ran
- [ ] nginx served a page on a mapped port
- [ ] Used `ps`, `ps -a`, `stop`, `start`, `rm`

➡️ **Day 2:** [Images and Dockerfile](../Day-02-Images-and-Dockerfile/README.md)
