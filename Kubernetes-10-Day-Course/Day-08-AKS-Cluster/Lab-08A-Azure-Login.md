# Lab 08A — Azure login and resource group

**Time:** 15 minutes  
Need: Azure account, [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli). Cloud Shell at [https://shell.azure.com](https://shell.azure.com) also works ([aks-workshop setup](https://github.com/sshabb697/aks-workshop/blob/main/content/labs/00.setup.md)).

---

## Part A — Login (5 min)

```bash
az login
az account show
```

Confirm the **correct subscription** (school vs personal).

---

## Part B — Resource group (5 min)

Use a region your tutor chooses. Example `eastus`:

```bash
az group create -n k8s-class-rg -l eastus
az group show -n k8s-class-rg -o table
```

---

## Part C — kubectl on this machine (5 min)

```bash
az aks install-cli
kubectl version --client
```

On Windows, open a **new** terminal if `kubectl` is not found (PATH).

---

## Deliverables

- [ ] Logged in
- [ ] `k8s-class-rg` exists

➡️ Next: [02 — AKS and ACR](./02-AKS-and-ACR.md)
