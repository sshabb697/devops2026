# AWS 10-Day Course

Hands-on **AWS for DevOps** for **new students**, including people who are **not from IT**. Each class is **1 hour**. You will see a short story, one example, then a lab.

> Goal: **launch, secure, and automate** apps on AWS — from your first EC2 server to containers, CI/CD, and serverless.

Print or keep open: **[Command Cheat Sheet](./Command-Cheat-Sheet.md)** · Tutors: **[Tutor Notes](./Tutor-Notes.md)**

This course is a classroom-friendly reshaping of the community favourite [aws-devops-zero-to-hero](https://github.com/iam-veeramalla/aws-devops-zero-to-hero) by Abhishek Veeramalla (30 days → 10 focused days), plus the **official [AWS documentation](https://docs.aws.amazon.com/)** and **[AWS Skill Builder](https://skillbuilder.aws/)**.

**After class (optional):** [Resources/Useful-Links.md](./Resources/Useful-Links.md) · [Optional homework by day](./Resources/Optional-Homework.md)

---

## What you will be able to do

By Day 10 you can:

1. Explain cloud, regions, and Availability Zones with a simple analogy.
2. Create IAM users/roles and follow least-privilege security.
3. Launch an EC2 server, deploy a web app, and reach it from the internet.
4. Design a VPC with public/private subnets, route tables, and gateways.
5. Store data in S3, host a static website, and use RDS for a database.
6. Automate infrastructure with CloudFormation (and Terraform on AWS).
7. Build a CI/CD pipeline with CodeBuild, CodeDeploy, and CodePipeline.
8. Run containers on ECR + ECS, and deploy to EKS.
9. Write a Lambda function and monitor everything with CloudWatch.
10. Tear everything down cleanly to avoid surprise bills.

| Day | Topic | Outcome |
| --- | ----- | ------- |
| [Day 1](./Day-01-Cloud-and-AWS-Fundamentals/) | Cloud + AWS fundamentals | Account ready; console, regions, billing understood |
| [Day 2](./Day-02-IAM/) | IAM | Users, groups, roles, least-privilege policies |
| [Day 3](./Day-03-EC2-Compute/) | EC2 compute | Web app live on an EC2 server |
| [Day 4](./Day-04-Networking-VPC/) | Networking (VPC) | Public + private subnets with routing |
| [Day 5](./Day-05-Storage-S3-EBS/) | Storage (S3 + EBS) | Bucket, versioning, static website |
| [Day 6](./Day-06-Databases-and-CLI/) | Databases + AWS CLI | RDS database + scripting with the CLI |
| [Day 7](./Day-07-Infrastructure-as-Code/) | IaC (CloudFormation) | One template builds a full stack |
| [Day 8](./Day-08-CICD-on-AWS/) | CI/CD on AWS | Pipeline builds and deploys automatically |
| [Day 9](./Day-09-Containers-ECR-ECS-EKS/) | Containers | Image in ECR, app on ECS/EKS |
| [Day 10](./Day-10-Serverless-Monitoring-Capstone/) | Serverless + monitoring + capstone | Lambda, CloudWatch, full cleanup |

---

## Class timing (every day = 60 minutes)

| Block | Minutes |
| ----- | ------- |
| Lesson A (talk + picture) | 10 |
| Lab A (students do it) | 15 |
| Lesson B | 10 |
| Lab B | 15 |
| Recap / questions | 10 |

**After every lesson there is a lab.** Do not skip labs. AWS only sticks when you click and type the commands yourself.

---

## Prerequisites

- An **AWS account** (the [Free Tier](https://aws.amazon.com/free/) is enough for almost everything here).
- A **credit/debit card** is required to open the account — AWS may place a small temporary hold.
- Comfort with a terminal (`cd`, `ls` / `dir`). The [Linux 5-Day Course](../Linux-5-Day-Course/) helps.
- [AWS CLI v2](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) installed from Day 6 onward.
- For containers (Day 9): basic Docker — see the [Docker 5-Day Course](../Docker-5-Day-Course/).

> **Money warning:** EC2, RDS, NAT Gateways, ECS/EKS and load balancers **cost money** beyond the Free Tier. Use the **smallest sizes**, and **delete resources at the end of every day** (Day 10 has a full teardown checklist).

---

## How to teach / study

1. Read the **one-sentence idea**.
2. Walk through the **example / console click-path**.
3. Students complete the **lab**.
4. Use the **cheat sheet** when someone forgets a command.
5. **Tag everything** with `Project=aws-class` so cleanup is easy.

**If something fails:** read the error, check the **Region** (top-right of the console), and confirm your IAM permissions.

---

## Course layout

```
AWS-10-Day-Course/
├── README.md
├── Command-Cheat-Sheet.md
├── Tutor-Notes.md
├── Resources/        ← extra links, optional homework, teardown
└── Day-01- … Day-10- …
```

---

## Connects to other courses in this repo

| Before this course | After this course |
| ------------------ | ----------------- |
| [Linux 5-Day Course](../Linux-5-Day-Course/) | [Terraform 5-Day Course](../Terraform-5-Day-Course/) (IaC on Azure/AWS) |
| [Docker 5-Day Course](../Docker-5-Day-Course/) | [Kubernetes 10-Day Course](../Kubernetes-10-Day-Course/) (EKS is managed Kubernetes) |
| | [Azure DevOps 6-Day Course](../Azure-DevOps-6-Day-Course/) (compare CI/CD platforms) |
