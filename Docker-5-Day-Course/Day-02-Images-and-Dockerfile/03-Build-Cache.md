# 03 — Build cache and `.dockerignore`

**Learning objectives**

- Rebuild only changed layers
- Keep secrets and junk out of the image

---

## Cache

Each Dockerfile line is a **layer**. If a line and everything above it are unchanged, Docker reuses the layer. That is why builds get fast.

Change `index.html` and rebuild — only the `COPY` layer and after it rebuild.

---

## `.dockerignore`

Like `.gitignore`. Put next to the Dockerfile:

```
.git
*.md
.venv
node_modules
```

Without this you might copy huge folders into the context and slow every build.

---

## Do not bake secrets

Never `COPY .env` with production passwords. Pass secrets at **run** time (`-e`, Compose `environment`, or a secret store).

---

## Knowledge check

1. Why copy `requirements.txt` before the rest of the app?
2. What belongs in `.dockerignore`?

<details>
<summary>Answers</summary>

1. So pip install is cached when only app code changes.
2. Git metadata, docs, local venv, `node_modules`, secrets.

</details>

➡️ Next: [Lab 02](./Lab-02-Build-Image.md)
