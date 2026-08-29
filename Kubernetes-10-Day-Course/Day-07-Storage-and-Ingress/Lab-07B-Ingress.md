# Lab 07B — Ingress YAML (and optional controller)

**Time:** 15 minutes

---

## Part A — Read the YAML (5 min)

Open `shop-ingress.yaml`. Circle:

- Deployment `shop`
- Service `shop`
- Ingress path `/` → service `shop`

---

## Part B — Apply (5 min)

```bash
kubectl apply -f shop-ingress.yaml
kubectl get deploy,svc,ingress
```

If `ADDRESS` is empty, you **do not** have an Ingress Controller yet. That is OK for this hour.

---

## Part C — Optional controller (5 min) — skip if time is short

Docker Desktop / many local clusters:

```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.11.3/deploy/static/provider/cloud/deploy.yaml
kubectl -n ingress-nginx get pods
```

Wait until ingress-nginx pods are Running, then `kubectl get ingress` again.

Cleanup shop if you want a clean cluster:

```bash
kubectl delete -f shop-ingress.yaml
```

---

## Deliverables

- [ ] Explained Ingress vs Service to a partner

➡️ **Day 8:** [AKS cluster](../Day-08-AKS-Cluster/README.md)
