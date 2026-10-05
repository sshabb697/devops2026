# 01 — CI/CD and the AWS Code* services

**Learning objectives**

- Explain **CI** and **CD** in plain words
- Match each AWS service to a pipeline stage

---

## One-sentence idea

CI/CD is a **conveyor belt** that takes your code from commit to running app, automatically.

---

## CI and CD in plain words

- **CI — Continuous Integration:** every time someone pushes code, it's automatically **built and tested**. Catch breakage early.
- **CD — Continuous Delivery/Deployment:** the tested build is automatically **deployed** to servers.

```text
Commit ─▶ Build & test (CI) ─▶ Deploy (CD) ─▶ Running app
```

No more "it worked on my machine" and no manual copy-to-server at 2am.

---

## The AWS Code* family

| Service | Job | Analogy |
| ------- | --- | ------- |
| **CodeCommit** | Git hosting (legacy; use GitHub now) | The warehouse of code |
| **CodeBuild** | Compile, test, package | The factory machine |
| **CodeDeploy** | Push the build to EC2/ECS/Lambda | The delivery van |
| **CodePipeline** | Orchestrate all the stages | The conveyor belt tying it together |

> Think of **CodePipeline** as the manager that calls CodeBuild, then CodeDeploy, in order, on every change.

---

## buildspec.yml — CodeBuild's instructions

CodeBuild reads a `buildspec.yml` from your repo:

```yaml
version: 0.2
phases:
  install:
    commands: [ "echo installing" ]
  build:
    commands: [ "echo building", "npm test" ]
artifacts:
  files: [ "**/*" ]
```

- **phases** run in order: install → pre_build → build → post_build.
- **artifacts** are the output files handed to the next stage.

---

## Knowledge check

1. What's the difference between CI and CD?
2. Which service orchestrates the whole flow?

<details>
<summary>Answers</summary>

1. CI automatically builds and tests every change; CD automatically deploys the tested build.
2. CodePipeline — it ties source, build (CodeBuild), and deploy (CodeDeploy) together.

</details>

➡️ Next: [Lab 08A](./Lab-08A-CodeBuild.md)
