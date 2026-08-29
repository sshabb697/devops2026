# Lab 08B — Create ACR and AKS

**Time:** 15 minutes of *your* time. Cluster create can take **10–15 extra minutes** — start it before the break if needed.

**Use bash** (Cloud Shell or Git Bash). PowerShell: `$ACR="k8sclass$NUMBER"` style.

---

## Part A — Names (2 min)

```bash
NUMBER=$RANDOM
ACR="k8sclass${NUMBER}acr"
echo $ACR
```

Write the name down. ACR must be unique.

---

## Part B — ACR (3 min)

```bash
az acr create -g k8s-class-rg -n $ACR --sku Basic
```

---

## Part C — AKS, 1 small node (start this; wait)

```bash
az aks create -g k8s-class-rg -n aks-class \
  --node-count 1 \
  --node-vm-size Standard_B2s \
  --generate-ssh-keys \
  --attach-acr $ACR
```

If `Standard_B2s` is not allowed, tutor picks another small size.

---

## Part D — Connect kubectl (when create finishes)

```bash
az aks get-credentials -g k8s-class-rg -n aks-class --overwrite-existing
kubectl get nodes
kubectl get ns
```

Expected: 1 node **Ready**. Namespaces like Day 2.

**Portal:** search `k8s-class-rg` and also `MC_k8s-class-rg_aks-class_eastus` (name varies by region).

---

## If create is still running at the bell

Students finish Part D as homework. Do not create a second cluster.

---

## Deliverables

- [ ] ACR created
- [ ] `kubectl get nodes` on **aks-class** (today or tonight)

➡️ **Day 9:** [Deploy to AKS](../Day-09-Deploy-to-AKS/README.md)
