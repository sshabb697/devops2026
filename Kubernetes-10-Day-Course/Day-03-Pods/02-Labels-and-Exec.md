# 02 — Labels, exec, delete

**Learning objectives**

- **Labels** are stickers so Services can find Pods
- `exec` is “open a shell inside the lunchbox”
- Deleting a **naked Pod** is final — nothing recreates it (that is why we use Deployments tomorrow)

---

## One-sentence idea

Stickers (**labels**) say “this is the web app.” Tomorrow a Service will look for those stickers.

---

## Example: exec (like SSH, but into the Pod)

```bash
kubectl exec -it nginx-demo -- sh
# inside:
ls
exit
```

**Delete:**

```bash
kubectl delete pod nginx-demo
```

If you still need nginx, you must `apply` again. That pain is the lesson: **Pods should be managed by a Deployment.**

---

## Knowledge check

1. What label did we put on `nginx-demo`?
2. After `kubectl delete pod nginx-demo`, does Kubernetes recreate it?

<details>
<summary>Answers</summary>

1. `app: nginx`  
2. No — not unless a ReplicaSet/Deployment owns it.

</details>

➡️ Next: [Lab 03B](./Lab-03B-Exec-and-Labels.md)
