# Day 8 — AKS cluster

**Goal:** Create a small AKS cluster and talk to it with kubectl.  
Adapted from [aks-workshops Lab-01](https://github.com/sshabb697/aks-workshops) and [aks-workshop 02.basic-aks](https://github.com/sshabb697/aks-workshop/tree/main/content/labs).

| # | Item | Time |
| - | ---- | ---- |
| 01 | [Lesson — What is AKS](./01-What-is-AKS.md) | 10m |
| Lab | [Lab 08A — Azure login and resource group](./Lab-08A-Azure-Login.md) | 15m |
| 02 | [Lesson — ACR + AKS together](./02-AKS-and-ACR.md) | 10m |
| Lab | [Lab 08B — Create AKS](./Lab-08B-Create-AKS.md) | 15m |
| | Recap | 10m |

**Cost warning:** AKS worker VMs cost money. Use **1 node**. Delete everything on **Day 10**.

**Day 8 deliverable:** `kubectl get nodes` against **AKS** shows Ready.

**Go further (optional):** [What is AKS?](https://learn.microsoft.com/azure/aks/what-is-aks) · [Microsoft Learn: Intro to Kubernetes](https://learn.microsoft.com/training/modules/intro-to-kubernetes/)
