# 03 — What is next

You finished **Docker inner loop**: run, build, persist, compose, push.

---

## Kubernetes in one paragraph

Kubernetes runs **many containers** across machines: Pods, Deployments, Services, Ingress.

Mental map:

| Docker (this week) | Kubernetes (later) |
| ------------------ | ------------------ |
| `docker run` | Pod |
| Compose `services` | Deployment + Service |
| `-p` / Compose ports | Service / Ingress |
| Named volume | PersistentVolumeClaim |

Do not start kubectl until `docker compose` feels boring.

---

## In this repo

- [Linux 5-Day Course](../../Linux-5-Day-Course/) — the OS inside most images
- [Azure DevOps](../../Azure-DevOps-6-Day-Course/) — build/push in a pipeline
- [AZ-104](../../AZ-104-Azure-Administrator/) — VMs and networks that host Docker

➡️ Next: [Lab 05 — Capstone](./Lab-05-Capstone.md)
