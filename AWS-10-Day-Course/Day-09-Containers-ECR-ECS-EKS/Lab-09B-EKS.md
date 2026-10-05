# Lab 09B — Deploy to EKS

**Time:** 15 minutes
Uses [`k8s/deployment.yaml`](./k8s/deployment.yaml) and the image you pushed to ECR in Lab 09A.

> EKS costs money (control plane + nodes). **Create it, use it, delete it the same day.** The fastest path is [`eksctl`](https://eksctl.io/).

Set your values:
```bash
export ACCOUNT=123456789012
export REGION=eu-west-1
```

---

## Part A — Create a tiny cluster (~10 min to build) (4 min to run)

```bash
eksctl create cluster \
  --name class-eks \
  --region $REGION \
  --nodes 1 \
  --node-type t3.small \
  --managed
```

This builds the control plane + **1** worker node. It takes ~10–15 minutes — start it, then read the EKS lesson again while it builds. When done:
```bash
kubectl get nodes      # one node, Ready
```

---

## Part B — Deploy your image (6 min)

1. Point the manifest at your image. Edit [`k8s/deployment.yaml`](./k8s/deployment.yaml) and replace `ACCOUNT` and `REGION`, **or** use sed:
   ```bash
   sed -i "s/ACCOUNT/$ACCOUNT/g; s/REGION/$REGION/g" k8s/deployment.yaml
   ```
2. Apply it:
   ```bash
   kubectl apply -f k8s/deployment.yaml
   kubectl get pods         # 2 pods Running
   kubectl get svc          # wait for the LoadBalancer EXTERNAL-IP
   ```
3. Open the LoadBalancer URL (an ELB DNS name) → your container page loads, served by Kubernetes on AWS.

---

## Part C — Scale (2 min)

```bash
kubectl scale deployment class-app --replicas=4
kubectl get pods         # now 4
```

---

## End of day — DELETE the cluster 💸 (critical!)

```bash
eksctl delete cluster --name class-eks --region $REGION
```

This removes the control plane, nodes, and the load balancer. **Do not skip this** — EKS bills by the hour.

---

## If you get stuck

| Problem | Fix |
| ------- | --- |
| `eksctl` not found | Install eksctl; it uses your AWS CLI credentials. |
| Pods `ImagePullBackOff` | ACCOUNT/REGION in the image URL wrong, or node role lacks ECR pull. |
| No EXTERNAL-IP | Wait 2–3 min for the ELB to provision. |

---

## Deliverables

- [ ] `class-eks` cluster with 1 node
- [ ] App deployed, reachable via the LoadBalancer
- [ ] Scaled to 4 pods
- [ ] **Cluster deleted** at end of day

➡️ Next day: [Day 10 — Serverless, Monitoring & Capstone](../Day-10-Serverless-Monitoring-Capstone/)
