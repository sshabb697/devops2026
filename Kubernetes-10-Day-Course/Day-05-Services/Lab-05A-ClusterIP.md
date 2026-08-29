# Lab 05A — ClusterIP + port-forward

**Time:** 15 minutes  
Need Deployment `hello` from Day 4. If missing:

```bash
kubectl apply -f ../Day-04-ReplicaSets-and-Deployments/hello-deploy.yaml
```

---

## Part A — Create the Service (5 min)

```bash
kubectl apply -f hello-svc.yaml
kubectl get svc hello
kubectl describe svc hello
```

Find **Endpoints** — should list Pod IPs.

---

## Part B — Open in browser (7 min)

ClusterIP is **inside** the cluster only. From your laptop:

```bash
kubectl port-forward svc/hello 8080:80
```

Open **http://localhost:8080**

`Ctrl+C` when done.

---

## Part C — DNS name (3 min)

Inside the cluster the name is `hello` or `hello.default.svc.cluster.local`. You will use that on Day 7.

---

## Deliverables

- [ ] Service has Endpoints
- [ ] Browser worked via port-forward

➡️ Next: [02 — Service types](./02-Service-Types.md)
