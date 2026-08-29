# Lab 06A — ConfigMap

**Time:** 15 minutes

---

## Part A — Apply (5 min)

```bash
kubectl apply -f config-demo.yaml
kubectl get configmap class-config -o yaml
kubectl get pod config-demo
```

Wait until Running.

---

## Part B — Read the settings (7 min)

```bash
kubectl logs config-demo
```

Expected: `WELCOME=Hello class THEME=blue`

```bash
kubectl exec config-demo -- printenv WELCOME
```

---

## Part C — Change the note (3 min)

Edit `config-demo.yaml` — set `WELCOME: "Good afternoon"`, apply again.

For env from ConfigMap, **restart the Pod** so it picks up the new value:

```bash
kubectl delete pod config-demo
kubectl apply -f config-demo.yaml
kubectl logs config-demo
```

---

## Deliverables

- [ ] Logs show the welcome text

➡️ Next: [02 — Secrets](./02-Secrets.md)
