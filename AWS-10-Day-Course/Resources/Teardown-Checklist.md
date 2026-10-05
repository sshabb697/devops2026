# Teardown Checklist — delete everything

Run through this at the **end of the course** (and ideally end of each day). AWS charges by the hour — a forgotten resource is a real bill.

Go **region by region** (check the Region selector, top-right of the console).

## Order matters (delete dependents first)

1. **EKS / ECS**
   - [ ] Delete EKS node groups, then the EKS cluster.
   - [ ] Delete ECS services, then the cluster. Deregister task definitions.
2. **Load balancers & Auto Scaling**
   - [ ] Delete ALBs/NLBs and target groups.
   - [ ] Delete Auto Scaling groups and launch templates.
3. **Compute**
   - [ ] Terminate all **EC2** instances (`Project=aws-class`).
   - [ ] Delete unattached **EBS** volumes and old snapshots.
4. **Databases**
   - [ ] Delete **RDS** instances (skip final snapshot for class DBs).
5. **Serverless / CI-CD**
   - [ ] Delete **Lambda** functions, **CodePipeline**, **CodeBuild** projects.
6. **Storage**
   - [ ] Empty and delete **S3** buckets (`aws s3 rb s3://NAME --force`).
   - [ ] Delete **ECR** repositories (and their images).
7. **Networking (do this LAST)**
   - [ ] Delete **NAT Gateways** (biggest hidden cost!).
   - [ ] Release **Elastic IPs**.
   - [ ] Delete custom **VPCs** (removes subnets, route tables, IGWs).
8. **IaC**
   - [ ] `aws cloudformation delete-stack` for any class stacks.
9. **Identity**
   - [ ] Deactivate/delete temporary **IAM** access keys.

## Verify nothing is left

```bash
aws resourcegroupstaggingapi get-resources --tag-filters Key=Project,Values=aws-class
```

- [ ] **Billing dashboard** shows no new charges building up.
- [ ] Billing alarm from Day 1 is still armed.
