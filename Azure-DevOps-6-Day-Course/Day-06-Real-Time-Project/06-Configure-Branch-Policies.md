# 06 - Configure Branch Policies

## Overview

To enforce quality, we'll protect `main` so that changes can only arrive via reviewed pull requests that pass a build. This applies Day 2 (lesson 08) and sets up the gate that our CI pipeline will satisfy.

## Step 1 — Open Branch Policies

1. **Repos → Branches**.
2. Next to `main`, click **⋯ → Branch policies**.

## Step 2 — Configure Policies

Enable the following:

- **Require a minimum number of reviewers:** `1`
  - ☑ Reset code reviewer votes when there are new changes.
  - ☑ Prohibit the most recent pusher from approving their own changes (separation of duties).
- **Check for linked work items:** Required (ties code to Boards).
- **Check for comment resolution:** Required.
- **Limit merge types:** allow **Squash** only (clean history).

> We'll add **Build validation** in lesson 07 after the CI pipeline exists.

## Step 3 — Save

Save the policies. `main` now shows a shield/lock icon and **direct pushes are blocked**.

## Step 4 — Test the Protection

Try pushing directly to `main`:

```bash
git checkout main
echo "// direct edit" >> app.js
git commit -am "direct change"
git push origin main      # ← should be REJECTED by policy
```

You'll get a rejection telling you to use a pull request. Undo the local commit:

```bash
git reset --hard origin/main
```

✅ **Checkpoint:** `main` rejects direct pushes; changes must go through PRs.

## Why These Policies?

| Policy | Benefit |
| ------ | ------- |
| Min reviewers | Peer review catches issues |
| No self-approval | Separation of duties |
| Linked work items | Traceability to Boards |
| Comment resolution | Nothing slips through review |
| Squash only | Clean, linear history |
| (Soon) Build validation | Code must compile & tests pass |

## Verification

- [ ] `main` requires a PR with ≥1 reviewer.
- [ ] Self-approval prohibited.
- [ ] Linked work item + comment resolution required.
- [ ] Direct push to `main` is rejected.

## Summary

- Protected `main` with branch policies: required reviewer, no self-approval, linked work items, comment resolution, squash-only merges.
- Verified that direct pushes are now blocked.
- Build validation will be added once the CI pipeline exists.

➡️ Next: [07 - Create Build Pipeline](./07-Create-Build-Pipeline.md)
