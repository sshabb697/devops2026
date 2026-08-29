# Lab 10B — Capstone and cleanup

**Time:** 15 minutes  
**Most important:** delete the resource group so you are not billed.

---

## Part A — Break on purpose (5 min)

```bash
kubectl apply -f bad-image.yaml
kubectl get pods -n class
kubectl describe pod -n class -l app=broken
```

Expected: **ImagePullBackOff** or ErrImagePull. This is success — you diagnosed it.

```bash
kubectl delete -f bad-image.yaml
```

---

## Part B — Delete Azure (8 min) — required

```bash
az group delete -n k8s-class-rg --yes --no-wait
```

Confirm in the portal later: `k8s-class-rg` is gone. The `MC_*` group goes away with it.

If you used a different group name, delete **that** name.

---

## Part C — What you can do now (2 min)

You can:

- Explain Pod, Deployment, Service, AKS
- Deploy nginx on AKS with a public IP
- Scale and read logs

Next learning: HPA, Ingress on AKS, GitOps (Flux) — [aks-workshops](https://github.com/sshabb697/aks-workshops) workshops 4–6.

---

## Deliverables

- [ ] Diagnosed ImagePullBackOff
- [ ] Started resource group delete
- [ ] Tutor checked no extra AKS clusters remain

Congratulations — 10 hours complete.
