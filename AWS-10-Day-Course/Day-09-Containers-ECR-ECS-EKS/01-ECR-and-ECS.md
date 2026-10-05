# 01 — ECR and ECS

**Learning objectives**

- Know what **ECR** (registry) and **ECS** (orchestrator) are
- Understand **Fargate** vs EC2 launch type

---

## One-sentence idea

**ECR** is a private warehouse for your container images; **ECS** is the service that runs those images as containers.

---

## Quick recap: what's a container?

A **container** packages your app + everything it needs into one portable box. It runs the same on any machine. An **image** is the saved blueprint; a **container** is a running copy. (Full detail in the Docker course.)

---

## ECR — Elastic Container Registry

A private place to store your images, like Docker Hub but inside your AWS account.

```bash
# 1. Log Docker in to your ECR
aws ecr get-login-password | docker login --username AWS \
  --password-stdin ACCOUNT.dkr.ecr.REGION.amazonaws.com
# 2. Tag and push
docker tag class-app:latest ACCOUNT.dkr.ecr.REGION.amazonaws.com/class-app:latest
docker push ACCOUNT.dkr.ecr.REGION.amazonaws.com/class-app:latest
```

---

## ECS — Elastic Container Service

ECS **runs and manages** containers for you: starts them, restarts crashed ones, scales them.

| ECS term | Meaning | Analogy |
| -------- | ------- | ------- |
| **Task definition** | Recipe: which image, CPU, memory, ports | A blueprint |
| **Task** | One running copy of the task definition | One running container |
| **Service** | Keeps N tasks running, handles scaling | A manager keeping staff on shift |
| **Cluster** | Where tasks run | The building |

---

## Fargate vs EC2 launch type

| | Fargate | EC2 launch type |
| - | ------- | --------------- |
| You manage | Nothing — AWS runs the servers | You manage the EC2 hosts |
| Pay for | Just the task's CPU/memory | The EC2 instances |
| Best for | Simplicity (great for class) | Fine-grained control/cost at scale |

**Fargate = serverless containers.** No servers to patch. We'll use it in the lab.

---

## Knowledge check

1. What's the difference between ECR and ECS?
2. What does Fargate save you from managing?

<details>
<summary>Answers</summary>

1. ECR stores container images; ECS runs them as containers.
2. Managing the underlying servers (EC2 hosts) — Fargate runs containers without you provisioning VMs.

</details>

➡️ Next: [Lab 09A](./Lab-09A-ECR-and-ECS.md)
