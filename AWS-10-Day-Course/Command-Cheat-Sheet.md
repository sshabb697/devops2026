# AWS command cheat sheet

Copy-paste friendly. Use **PowerShell** or **bash**. Needs [AWS CLI v2](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

Longer official list: [AWS CLI reference](https://docs.aws.amazon.com/cli/latest/reference/)

---

## Setup and identity

```bash
aws --version
aws configure                       # enter Access Key, Secret, region, output
aws sts get-caller-identity         # "who am I?"
aws configure list
export AWS_REGION=eu-west-1          # bash   (PowerShell: $env:AWS_REGION="eu-west-1")
```

---

## IAM (Day 2)

```bash
aws iam list-users
aws iam create-user --user-name dev-amy
aws iam create-group --group-name developers
aws iam attach-group-policy --group-name developers \
  --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess
aws iam add-user-to-group --user-name dev-amy --group-name developers
```

---

## EC2 (Day 3)

```bash
aws ec2 describe-instances --query "Reservations[].Instances[].InstanceId"
aws ec2 describe-instances --filters "Name=tag:Project,Values=aws-class"
aws ec2 create-key-pair --key-name class-key --query KeyMaterial --output text > class-key.pem
aws ec2 start-instances  --instance-ids i-0123456789abcdef0
aws ec2 stop-instances   --instance-ids i-0123456789abcdef0
aws ec2 terminate-instances --instance-ids i-0123456789abcdef0
ssh -i class-key.pem ec2-user@PUBLIC_IP
```

---

## VPC (Day 4)

```bash
aws ec2 describe-vpcs
aws ec2 describe-vpcs --filters Name=isDefault,Values=true
aws ec2 describe-subnets --filters "Name=vpc-id,Values=vpc-0abc123"
aws ec2 describe-route-tables
aws ec2 describe-security-groups
```

---

## S3 (Day 5)

```bash
aws s3 ls
aws s3 mb s3://aws-class-UNIQUE-NAME
aws s3 cp index.html s3://aws-class-UNIQUE-NAME/
aws s3 sync ./site s3://aws-class-UNIQUE-NAME
aws s3 rb s3://aws-class-UNIQUE-NAME --force   # remove bucket + contents
```

---

## RDS (Day 6)

```bash
aws rds describe-db-instances --query "DBInstances[].DBInstanceIdentifier"
aws rds stop-db-instance  --db-instance-identifier class-db
aws rds delete-db-instance --db-instance-identifier class-db --skip-final-snapshot
```

---

## CloudFormation (Day 7)

```bash
aws cloudformation deploy --template-file stack.yaml --stack-name class-stack \
  --capabilities CAPABILITY_NAMED_IAM
aws cloudformation describe-stacks --stack-name class-stack
aws cloudformation delete-stack --stack-name class-stack
```

---

## Containers: ECR / ECS / EKS (Day 9)

```bash
aws ecr get-login-password | docker login --username AWS --password-stdin ACCOUNT.dkr.ecr.REGION.amazonaws.com
aws ecr create-repository --repository-name class-app
aws ecs list-clusters
aws eks update-kubeconfig --name class-eks --region eu-west-1
kubectl get nodes
```

---

## Lambda + CloudWatch (Day 10)

```bash
aws lambda list-functions
aws lambda invoke --function-name class-fn out.json
aws logs tail /aws/lambda/class-fn --follow
aws cloudwatch describe-alarms
```

---

## Cleanup helpers (run at end of day)

```bash
aws ec2 describe-instances --filters "Name=tag:Project,Values=aws-class" \
  --query "Reservations[].Instances[].InstanceId" --output text
aws resourcegroupstaggingapi get-resources --tag-filters Key=Project,Values=aws-class
```

> Golden rule: **tag everything `Project=aws-class`**, then you can always find what to delete.
