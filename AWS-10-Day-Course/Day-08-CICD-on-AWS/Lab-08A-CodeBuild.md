# Lab 08A — Build with CodeBuild

**Time:** 15 minutes
Uses the files in [`sample-app/`](./sample-app/) (`buildspec.yml`, `index.html`).

---

## Part A — Put the sample app on GitHub (5 min)

1. Create a new **public GitHub repo**, e.g. `aws-class-cicd`.
2. Copy the contents of `sample-app/` into it (keep the folder structure) and push:
   ```bash
   git init
   git add .
   git commit -m "AWS class CI/CD demo"
   git branch -M main
   git remote add origin https://github.com/YOU/aws-class-cicd.git
   git push -u origin main
   ```

---

## Part B — Create a CodeBuild project (7 min)

1. **CodeBuild → Create build project**.
2. Name: `class-build`.
3. **Source:** GitHub → connect your account → pick `aws-class-cicd`, branch `main`.
4. **Environment:** Managed image, Amazon Linux, Standard runtime. Let CodeBuild **create a new service role**.
5. **Buildspec:** "Use a buildspec file" (it reads `buildspec.yml` from the repo).
6. Create, then **Start build**.

---

## Part C — Read the logs (3 min)

- Open the running build → **Build logs**.
- You'll see your phases run: `install → pre_build → build → post_build`.
- The `pre_build` step prints **"index.html present"** — that's your test passing.
- Status goes **Succeeded** (green).

> **Homework idea:** break the build — rename `index.html` in the repo, push, and watch `pre_build` fail. Then fix it.

---

## If you get stuck

| Problem | Fix |
| ------- | --- |
| GitHub won't connect | Use the OAuth/app connection flow; repo must be accessible. |
| Build fails immediately | Check the `buildspec.yml` is at the **repo root**. |
| YAML error | Indentation — 2 spaces, no tabs. |

---

## Deliverables

- [ ] Sample app pushed to GitHub
- [ ] `class-build` project builds successfully
- [ ] Read the phase logs

➡️ Next: [02 — Pipelines and deployments](./02-Pipelines-and-Deploy.md)
