# 02 — Deployment (the one you use at work)

**Learning objectives**

- **Deployment** = ReplicaSet + **updates** (new image, rollout, undo)
- This is the YAML you will see in real jobs

---

## One-sentence idea

A Deployment is the **project plan**: how many copies, which image, how to replace old with new.

---

## Example

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello
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

**Scale:** `kubectl scale deployment hello --replicas=4`  
**Update:** change the image, `kubectl apply -f ...`  
**Undo:** `kubectl rollout undo deployment/hello`

Same story as [Kubelabs Deployment101](https://collabnix.github.io/kubelabs/) and [AKS workshop lab-06](https://github.com/sshabb697/aks-workshops).

---

## Knowledge check

1. Should beginners create naked Pods in production?
2. What command rolls back a bad image?

<details>
<summary>Answers</summary>

1. No — use a Deployment.  
2. `kubectl rollout undo deployment/NAME`

</details>

➡️ Next: [Lab 04B](./Lab-04B-Deployment.md)
