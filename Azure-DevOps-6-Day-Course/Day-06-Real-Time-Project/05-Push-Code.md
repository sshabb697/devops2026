# 05 - Push Code

## Overview

Now we'll put the Contoso Tasks application code into the repository. We'll use the **Node.js sample app**, but the steps are the same for any sample.

## Step 1 — Clone the Repo

```bash
git clone https://dev.azure.com/<org>/Contoso-Tasks/_git/contoso-tasks-app
cd contoso-tasks-app
```

## Step 2 — Add the Application Code

Copy the Node.js sample into the repo:

```bash
cp -r /path/to/Sample-Applications/NodeJS/* .
```

The app includes:
- `app.js` — an Express server with `/` and `/health` endpoints and a small tasks API.
- `app.test.js` — tests.
- `package.json` — scripts (`start`, `test`) and dependencies.
- `.gitignore`, `README.md`.
- `azure-pipelines.yml` — a starter CI pipeline (we'll build on it).

> If you can't access the sample folder, recreate the files from [Sample-Applications/NodeJS](../../Sample-Applications/NodeJS/).

## Step 3 — Verify Locally (optional but recommended)

```bash
npm install
npm test        # tests should pass
npm start       # visit http://localhost:3000 and /health
```

## Step 4 — Commit and Push to `main`

```bash
git add .
git commit -m "Add Contoso Tasks Node.js application"
git push origin main
```

✅ **Checkpoint:** Refresh **Repos → Files** — the app code is now in Azure Repos.

> If `main` is already protected (it won't be yet — we protect it next lesson), you'd push to a branch and open a PR instead. For this initial seed, pushing to `main` is fine.

## Step 5 — Create a Feature Branch (for the rest of the project)

From now on, follow GitHub Flow:

```bash
git checkout -b feature/12-health-endpoint
# make a small change, e.g., tweak the health message
git commit -am "Improve health endpoint message"
git push -u origin feature/12-health-endpoint
```

We'll turn this into a pull request after configuring branch policies.

## Verification

- [ ] App code is in the repo on `main`.
- [ ] Tests pass locally (`npm test`).
- [ ] A `feature/*` branch is pushed for the upcoming PR.

## Summary

- Cloned the repo and added the Node.js sample application.
- Verified the app/tests locally.
- Pushed the initial code to `main` and created a feature branch.

➡️ Next: [06 - Configure Branch Policies](./06-Configure-Branch-Policies.md)
