---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section { font-size: 28px; }
  h1 { color: #0078d4; }
  h2 { color: #106ebe; }
  table { font-size: 20px; }
  footer { color: #666; font-size: 14px; }
footer: Kubernetes 10-Day | Day 4 Deployments
---

# Day 4 — ReplicaSet and Deployment
## Keep 3 copies. Update. Undo.

**Today’s win:** delete one Pod — a new one appears.

---

# The stack (remember this picture)

![w:1000](../images/k8s-replicaset-deployment.png)

---

# ReplicaSet = babysitter

Rule: **always 3 Pods** with this sticker.

If you throw one away, it prints another copy.

You rarely write ReplicaSets at work.  
**Deployments** create them for you. We look at one so the picture is clear.

---

# Lab 04A — 15 minutes

```bash
kubectl apply -f nginx-rs.yaml
kubectl get rs
kubectl get pods -l app=web
kubectl delete pod PUT_THE_NAME_HERE
kubectl get pods -l app=web -w
```

Watch a **new name** appear. `Ctrl+C` to stop.

Then: `kubectl delete -f nginx-rs.yaml`

---

# Deployment = the one you use at work

Deployment = ReplicaSet **plus**:

- new image (update)
- **rolling** replace (old → new, little downtime)
- **undo** if the new image is bad

```bash
kubectl scale deployment hello --replicas=3
kubectl rollout undo deployment/hello
```

---

# Tiny Deployment (idea)

```yaml
kind: Deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: hello
  template:
    metadata:
      labels:
        app: hello
    spec:
      containers:
        - name: hello
          image: nginx
```

Selector stickers **must** match Pod stickers.

---

# Lab 04B — 15 minutes

```bash
kubectl apply -f hello-deploy.yaml
kubectl scale deployment hello --replicas=3
kubectl set image deployment/hello hello=nginx:1.27
kubectl rollout status deployment/hello
kubectl rollout undo deployment/hello
```

**Leave `hello` running** for Day 5.

---

# Recap

| Object | Job |
|--------|------|
| Pod | One running copy |
| ReplicaSet | Keep N copies |
| Deployment | Updates + rollback |

**Tomorrow:** how users **reach** the app (Service).
