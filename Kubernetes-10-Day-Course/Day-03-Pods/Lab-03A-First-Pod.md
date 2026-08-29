# Lab 03A — First nginx Pod

**Time:** 15 minutes  
Folder: `Kubernetes-10-Day-Course/Day-03-Pods/`

---

## Part A — Apply the YAML (5 min)

```bash
kubectl apply -f nginx-pod.yaml
kubectl get pods
kubectl get pods -o wide
```

Wait until `STATUS` is **Running**. First pull can take a minute.

---

## Part B — Open the page (5 min)

```bash
kubectl port-forward pod/nginx-demo 8080:80
```

Open **http://localhost:8080** — nginx welcome page.

Stop with `Ctrl+C`.

---

## Part C — Where is it running? (5 min)

```bash
kubectl describe pod nginx-demo
```

Find **Node:** and **IP:**. That is “which hotel floor / room.”

Leave the Pod running for Lab 03B.

---

## If you get stuck

| Error | Fix |
| ----- | --- |
| ImagePullBackOff | Internet / Docker running? |
| port 8080 in use | Use `8090:80` |

---

## Deliverables

- [ ] Pod Running
- [ ] Browser showed nginx

➡️ Next: [02 — Labels and exec](./02-Labels-and-Exec.md)
