# Lab 04A — ReplicaSet heals a Pod

**Time:** 15 minutes  
Folder: `Day-04-ReplicaSets-and-Deployments/`

---

## Part A — Create 3 copies (5 min)

```bash
kubectl apply -f nginx-rs.yaml
kubectl get rs
kubectl get pods -l app=web
```

Expected: **3** pods, `Running`.

---

## Part B — Kill one (7 min)

Copy one Pod name from `kubectl get pods -l app=web`, then:

```bash
kubectl delete pod POD_NAME_HERE
kubectl get pods -l app=web -w
```

Watch: one disappears, a **new name** appears. `Ctrl+C` to stop watch.

---

## Part C — Cleanup (3 min)

```bash
kubectl delete -f nginx-rs.yaml
kubectl get pods -l app=web
```

Expected: all those Pods gone.

---

## Deliverables

- [ ] Saw a replacement Pod after delete

➡️ Next: [02 — Deployment](./02-Deployment.md)
