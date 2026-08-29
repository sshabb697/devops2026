# Lab 10A — Scale and logs

**Time:** 15 minutes  
Context must be **AKS**.

---

## Part A — Scale (7 min)

```bash
kubectl get deploy hello -n class
kubectl scale deployment hello -n class --replicas=3
kubectl get pods -n class
```

Expected: 3 pods.

---

## Part B — Logs and portal (8 min)

```bash
kubectl logs -n class deploy/hello --tail=30
```

Optional: Azure Portal → AKS `aks-class` → **Workloads** / **Insights** if monitoring was enabled.

---

## Deliverables

- [ ] 3 replicas
- [ ] Logs command worked

➡️ Next: [02 — Troubleshoot](./02-Troubleshoot.md)
