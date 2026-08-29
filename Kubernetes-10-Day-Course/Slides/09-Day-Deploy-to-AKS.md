---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section { font-size: 28px; }
  h1 { color: #0078d4; }
  h2 { color: #106ebe; }
  table { font-size: 22px; }
  footer { color: #666; font-size: 14px; }
footer: Kubernetes 10-Day | Day 9 Deploy to AKS
---

# Day 9 — Deploy to AKS
## Same YAML. Computers are in Azure.

**Today’s win:** nginx in the browser on an Azure **EXTERNAL-IP**.

---

# Check the remote first

```bash
kubectl config current-context
```

Must look like **aks-class**.

If you see `docker-desktop`, you are on the laptop. Fix:

```bash
az aks get-credentials -g k8s-class-rg -n aks-class --overwrite-existing
```

---

# Namespace still works

We use folder **`class`** so class work is easy to find.

```bash
kubectl apply -f hello-aks.yaml
kubectl get all -n class
```

YAML language did **not** change. Only the cluster did.

---

# Lab 09A — 15 minutes

Folder: `Day-09-Deploy-to-AKS/`

```bash
kubectl get nodes
kubectl apply -f hello-aks.yaml
kubectl get all -n class
```

Wait for **2** pods Running.

Service is still **ClusterIP** — no public website yet.

---

# LoadBalancer = public doorbell

Azure creates a **public IP** in front of the Service.

`EXTERNAL-IP` stays `<pending>` for a few minutes. That is normal.

This is the same idea as the AKS workshop: ClusterIP → LoadBalancer.

---

# Lab 09B — 15 minutes

```bash
kubectl apply -f hello-lb.yaml
kubectl get svc hello -n class -w
```

When you see a real IP, open: `http://THAT_IP`  
(use **http**, not https)

Optional extra: build your own image in ACR (`az acr build`). nginx is enough for class.

---

# Recap

1. Always check **context**
2. `-n class` on get/apply
3. Public IP costs a little — we delete tomorrow

**Tomorrow:** scale, broken image, **delete the resource group**.
