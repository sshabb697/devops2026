# Lab 07A — Deploy a CloudFormation stack

**Time:** 15 minutes
Uses [`stack.yaml`](./stack.yaml) — it creates an S3 bucket (with versioning) and a security group.

---

## Part A — Validate and deploy (7 min)

From the `Day-07-Infrastructure-as-Code/` folder:

```bash
# 1. Validate the template syntax
aws cloudformation validate-template --template-body file://stack.yaml

# 2. Deploy it as a stack (pick a UNIQUE bucket name)
aws cloudformation deploy \
  --template-file stack.yaml \
  --stack-name class-stack \
  --parameter-overrides BucketName=aws-class-cfn-amy-051026
```

Watch the events:
```bash
aws cloudformation describe-stack-events --stack-name class-stack \
  --query "StackEvents[].[ResourceStatus,ResourceType]" --output table
```

---

## Part B — See the outputs (4 min)

```bash
aws cloudformation describe-stacks --stack-name class-stack \
  --query "Stacks[0].Outputs" --output table
```

You'll see the **BucketArn** and **SecurityGroupId**. Confirm the bucket exists:
```bash
aws s3 ls | grep cfn
```

Also open **CloudFormation** in the console → your stack → **Resources** tab to see what it built.

---

## Part C — Update, then delete (4 min)

Edit `stack.yaml`: change `ProjectTag` default from `aws-class` to `aws-class-day7`, redeploy, and note CloudFormation only updates the tags (a *change set*):
```bash
aws cloudformation deploy --template-file stack.yaml --stack-name class-stack \
  --parameter-overrides BucketName=aws-class-cfn-amy-051026
```

Then tear the whole thing down with **one** command:
```bash
aws cloudformation delete-stack --stack-name class-stack
```

> One command created **and** destroyed everything — that's the power of IaC.

---

## If you get stuck

| Problem | Fix |
| ------- | --- |
| `BucketName already exists` | Names are global — make it more unique. |
| Stack `ROLLBACK_COMPLETE` | Delete the stack, fix the error, redeploy. |
| Delete fails (bucket not empty) | Empty the bucket first: `aws s3 rm s3://NAME --recursive`. |

---

## Deliverables

- [ ] Stack `class-stack` deployed from the template
- [ ] Viewed its outputs and resources
- [ ] Deleted the stack (everything gone)

➡️ Next: [02 — Terraform on AWS](./02-Terraform-on-AWS.md)
