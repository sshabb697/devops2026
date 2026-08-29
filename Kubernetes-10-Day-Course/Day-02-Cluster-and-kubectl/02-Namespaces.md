# 02 — Namespaces (folders in the cluster)

**Learning objectives**

- Treat a **namespace** like a folder
- Know `default` vs `kube-system`

---

## One-sentence idea

A **namespace** keeps school work from mixing with the hotel’s own staff.

---

## Everyday analogy: school lockers

- `default` — your locker (where we put class apps)
- `kube-system` — staff only (DNS, metrics). **Do not delete this.**

**Example:** two teams, `team-blue` and `team-green`, can both have a Pod named `web`. Namespaces stop the name clash.

```bash
kubectl get namespaces
```

You will see `default`, `kube-system`, `kube-public`, `kube-node-lease`.

---

## Knowledge check

1. Should students deploy apps into `kube-system`?
2. Can two Pods have the same name in two namespaces?

<details>
<summary>Answers</summary>

1. No.  
2. Yes.

</details>

➡️ Next: [Lab 02B](./Lab-02B-First-Commands.md)
