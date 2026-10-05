# Lab 09A — Build, push to ECR, run on ECS

**Time:** 15 minutes
Uses [`app/Dockerfile`](./app/Dockerfile) and [`app/index.html`](./app/index.html). Needs Docker running.

Set these first (replace with your values):
```bash
export ACCOUNT=123456789012
export REGION=eu-west-1
```

---

## Part A — Build and push to ECR (7 min)

```bash
# 1. Create the registry repo
aws ecr create-repository --repository-name class-app

# 2. Build the image (from the app/ folder)
cd app
docker build -t class-app:latest .

# 3. Log Docker in to ECR
aws ecr get-login-password --region $REGION | docker login --username AWS \
  --password-stdin $ACCOUNT.dkr.ecr.$REGION.amazonaws.com

# 4. Tag and push
docker tag class-app:latest $ACCOUNT.dkr.ecr.$REGION.amazonaws.com/class-app:latest
docker push $ACCOUNT.dkr.ecr.$REGION.amazonaws.com/class-app:latest
```

Confirm:
```bash
aws ecr list-images --repository-name class-app
```

---

## Part B — Run it on ECS Fargate (8 min)

Use the console wizard (fastest):
1. **ECS → Clusters → Create cluster** → name `class-cluster` → **AWS Fargate**. Create.
2. **Task definitions → Create new** → Fargate → name `class-task`.
   - Container name `web`, Image URI = your ECR image, Port **80**.
   - Smallest CPU/memory (0.25 vCPU / 0.5 GB). Create.
3. **Cluster → Services → Create** → launch type Fargate, task `class-task`, **1** task.
   - Networking: a public subnet, **assign public IP ON**, security group allowing port **80**.
   - Create.
4. When the task is **Running**, open its **public IP** → your container page loads.

---

## End of day — clean up 💸

```text
ECS → delete the service, then the cluster
ECR → delete the class-app repository (and images)
```

---

## If you get stuck

| Problem | Fix |
| ------- | --- |
| `docker login` fails | Re-run the `get-login-password` command; check ACCOUNT/REGION. |
| Task stuck PENDING | Public subnet + assign public IP + SG port 80 must all be set. |
| 403 pulling image | Task execution role needs ECR pull permission (wizard adds it). |

---

## Deliverables

- [ ] Image pushed to ECR
- [ ] Service running on ECS Fargate, page reachable
- [ ] Cleaned up service, cluster, and ECR repo

➡️ Next: [02 — EKS (managed Kubernetes)](./02-EKS.md)
