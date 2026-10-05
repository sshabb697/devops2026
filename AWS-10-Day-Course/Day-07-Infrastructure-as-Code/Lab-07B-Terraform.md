# Lab 07B — The same bucket with Terraform

**Time:** 15 minutes
Uses [`terraform/main.tf`](./terraform/main.tf). Needs [Terraform installed](https://developer.hashicorp.com/terraform/install).

> Your AWS CLI credentials from Day 6 are reused automatically by Terraform.

---

## Part A — init and plan (6 min)

```bash
cd terraform
terraform init      # downloads the AWS provider
terraform plan -var="bucket_name=aws-class-tf-amy-051026"
```

Read the plan: it shows **3 to add** (bucket, versioning, and the bucket's config) and **0 to destroy**. Nothing has changed yet.

---

## Part B — apply (5 min)

```bash
terraform apply -var="bucket_name=aws-class-tf-amy-051026"
# type: yes
```

Confirm it exists:
```bash
aws s3 ls | grep tf
terraform output bucket_arn
```

Look at the files Terraform created: `terraform.tfstate` (its memory of what exists).

---

## Part C — destroy (4 min)

```bash
terraform destroy -var="bucket_name=aws-class-tf-amy-051026"
# type: yes
```

Everything Terraform made is removed. Compare the experience to CloudFormation in Lab 07A — same outcome, different tool.

---

## If you get stuck

| Problem | Fix |
| ------- | --- |
| `No valid credential sources` | Run `aws configure` (Day 6) first. |
| `BucketAlreadyExists` | Change the `bucket_name` value — it's global. |
| `terraform: command not found` | Install Terraform and reopen the terminal. |

---

## Deliverables

- [ ] `terraform apply` created the bucket
- [ ] Saw the state file and output
- [ ] `terraform destroy` removed everything

➡️ Next day: [Day 8 — CI/CD on AWS](../Day-08-CICD-on-AWS/)
