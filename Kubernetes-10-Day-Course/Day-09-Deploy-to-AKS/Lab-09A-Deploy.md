# Lab 09A — Namespace and Deployment on AKS

**Time:** 15 minutes  
Folder: `Day-09-Deploy-to-AKS/`

---

## Part A — Context (3 min)

```bash
kubectl config current-context
kubectl get nodes
```

---

## Part B — Apply (7 min)

```bash
kubectl apply -f hello-aks.yaml
kubectl get all -n class
```

Wait until 2/2 pods Running.

---

## Part C — Inside-only Service (5 min)

```bash
kubectl get svc -n class
```

Type is **ClusterIP**. No public website yet. That is the next lesson.

---

## Deliverables

- [ ] Pods Running in namespace `class`

➡️ Next: [02 — LoadBalancer](./02-LoadBalancer.md)
