# Bonus (optional) — Liveness probe

**Not in the 1-hour Day 4 class.** Do this at home or if a class finishes early.

Kubernetes can **check if the app is alive**. If the check fails, it **restarts** the container.

This idea is in the [AKS workshops 101 probes lab](https://github.com/sshabb697/aks-workshops) and the [official liveness docs](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/).

---

## Everyday analogy

A teacher asks “are you OK?” every few seconds.  
If you never answer, they send you out and bring a new student (restart).

---

## Lab (10–15 min)

Need a local cluster (`kubectl get nodes` works).

```bash
kubectl apply -f liveness-demo.yaml
kubectl get pods -w
```

Wait. The pod will **restart** on purpose (the app is written to fail the check after a while).

```bash
kubectl describe pod liveness-demo
```

Look for **Liveness probe failed** and **Restart Count** going up.

Cleanup:

```bash
kubectl delete -f liveness-demo.yaml
```

---

## One sentence

**livenessProbe** = “restart me if I am stuck.”  
**readinessProbe** = “do not send me traffic until I am ready.” (read later)
