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
footer: Kubernetes 10-Day | Day 7 Storage and Ingress
---

# Day 7 — Storage and Ingress
## USB stick for files. Front door for websites.

**Today’s win:** “PVC asks for a disk. Ingress is the mall directory.”

---

# Files in a container can vanish

If you write only inside the container,  
**delete Pod** = file gone.

A **volume** is a USB stick you plug into the Pod.

---

# PVC vs PV

![w:1000](../images/k8s-volume-pvc.png)

- **PVC** = “I need 1Gi disk” (the request)
- **PV** = the real disk Azure (or the lab) gives you
- **emptyDir** = whiteboard for **this** Pod only (good for class)

---

# Lab 07A — 15 minutes

```bash
kubectl apply -f vol-demo.yaml
kubectl exec vol-demo -- cat /data/note.txt
kubectl delete pod vol-demo
```

emptyDir dies with the Pod.  
(The YAML writes `hello` again on start — extra handwritten notes would be lost.)

---

# Ingress = mall reception

![w:1000](../images/k8s-ingress.png)

One address.  
`/` → shop. `/api` → API.

YAML is a **sign**.  
**Ingress Controller** is the person who reads the sign.

---

# Service vs Ingress

| | Service | Ingress |
|--|---------|---------|
| Job | Phone number for **one** app | Directory for **many** apps |
| Example | `hello:80` | `shop.example.com/` |

LoadBalancer is a **Service type**. Ingress sits **in front**.

---

# Lab 07B — 15 minutes

1. Read `shop-ingress.yaml` — circle Deployment, Service, Ingress
2. `kubectl apply -f shop-ingress.yaml`
3. `kubectl get ingress` — empty ADDRESS = **no controller yet** (OK today)

Optional if time: install ingress-nginx (see the lab file).

---

# Recap

1. emptyDir ≠ backup
2. PVC = please give me a disk
3. Ingress needs a controller to work

**Tomorrow:** **AKS** — Kubernetes on Azure. Costs money. One small node.
