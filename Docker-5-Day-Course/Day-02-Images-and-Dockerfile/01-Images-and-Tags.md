# 01 — Images and tags

**Learning objectives**

- Read `nginx:1.27` as name + tag
- List and inspect local images

---

## Name and tag

```
nginx:1.27-alpine
│     │
│     └── tag (version / variant)
└──────── repository name
```

`nginx` with no tag means `nginx:latest`. In class, **prefer an explicit tag** so everyone gets the same version.

```bash
docker images
docker image ls
docker inspect nginx
docker history nginx
```

---

## Where images come from

1. `docker pull` from a registry
2. `docker build` from a Dockerfile (today)
3. `docker commit` (avoid in class — use Dockerfiles)

Images are **layered**. Tomorrow you will see why cache matters.

---

## Knowledge check

1. What is the tag in `httpd:2.4`?
2. Why pin a version instead of `latest`?

<details>
<summary>Answers</summary>

1. `2.4`
2. `latest` can change overnight; class and production need a known version.

</details>

➡️ Next: [02 — Dockerfile](./02-Dockerfile.md)
