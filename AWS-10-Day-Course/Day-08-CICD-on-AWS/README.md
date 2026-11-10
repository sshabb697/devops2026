# Day 8 — CI/CD on AWS

**Goal:** Automate build and deployment. Understand CodeBuild, CodeDeploy, and CodePipeline, and wire a source → build → deploy pipeline.

## Core path (~60 min)

| # | Item | Time |
| - | ---- | ---- |
| 01 | [Lesson — CI/CD and the AWS Code* services](./01-CICD-and-Code-Services.md) | 10m |
| 03 | [Lesson — CodeBuild demo](./03-CodeBuild-Demo.md) | 10m |
| Lab | [Lab 08A — Build with CodeBuild](./Lab-08A-CodeBuild.md) | 15m |
| 02 | [Lesson — Pipelines and deployments](./02-Pipelines-and-Deploy.md) | 10m |
| 04 | [Lesson — CodePipeline demo (2- and 4-stage)](./04-CodePipeline-Demo.md) | 10m |
| Lab | [Lab 08B — A CodePipeline end to end](./Lab-08B-CodePipeline.md) | 15m |
| | Recap | 10m |

**Day 8 deliverable:** a pipeline that automatically builds on every commit and deploys the result.

> **Note:** AWS CodeCommit is closed to new accounts — use **GitHub** as the source instead (shown in the labs). KodeKloud screenshots may still show CodeCommit/S3 → CodeDeploy → EC2; the ideas are the same.

> **Images:** [`../images/day-08-cicd/`](../images/day-08-cicd/) from [KodeKloud AWS CodePipeline (CI/CD Pipeline)](https://notes.kodekloud.com/docs/AWS-CodePipeline-CICD-Pipeline). Index: [images README](../images/README.md).

> **Money:** Delete pipelines, CodeBuild projects, deploy buckets, and any demo EC2/CodeDeploy apps when done.

**Go further (optional):** [CodePipeline docs](https://docs.aws.amazon.com/codepipeline/) · [CodeBuild buildspec reference](https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html) · [KodeKloud notes](https://notes.kodekloud.com/docs/AWS-CodePipeline-CICD-Pipeline)
