---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section { font-size: 26px; }
  h1 { color: #0078d4; }
  h2 { color: #106ebe; }
  table { font-size: 20px; }
  footer { color: #666; font-size: 14px; }
footer: Kubernetes 10-Day | Day 10 Capstone
---

# Day 10 — Scale, logs, cleanup
## Finish the habit. Stop the bill.

**Today’s win:** 3 copies + diagnose ImagePullBackOff + **delete AKS**.

---

# Scale vs more computers

```bash
kubectl scale deployment hello -n class --replicas=3
```

This adds **Pods**, not VMs.

More **nodes** later = cluster autoscaler (not today).

---

# Logs = the app diary

```bash
kubectl logs -n class deploy/hello --tail=30
```

If many pods: `-l app=hello`

---

# Lab 10A — 15 minutes

```bash
kubectl scale deployment hello -n class --replicas=3
kubectl get pods -n class
kubectl logs -n class deploy/hello --tail=30
```

Optional: Azure Portal → your AKS → Workloads.

---

# When it is broken — this order

![w:1000](../images/k8s-troubleshoot.png)

**get → describe → logs** before Google.

---

# Status cheat sheet

| You see | Meaning |
|---------|---------|
| Pending | No room, or still pulling |
| ImagePullBackOff | Wrong image name, or no ACR access |
| CrashLoopBackOff | App starts then dies — **read logs** |
| Running | Good |

---

# Lab 10B — capstone + delete

**Break on purpose:**

```bash
kubectl apply -f bad-image.yaml
kubectl get pods -n class
kubectl describe pod -n class -l app=broken
```

You **want** ImagePullBackOff. Then delete the bad YAML.

**Required — money:**

```bash
az group delete -n k8s-class-rg --yes --no-wait
```

Tutor checks no extra AKS is left.

---

# You can now

- Explain Pod, Deployment, Service, AKS in simple words
- Deploy nginx on AKS
- Scale and read logs
- Follow get → describe → logs

Later (not this course): HPA, Ingress on AKS, GitOps.

---

# Thank you

10 hours. You did the labs.

Keep: `Command-Cheat-Sheet.md`

Delete Azure leftovers **today**.
