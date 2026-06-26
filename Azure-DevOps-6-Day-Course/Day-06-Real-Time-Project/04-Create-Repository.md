# 04 - Create Repository

## Overview

Every project gets a default Git repository named after the project. We'll use it (or create a dedicated one) to hold the Contoso Tasks application code.

## Option A — Use the Default Repo

A repo named `Contoso-Tasks` already exists under **Repos → Files**. You can use it directly.

## Option B — Create a New Repo

1. **Repos → Files** → click the repo dropdown → **+ New repository**.
2. Type: **Git**, name: `contoso-tasks-app`.
3. Toggle **Add a README** to initialize it (so it's not empty).
4. **Create**.

## Initialize the Repo (if empty)

If the repo is empty, add a README and a `.gitignore` from the UI:

1. **Repos → Files → Initialize** (offers README + `.gitignore` template).
2. Choose the **Node** `.gitignore` template (we're using the Node.js app).
3. Commit.

Or do it from the command line (next lesson).

## Get the Clone URL

1. **Repos → Files → Clone**.
2. Copy the **HTTPS** URL:
   ```
   https://dev.azure.com/<org>/Contoso-Tasks/_git/contoso-tasks-app
   ```
3. Authentication uses Git Credential Manager, a PAT, or SSH (Day 2, lesson 03).

## Plan the Branching Strategy

For Contoso Tasks we'll use **GitHub Flow** (Day 2, lesson 06):
- `main` is always deployable and **protected**.
- Short-lived `feature/*` branches → PR → merge to `main`.

Branch naming: `feature/<work-item-id>-<description>` (e.g., `feature/12-create-task`).

## Verification

- [ ] A Git repository exists for the app.
- [ ] It's initialized (README + `.gitignore`).
- [ ] You have the clone URL.
- [ ] Branching strategy decided (GitHub Flow).

## Summary

- Created/initialized the application repository.
- Added a Node `.gitignore` and README.
- Chose **GitHub Flow** with protected `main` and `feature/*` branches.

➡️ Next: [05 - Push Code](./05-Push-Code.md)
