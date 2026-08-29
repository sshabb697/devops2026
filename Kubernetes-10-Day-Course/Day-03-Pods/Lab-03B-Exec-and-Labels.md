# Lab 03B — Exec and labels

**Time:** 15 minutes  
Need `nginx-demo` from Lab 03A. If missing, `kubectl apply -f nginx-pod.yaml` again.

---

## Part A — Labels (4 min)

```bash
kubectl get pods --show-labels
kubectl get pods -l app=nginx
```

Expected: `nginx-demo` listed.

---

## Part B — Exec (6 min)

```bash
kubectl exec -it nginx-demo -- nginx -v
kubectl logs nginx-demo
```

Optional: `kubectl exec -it nginx-demo -- sh` then `exit`.

---

## Part C — Delete and see the gap (5 min)

```bash
kubectl delete pod nginx-demo
kubectl get pods
```

Expected: empty (or no `nginx-demo`). Tutor asks: “Who brings it back?” Answer: **nobody — until Day 4 Deployment.**

---

## Deliverables

- [ ] Used `--show-labels` and `-l app=nginx`
- [ ] Deleted the Pod on purpose

➡️ **Day 4:** [ReplicaSets and Deployments](../Day-04-ReplicaSets-and-Deployments/README.md)
