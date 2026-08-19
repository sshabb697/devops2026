# 02 — Security basics

**Learning objectives**

- Keep secrets out of images
- Prefer small official base images
- Scan as a habit (awareness)

---

## Rules for this class (and work)

1. **No secrets in Dockerfiles** or Git. Use env vars at run time, or a vault.
2. **Pin tags** (`nginx:1.27-alpine`, not only `latest`).
3. **Small bases** (`alpine`, distroless) when they fit — fewer packages to patch.
4. **Do not run as root** in production apps when you can set `USER`.
5. **Scan** images in CI (`docker scout`, ACR scan, Trivy) — awareness this week.

---

## Multi-stage helps security

The compiler and source do not ship to production (Day 4).

---

## Publish less

Only `-p` what the browser or load balancer needs. Databases stay on the Compose network without a public port (like Redis in the sample stack).

---

## Knowledge check

1. Why is Redis in our stack without `ports:`?
2. Why avoid `latest` in production?

<details>
<summary>Answers</summary>

1. Only `web` needs to be reached from the laptop; Redis is internal.
2. The image can change without you noticing.

</details>

➡️ Next: [03 — What’s next](./03-Whats-Next.md)
