# Lab 08B — A CodePipeline end to end

**Time:** 15 minutes
Builds a Source → Build → Deploy pipeline from the repo you made in Lab 08A.

> Deploy target options: **S3** (simplest, no server) or **EC2 via CodeDeploy**. We'll use **S3** to keep it cheap and fast; EC2 steps are noted at the end.

---

## Part A — Create the pipeline (8 min)

1. **CodePipeline → Create pipeline** → *Build custom pipeline*.
2. Name: `class-pipeline`. Let it create a new service role.
3. **Source:** GitHub (version 2) → connect → repo `aws-class-cicd`, branch `main`.
4. **Build:** CodeBuild → choose your `class-build` project (from Lab 08A).
5. **Deploy:** **Amazon S3** → pick/create a bucket `aws-class-deploy-amy-051026` → tick **Extract file before deploy**.
6. Create the pipeline. It runs automatically.

---

## Part B — Watch it flow (4 min)

- The pipeline shows three stages going green: **Source → Build → Deploy**.
- Enable static website hosting on the deploy bucket (Day 5) and open the URL — you see the demo page.

```text
git push ─▶ Source ✅ ─▶ Build ✅ ─▶ Deploy to S3 ✅ ─▶ live
```

---

## Part C — Prove automation (3 min)

1. Edit `index.html` in your GitHub repo (change the heading text). Commit to `main`.
2. Within a minute the pipeline **re-runs by itself**.
3. Refresh the website — your change is live. **No manual deploy.**

---

## EC2 deploy (optional, if time)

To deploy to EC2 instead of S3: install the **CodeDeploy agent** on an EC2 instance, create a **CodeDeploy application + deployment group**, and point the Deploy stage at it. It uses the `appspec.yml` and `scripts/restart_server.sh` from `sample-app/`.

---

## End of day — clean up 💸

- Delete the pipeline, the CodeBuild project, and both S3 buckets.
- Terminate any EC2 instance you created for CodeDeploy.

---

## If you get stuck

| Problem | Fix |
| ------- | --- |
| Source stage fails | Reconnect the GitHub connection; check branch name. |
| Deploy to S3 fails | Pipeline role needs `s3:PutObject` on the bucket. |
| Website shows old page | Hard-refresh (Ctrl+F5); check the Deploy stage finished. |

---

## Deliverables

- [ ] `class-pipeline` runs Source → Build → Deploy
- [ ] A commit auto-triggers a redeploy
- [ ] Cleaned up pipeline + buckets

➡️ Next day: [Day 9 — Containers (ECR, ECS, EKS)](../Day-09-Containers-ECR-ECS-EKS/)
