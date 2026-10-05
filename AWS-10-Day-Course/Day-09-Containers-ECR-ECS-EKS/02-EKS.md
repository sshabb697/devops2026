# 02 — EKS (managed Kubernetes)

**Learning objectives**

- Know what **EKS** is and when to pick it over ECS
- Understand the managed control plane + worker nodes

---

## One-sentence idea

**EKS** is **Kubernetes, run for you by AWS** — you get the standard Kubernetes API without managing the control plane.

---

## ECS vs EKS

| | ECS | EKS |
| - | --- | --- |
| Orchestrator | AWS's own | **Kubernetes** (open standard) |
| Portability | AWS-only | Runs anywhere Kubernetes runs |
| Complexity | Simpler | More moving parts, more power |
| Pick when | You're all-in on AWS, want simple | You use Kubernetes already / multi-cloud |

If your team already knows `kubectl` and YAML manifests, EKS lets you reuse all of it. (That's the whole [Kubernetes 10-Day Course](../../Kubernetes-10-Day-Course/).)

---

## What AWS manages vs what you manage

```text
┌──────────────── AWS manages ────────────────┐
│  EKS control plane (API server, etcd, …)     │  ← highly available, patched
└──────────────────────────────────────────────┘
┌──────────────── You manage ──────────────────┐
│  Worker nodes (EC2 or Fargate)               │
│  Your Deployments, Services, Ingress (YAML)  │
└──────────────────────────────────────────────┘
```

You pay ~$0.10/hour for the control plane **plus** the worker nodes.

---

## Connecting kubectl to EKS

```bash
aws eks update-kubeconfig --name class-eks --region eu-west-1
kubectl get nodes
kubectl apply -f deployment.yaml
kubectl get svc        # the LoadBalancer gives you a public URL
```

One command (`update-kubeconfig`) wires `kubectl` to your EKS cluster. After that it's **normal Kubernetes**.

---

## Knowledge check

1. What does AWS run for you in EKS, and what do you still run?
2. When would you choose EKS over ECS?

<details>
<summary>Answers</summary>

1. AWS manages the control plane; you manage worker nodes and your Kubernetes workloads (manifests).
2. When you already use Kubernetes, want portability/multi-cloud, or need its rich ecosystem.

</details>

➡️ Next: [Lab 09B](./Lab-09B-EKS.md)
