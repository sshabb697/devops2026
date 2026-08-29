# 01 — Same YAML, new cluster

**Learning objectives**

- YAML from Days 3–5 works on AKS
- Always check **context** so you do not deploy to Docker Desktop by mistake

---

## One-sentence idea

Kubernetes language did not change. Only the **computers** are in Azure now.

---

## Example: check context first

```bash
kubectl config current-context
```

Should mention `aks-class`. If you see `docker-desktop`, run:

```bash
az aks get-credentials -g k8s-class-rg -n aks-class --overwrite-existing
```

Namespaces still work — [aks-workshop managing-aks](https://github.com/sshabb697/aks-workshop/blob/main/content/labs/03.managing-aks.md) creates `helloapp`. We will use `class`.

---

## Knowledge check

1. Why check context?
2. Is `kubectl apply` different on AKS?

<details>
<summary>Answers</summary>

1. So labs do not land on the laptop cluster.  
2. Same command; different API server.

</details>

➡️ Next: [Lab 09A](./Lab-09A-Deploy.md)
