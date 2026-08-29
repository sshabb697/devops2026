# Lab 05B — NodePort

**Time:** 15 minutes

---

## Part A — Apply NodePort (5 min)

```bash
kubectl apply -f hello-nodeport.yaml
kubectl get svc hello-nodeport
```

Note `PORT(S)` like `80:30080/TCP`.

---

## Part B — Browser (7 min)

**Docker Desktop:** try **http://localhost:30080**

If it fails, use port-forward on `hello-nodeport` the same way as Lab 05A.

---

## Part C — Cleanup optional (3 min)

Keep `hello` Deployment for Day 6. You may delete the extra Service:

```bash
kubectl delete svc hello-nodeport
```

Keep `hello` ClusterIP Service if you still have it.

---

## Deliverables

- [ ] Can explain ClusterIP vs NodePort in one sentence each

➡️ **Day 6:** [ConfigMaps and Secrets](../Day-06-ConfigMaps-and-Secrets/README.md)
