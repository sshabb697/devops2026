# Lab 02A — Enable Kubernetes on your laptop

**Time:** 15 minutes

Pick **one** path. Tutors: Docker Desktop is the default for this class.

---

## Path 1 — Docker Desktop (recommended)

1. Open **Docker Desktop**.
2. Settings → **Kubernetes** → enable Kubernetes → Apply.
3. Wait until Docker says Kubernetes is running (can take several minutes the first time).

```bash
kubectl get nodes
```

Expected: one node, `STATUS` = `Ready`.

---

## Path 2 — minikube

Official walkthrough: [Hello Minikube](https://kubernetes.io/docs/tutorials/hello-minikube/)

```bash
minikube start
kubectl get nodes
```

---

## Path 3 — no local install (browser)

If Docker Desktop will not start, use a **free playground** (session ~60 minutes):

1. Open [Killercoda Kubernetes playground](https://killercoda.com/playgrounds/scenario/kubernetes)
2. Wait for the terminal
3. Run `kubectl get nodes`

You can still do Days 3–7 labs there. Days 8–10 still need Azure.

Also listed: [Play with Kubernetes](https://labs.play-with-k8s.com/) and the official [learning environment](https://kubernetes.io/docs/setup/learning-environment/) page.

---

## If you get stuck

| Problem | Fix |
| ------- | --- |
| `kubectl` not found | Docker Desktop: restart the terminal. Windows: install CLI from Docker or `az aks install-cli` later |
| connection refused | Kubernetes toggle is still starting — wait, then retry |
| Two contexts | `kubectl config current-context` — should be `docker-desktop` or `minikube` |

---

## Deliverables

- [ ] `kubectl get nodes` works
- [ ] Screenshot or tutor sign-off

➡️ Next: [02 — Namespaces](./02-Namespaces.md)
