# 01 — What is a Pod

**Learning objectives**

- A **Pod** is the smallest thing Kubernetes runs
- Usually **one container** per Pod (two only when they must share a disk or network)

---

## One-sentence idea

A Pod is a **wrapper** around your container(s) — like a lunchbox around a sandwich.

![Pod](../images/k8s-pod.png)

---

## Everyday analogy: a lunchbox

The sandwich is the **container** (nginx). The lunchbox is the **Pod**. Kubernetes moves lunchboxes, not loose sandwiches.

**Example YAML** (also in `nginx-pod.yaml`):

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-demo
  labels:
    app: nginx
spec:
  containers:
    - name: web
      image: nginx
      ports:
        - containerPort: 80
```

`image: nginx` is the same idea as `docker run nginx`.

---

## Knowledge check

1. Is a Pod the same as a Docker container?
2. Can one Pod hold two containers?

<details>
<summary>Answers</summary>

1. Almost — a Pod *contains* one or more containers.  
2. Yes, but beginners should use one.

</details>

➡️ Next: [Lab 03A](./Lab-03A-First-Pod.md)
