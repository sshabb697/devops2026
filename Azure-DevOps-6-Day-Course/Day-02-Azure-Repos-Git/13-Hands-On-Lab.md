# 13 - Hands-On Lab: Git & Azure Repos End-to-End

## Goal

Practice the full Git + Azure Repos workflow: clone a repo, branch, commit, push, open a pull request, configure branch policies, and resolve a merge conflict.

**Estimated time:** 60 minutes

## Prerequisites

- Completed the Day 1 lab (you have `Course-Project`).
- Git installed and configured (Day 2, lesson 03).

---

## Part 1 — Get the Repository URL

1. In your project, go to **Repos → Files**.
2. Click **Clone** (top right) and copy the HTTPS URL. It looks like:
   ```
   https://dev.azure.com/<org>/Course-Project/_git/Course-Project
   ```

---

## Part 2 — Clone and Make the First Commit

```bash
git clone https://dev.azure.com/<org>/Course-Project/_git/Course-Project
cd Course-Project

# Add a README and a .gitignore
echo "# Course Project" > README.md
printf "node_modules/\n.env\nbin/\nobj/\n" > .gitignore

git add .
git commit -m "Add README and .gitignore"
git push origin main
```

✅ **Checkpoint:** Refresh **Repos → Files** — you should see your files.

> If `main` already has files, run `git pull origin main` first.

---

## Part 3 — Create a Feature Branch

```bash
git checkout -b feature/add-greeting
echo "console.log('Hello, world!');" > app.js
git add app.js
git commit -m "Add greeting script"
git push -u origin feature/add-greeting
```

---

## Part 4 — Configure a Branch Policy on `main`

1. Go to **Repos → Branches**.
2. Next to `main`, click **⋯ → Branch policies**.
3. Enable:
   - **Require a minimum number of reviewers** → set to **1**.
   - **Check for linked work items** (optional for this lab).
   - **Check for comment resolution**.
4. Save.

✅ **Checkpoint:** `main` now shows a policy/shield icon.

---

## Part 5 — Open a Pull Request

1. Azure Repos shows a **"Create a pull request"** banner for your pushed branch — click it (or **Repos → Pull requests → New**).
2. Source: `feature/add-greeting`, Target: `main`.
3. Add a **title** and **description**.
4. Click **Create**.
5. Notice the policy status: it requires 1 reviewer.

**Approve it** (as the author you may need a second account, or temporarily lower the reviewer count / use "Approve" if your permissions allow). Then **Complete** the PR:
- Choose **Squash commit**.
- Check **Delete `feature/add-greeting` after merging**.

✅ **Checkpoint:** `app.js` now appears on `main`; the feature branch is gone.

---

## Part 6 — Create and Resolve a Merge Conflict

Simulate two diverging changes.

```bash
git checkout main
git pull origin main

# Branch A
git checkout -b feature/change-a
echo "const greeting = 'Hello from A';" > app.js
git commit -am "Change greeting (A)"
git push -u origin feature/change-a

# Back to main, make a conflicting change directly via a second branch
git checkout main
git checkout -b feature/change-b
echo "const greeting = 'Hi from B';" > app.js
git commit -am "Change greeting (B)"
git push -u origin feature/change-b
```

1. Open a PR for **feature/change-b** → merge it into `main` (approve + complete).
2. Now open a PR for **feature/change-a** → Azure Repos reports a **conflict** with `main`.

Resolve locally:
```bash
git checkout feature/change-a
git fetch origin
git merge origin/main
# CONFLICT in app.js — edit the file to the final desired content:
#   const greeting = 'Hello from A and B';
git add app.js
git commit
git push
```

3. The PR updates and the conflict clears. Complete the PR.

✅ **Checkpoint:** You resolved a real merge conflict.

---

## Part 7 — Create a Tag

```bash
git checkout main
git pull origin main
git tag -a v1.0.0 -m "First release"
git push origin v1.0.0
```

✅ **Checkpoint:** See it under **Repos → Tags**.

---

## Deliverables / Verification

- [ ] Files committed and pushed to `main`.
- [ ] A feature branch merged via a **pull request**.
- [ ] A **branch policy** configured on `main`.
- [ ] A **merge conflict** resolved.
- [ ] A **tag** (`v1.0.0`) created and pushed.

---

## Reflection Questions

1. Why did the direct push to a protected `main` need a pull request instead?
2. Which merge type did you use, and why might a team standardize on squash?
3. What practices would have reduced the merge conflict?

---

🎉 **Great work!** You now control source code like a pro. Tomorrow you'll automate building and shipping it with Azure Pipelines.

➡️ Continue to [Day 3 — Azure Pipelines](../Day-03-Azure-Pipelines/README.md)
