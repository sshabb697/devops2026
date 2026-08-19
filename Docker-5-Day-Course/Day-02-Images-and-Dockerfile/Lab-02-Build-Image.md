# Lab 02 — Build campus-hello

**Time:** 60 minutes

Use the course folder `Docker-5-Day-Course/sample-app/`.

---

## Part A — Read the files (10 min)

```bash
cd Docker-5-Day-Course/sample-app
cat Dockerfile
cat index.html
cat .dockerignore
```

---

## Part B — Build (20 min)

```bash
docker build -t campus-hello:1.0 .
docker images | grep campus-hello
docker history campus-hello:1.0
```

Expected: image `campus-hello` tag `1.0`.

---

## Part C — Run (15 min)

```bash
docker rm -f hello 2>/dev/null || true
docker run -d -p 8080:80 --name hello campus-hello:1.0
```

Open **http://localhost:8080**

Expected: “Hello from a container” (not the default nginx page).

```bash
docker logs hello
```

---

## Part D — Change and rebuild (15 min)

1. Edit `index.html` — change the heading text.
2. Rebuild:

```bash
docker build -t campus-hello:1.0 .
docker rm -f hello
docker run -d -p 8080:80 --name hello campus-hello:1.0
```

Refresh the browser. You should see the new text.

Cleanup:

```bash
docker rm -f hello
```

---

## Deliverables

- [ ] Built `campus-hello:1.0`
- [ ] Browser shows your HTML
- [ ] Rebuilt after an HTML change

➡️ **Day 3:** [Data and networking](../Day-03-Data-and-Networking/README.md)
