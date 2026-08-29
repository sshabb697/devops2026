# Lab 02B — First kubectl commands

**Time:** 15 minutes  
Work in a terminal where Lab 02A succeeded.

---

## Part A — Look around (5 min)

```bash
kubectl cluster-info
kubectl get nodes -o wide
kubectl get ns
kubectl get pods -A
```

`-A` means all namespaces. You will see system Pods. That is normal.

---

## Part B — Create a class namespace (5 min)

```bash
kubectl create namespace class-day2
kubectl get ns
```

Expected: `class-day2` is **Active**.

---

## Part C — Cleanup (5 min)

We will recreate namespaces later. Delete this one so names stay clean:

```bash
kubectl delete namespace class-day2
kubectl get ns
```

Expected: `class-day2` is gone.

---

## Deliverables

- [ ] Listed nodes and namespaces
- [ ] Created and deleted `class-day2`

➡️ **Day 3:** [Pods](../Day-03-Pods/README.md)
