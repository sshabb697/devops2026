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
footer: Kubernetes 10-Day | Day 6 Config and Secrets
---

# Day 6 — ConfigMaps and Secrets
## Change a greeting. Don’t rebuild the image.

**Today’s win:** see `WELCOME=Hello class` inside a Pod.

---

# Sticky note vs locked drawer

![w:1050](../images/k8s-configmap-secret.png)

---

# ConfigMap = settings

Like TV **language** and **volume**.  
You do not buy a new TV to change them.

Examples: welcome text, theme, log level.

**Not** for passwords.

---

# Lab 06A — 15 minutes

```bash
kubectl apply -f config-demo.yaml
kubectl logs config-demo
kubectl exec config-demo -- printenv WELCOME
```

Change the YAML welcome text → apply → **delete the Pod** → apply again  
(env vars are read at start).

---

# Secret = passwords

Same idea as ConfigMap. Different **kind**.

Class password is fake: `class123`  
**Never** put real passwords in GitHub.

Kubernetes Secrets are **not** a magic vault. Still better than plain text in the image.

---

# Lab 06B — 15 minutes

```bash
kubectl create secret generic db-secret --from-literal=password=class123
kubectl apply -f secret-demo.yaml
kubectl exec secret-demo -- printenv DB_PASSWORD
```

Then **delete** the demos:

```bash
kubectl delete pod config-demo secret-demo --ignore-not-found
kubectl delete configmap class-config
kubectl delete secret db-secret
```

---

# Recap

| Kind | Use |
|------|-----|
| ConfigMap | Theme, welcome, ports |
| Secret | Password, token |

**Tomorrow:** files that survive (or don’t) + one front door (Ingress).
