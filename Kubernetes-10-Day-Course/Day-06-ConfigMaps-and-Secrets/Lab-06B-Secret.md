# Lab 06B — Secret

**Time:** 15 minutes

---

## Part A — Create a Secret (5 min)

```bash
kubectl create secret generic db-secret --from-literal=password=class123
kubectl get secret db-secret
```

---

## Part B — Use it in a Pod (7 min)

```bash
kubectl apply -f secret-demo.yaml
kubectl get pod secret-demo
kubectl exec secret-demo -- printenv DB_PASSWORD
```

Expected: `class123`

---

## Part C — Cleanup (3 min)

```bash
kubectl delete pod config-demo secret-demo --ignore-not-found
kubectl delete configmap class-config
kubectl delete secret db-secret
```

Keep the `hello` Deployment from Day 4 if it is still there.

---

## Deliverables

- [ ] Printed `DB_PASSWORD` from the Pod
- [ ] Deleted the demo Secret so it does not linger

➡️ **Day 7:** [Storage and Ingress](../Day-07-Storage-and-Ingress/README.md)
