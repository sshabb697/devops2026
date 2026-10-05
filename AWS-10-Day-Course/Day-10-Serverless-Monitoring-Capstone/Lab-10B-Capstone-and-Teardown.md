# Lab 10B — Capstone + full teardown

**Time:** 15 minutes
Bring the course together, then leave your account clean.

---

## Part A — Mini capstone (7 min)

Pick **one** that fits your time. Each reuses skills from the week:

**Option 1 — Serverless greeting API**
1. Add an **API Gateway** HTTP trigger to `class-fn` (Lambda → Add trigger → API Gateway → HTTP API → Open).
2. Open the generated URL in a browser → your Lambda responds over the internet.

**Option 2 — Monitored web server**
1. Launch a `t2.micro` EC2 with the Day 3 user-data (web page).
2. Create a **CloudWatch alarm** on its **CPUUtilization > 70%** → notify your SNS topic.
3. SSH in and run `yes > /dev/null &` to spike CPU; watch the alarm flip to **In alarm**, then `kill %1`.

**Option 3 — IaC rebuild**
1. Use the Day 7 `stack.yaml` or Terraform to recreate the bucket + security group in **one command**, then destroy it.

---

## Part B — Full teardown (8 min) 💸

Work through the master checklist: **[Resources/Teardown-Checklist.md](../Resources/Teardown-Checklist.md)**.

Quick sweep by region:
```bash
# What's still tagged for this class?
aws resourcegroupstaggingapi get-resources --tag-filters Key=Project,Values=aws-class

# Common leftovers
aws ec2 describe-instances --filters "Name=instance-state-name,Values=running" \
  --query "Reservations[].Instances[].InstanceId" --output text
aws s3 ls
aws rds describe-db-instances --query "DBInstances[].DBInstanceIdentifier"
aws eks list-clusters
```

**Highest-cost items to double-check are gone:**
- [ ] NAT Gateways (Day 4)
- [ ] EKS clusters (Day 9)
- [ ] RDS instances (Day 6)
- [ ] Running EC2 instances (Days 3–9)
- [ ] Load balancers (Days 8–9)

Keep your **Day 1 billing alarm** armed as a safety net.

---

## You did it 🎓

Over 10 days you went from "what is the cloud?" to deploying containers, pipelines, and serverless functions — and cleaning it all up like a pro.

**Where to go next:**
- [Terraform 5-Day Course](../../Terraform-5-Day-Course/) — go deeper on IaC.
- [Kubernetes 10-Day Course](../../Kubernetes-10-Day-Course/) — master what EKS runs.
- [Observability 5-Day Course](../../Observability-5-Day-Course/) — Prometheus, Loki, Grafana.
- Prep for the **AWS Certified Cloud Practitioner** or **Solutions Architect – Associate**.

---

## Deliverables

- [ ] Completed one capstone option
- [ ] Ran the teardown checklist
- [ ] `get-resources` shows nothing left running
- [ ] Billing alarm still active
