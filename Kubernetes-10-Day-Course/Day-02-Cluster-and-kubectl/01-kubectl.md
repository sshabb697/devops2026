# 01 — kubectl (your remote control)

**Learning objectives**

- Know kubectl is a **client**, like a TV remote
- Know it reads a **kubeconfig** file (which cluster to talk to)

---

## One-sentence idea

**kubectl** is the command you type. The cluster does the work.

![kubectl flow](../images/k8s-kubectl-flow.png)

---

## Everyday analogy: a TV remote

The remote is not the TV. If the batteries are dead (wrong kubeconfig), buttons do nothing.

| You type | Meaning |
| -------- | ------- |
| `kubectl get nodes` | List the hotel floors |
| `kubectl get pods` | List guests (apps) |
| `kubectl apply -f file.yaml` | “Make the cluster match this shopping list” |

---

## Example

```bash
kubectl version --client
kubectl get nodes
```

You should see at least one node with status **Ready**.

If you later have **local** Kubernetes *and* **AKS**, you switch with:

```bash
kubectl config get-contexts
kubectl config use-context docker-desktop
```

(AKS context names look like `aks-class`.)

This matches the [Kubelabs kubectl for beginners](https://collabnix.github.io/kubelabs/) idea: Docker users already know a CLI; kubectl is the Kubernetes CLI.

---

## Knowledge check

1. Does kubectl run your nginx process itself?
2. What file tells kubectl *which* cluster to use?

<details>
<summary>Answers</summary>

1. No — the kubelet on a node starts the container.  
2. kubeconfig (often `~/.kube/config`).

</details>

➡️ Next: [Lab 02A](./Lab-02A-Enable-Kubernetes.md)
