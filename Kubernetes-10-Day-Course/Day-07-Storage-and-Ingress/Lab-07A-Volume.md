# Lab 07A — emptyDir

**Time:** 15 minutes

---

## Part A — Write a file (6 min)

```bash
kubectl apply -f vol-demo.yaml
kubectl exec vol-demo -- cat /data/note.txt
```

Expected: `hello`

---

## Part B — Delete the Pod (6 min)

```bash
kubectl delete pod vol-demo
kubectl apply -f vol-demo.yaml
kubectl exec vol-demo -- cat /data/note.txt
```

The file exists again only because the **command writes it at start**. If you had typed extra lines by hand, they would be **gone**. That is emptyDir.

---

## Part C — Cleanup (3 min)

```bash
kubectl delete pod vol-demo
```

---

## Deliverables

- [ ] Can explain emptyDir vs PVC in one sentence

➡️ Next: [02 — Ingress](./02-Ingress.md)
