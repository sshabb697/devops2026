# 02 — ClusterIP, NodePort, LoadBalancer

**Learning objectives**

- Pick the right type for laptop vs Azure

---

## One-sentence idea

**ClusterIP** = inside only. **NodePort** = a high port on the machine. **LoadBalancer** = cloud gives a public IP (AKS).

| Type | Who can call it | When we use it |
| ---- | --------------- | -------------- |
| ClusterIP | Other Pods | Default, internal |
| NodePort | Laptop → nodeIP:30000+ | Local demos |
| LoadBalancer | Internet (cloud) | Day 9 AKS |

On Docker Desktop, NodePort often maps to localhost. On AKS, LoadBalancer creates an Azure public IP (costs money).

---

## Knowledge check

1. Can the internet reach a ClusterIP on AKS?
2. Which type did the [aks-workshop lab](https://github.com/sshabb697/aks-workshop/tree/main/content/labs) switch to for a browser test?

<details>
<summary>Answers</summary>

1. No.  
2. LoadBalancer.

</details>

➡️ Next: [Lab 05B](./Lab-05B-NodePort.md)
