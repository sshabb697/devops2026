# 02 — Cluster architecture

**Learning objectives**

- Name **control plane** vs **worker node**
- Know that you talk to the **API server**, not to each machine by hand

---

## One-sentence idea

A **cluster** is a group of computers. The **brain** (control plane) decides. The **hands** (worker nodes) run your apps.

![Kubernetes architecture](../images/k8s-architecture.png)

---

## Two kinds of machines

| Piece | Job | Simple example |
| ----- | --- | -------------- |
| **Control plane** | Remember what you asked for; schedule Pods | The hotel front desk |
| **Worker node** | Run Pods | A floor of rooms |
| **kubelet** | Agent on each node: “start this Pod” | Housekeeping |
| **etcd** | Stores cluster data | The booking book |

On **AKS** (Day 8), Azure runs the control plane for you. You still pay for worker VMs.

---

## Example: you type a command

You will soon type:

```bash
kubectl run demo --image=nginx
```

What happens (simplified):

1. `kubectl` sends a request to the **API server**.
2. The **scheduler** picks a worker that has space.
3. The **kubelet** on that worker starts a **Pod** with nginx.

You never SSH into every VM to run Docker by hand.

---

## Knowledge check

1. Where does `kubectl` send commands?
2. Do your nginx Pods usually run on the control plane or on workers?
3. What is etcd for?

<details>
<summary>Answers</summary>

1. The API server.  
2. Workers.  
3. Cluster memory — the source of truth.

</details>

➡️ Next: [Lab 01B](./Lab-01B-Label-the-Cluster.md)
