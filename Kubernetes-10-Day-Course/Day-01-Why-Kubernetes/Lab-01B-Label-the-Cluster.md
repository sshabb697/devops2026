# Lab 01B — Label the cluster

**Time:** 15 minutes  
**Tools:** print the architecture picture or open `images/k8s-architecture.png`.

---

## Part A — Circle the pieces (8 min)

On the picture, write these labels (or number them):

1. Where **you** stand (`kubectl`)
2. **API server**
3. **etcd**
4. One **worker node**
5. A **Pod**

Tutor walks around and checks labels.

---

## Part B — Match (5 min)

| If this breaks… | What students notice |
| --------------- | -------------------- |
| API server down | |
| One worker dies | |
| etcd lost (disaster) | |

Write a short guess. Then discuss:

- API server down → `kubectl` fails; existing Pods may still run for a while.
- One worker dies → Pods on **other** nodes can still run; Kubernetes reschedules.
- etcd lost → the cluster forgets its memory (this is why AKS manages etcd for you).

---

## Part C — Homework sentence (2 min)

Finish this sentence in the chat or notebook:

> “Tomorrow we will install a cluster so that kubectl can talk to the ________.”

Expected: **API server**.

---

## Deliverables

- [ ] Picture labeled
- [ ] One sentence about AKS: Azure runs the **brain**; you still have **worker VMs**

➡️ **Day 2:** [Cluster and kubectl](../Day-02-Cluster-and-kubectl/README.md)
