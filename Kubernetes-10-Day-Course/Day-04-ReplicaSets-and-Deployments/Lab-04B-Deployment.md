# Lab 04B — Scale, update, undo

**Time:** 15 minutes

---

## Part A — Deploy (4 min)

```bash
kubectl apply -f hello-deploy.yaml
kubectl get deploy
kubectl get pods -l app=hello
```

---

## Part B — Scale (4 min)

```bash
kubectl scale deployment hello --replicas=3
kubectl get pods -l app=hello
```

Expected: 3 pods.

---

## Part C — Rolling update and undo (7 min)

```bash
kubectl set image deployment/hello hello=nginx:1.27
kubectl rollout status deployment/hello
kubectl rollout history deployment/hello
kubectl rollout undo deployment/hello
kubectl rollout status deployment/hello
```

Leave `hello` running for **Day 5**.

---

## Deliverables

- [ ] Scaled to 3
- [ ] Rollout and undo ran without error

➡️ **Day 5:** [Services](../Day-05-Services/README.md)
