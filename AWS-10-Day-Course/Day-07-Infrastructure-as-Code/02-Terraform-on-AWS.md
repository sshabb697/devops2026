# 02 — Terraform on AWS

**Learning objectives**

- Know what **Terraform** is and how it differs from CloudFormation
- Understand the `init` → `plan` → `apply` → `destroy` flow

---

## One-sentence idea

Terraform is a **cloud-agnostic IaC tool** that builds infrastructure on AWS (and Azure, GCP, …) from simple **HCL** files.

---

## CloudFormation vs Terraform

| | CloudFormation | Terraform |
| - | -------------- | --------- |
| Made by | AWS | HashiCorp |
| Works on | AWS only | AWS, Azure, GCP, 1000+ providers |
| Language | YAML/JSON | HCL (cleaner to read) |
| State | Managed by AWS | A **state file** you manage (local or remote) |

Many teams prefer Terraform because one tool and one language covers **every** cloud. This repo has a whole [Terraform 5-Day Course](../../Terraform-5-Day-Course/).

---

## The HCL for an S3 bucket

```hcl
terraform {
  required_providers {
    aws = { source = "hashicorp/aws", version = "~> 5.0" }
  }
}

provider "aws" {
  region = "eu-west-1"
}

resource "aws_s3_bucket" "demo" {
  bucket = "aws-class-tf-amy-051026"
  tags   = { Project = "aws-class" }
}
```

Compare to the YAML from the CloudFormation lab — same result, different syntax.

---

## The core workflow

```bash
terraform init      # download the AWS provider
terraform plan      # preview: what WILL change (no changes yet)
terraform apply     # make it real (asks for confirmation)
terraform destroy   # delete everything it created
```

- **`plan`** is the safety net: read it before every `apply`.
- **State file** (`terraform.tfstate`) is how Terraform remembers what it made — never delete it by hand.

---

## Knowledge check

1. One big advantage of Terraform over CloudFormation?
2. What does `terraform plan` do?

<details>
<summary>Answers</summary>

1. It's multi-cloud — the same tool/language works on AWS, Azure, GCP, and more.
2. Shows a preview of exactly what will be created/changed/destroyed, without making any changes yet.

</details>

➡️ Next: [Lab 07B](./Lab-07B-Terraform.md)
