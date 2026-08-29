# 01 — What is AKS

**Learning objectives**

- **AKS** = Kubernetes where Azure runs the **control plane**
- You still choose **node size** and pay for those VMs

---

## One-sentence idea

AKS is **managed Kubernetes on Azure** — you do not install etcd yourself.

![AKS managed](../images/k8s-aks-managed.png)

---

## Everyday analogy: rented kitchen vs owning a restaurant

You still cook (deploy YAML). Azure owns the building’s electricity and booking system (control plane). You pay for the cook stations (nodes).

| You | Azure |
| --- | ----- |
| Apps, YAML, images | API server, etcd, control plane upgrades |
| Worker VM size / count | Patching the control plane |
| `kubectl` | The AKS resource in the portal |

Same kubectl from Days 2–7. Only the **context** changes.

Two resource groups will appear: **yours** (`k8s-class-rg`) and **MC_...** (Azure-managed node resources). That is normal — see [aks-workshops lab-01 portal note](https://github.com/sshabb697/aks-workshops).

---

## Knowledge check

1. Do you SSH to etcd on AKS in this course?
2. Is the AKS control plane the same as your worker VMs?

<details>
<summary>Answers</summary>

1. No.  
2. No — control plane is managed; nodes are VMs you pay for.

</details>

➡️ Next: [Lab 08A](./Lab-08A-Azure-Login.md)
