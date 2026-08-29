# 01 — Scale and logs

**Learning objectives**

- More users → more **replicas** (HPA is a later course)
- Logs are the first place to look

---

## One-sentence idea

**Scale** = more copies. **Logs** = the app’s diary.

```bash
kubectl scale deployment hello -n class --replicas=3
kubectl logs -n class -l app=hello --tail=20
```

[aks-workshops workshop 5](https://github.com/sshabb697/aks-workshops) covers HPA and KEDA — mention only: “the cluster can scale itself later.”

---

## Knowledge check

1. Does `scale --replicas=3` add worker VMs by itself?
2. Where do you read stdout of the container?

<details>
<summary>Answers</summary>

1. No — that is more **Pods**. Cluster autoscaler (later) adds **nodes**.  
2. `kubectl logs`.

</details>

➡️ Next: [Lab 10A](./Lab-10A-Scale-Logs.md)
