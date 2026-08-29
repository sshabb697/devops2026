# 02 — Secrets (passwords)

**Learning objectives**

- Secrets are for **passwords, tokens, keys**
- They are **base64**, not strong encryption by default — still better than plain YAML in git if you are careless, but **do not commit real secrets**

---

## One-sentence idea

A Secret is a **locked drawer**. Same injection as ConfigMap; different kind.

---

## Example

```bash
kubectl create secret generic db-secret --from-literal=password=class123 --dry-run=client -o yaml
```

In class we use a fake password. On a job, use Azure Key Vault later — out of scope for this hour.

---

## Knowledge check

1. Is a Kubernetes Secret fully encrypted at rest everywhere by default?
2. Should `password: hunter2` sit in GitHub?

<details>
<summary>Answers</summary>

1. Not a magic vault — treat as sensitive, enable encryption at rest on real clusters.  
2. Never.

</details>

➡️ Next: [Lab 06B](./Lab-06B-Secret.md)
