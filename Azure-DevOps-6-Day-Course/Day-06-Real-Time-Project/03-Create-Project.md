# 03 - Create Project

## Overview

Now create the **project** that will contain the Contoso Tasks repository, pipelines, and boards.

## Steps

1. From the organization home → **+ New project**.
2. Configure:
   - **Project name:** `Contoso-Tasks`
   - **Description:** `Task management web app — CI/CD with Azure DevOps`
   - **Visibility:** Private
3. Expand **Advanced**:
   - **Version control:** Git
   - **Work item process:** Agile
4. **Create**.

## Configure the Project

Apply Day 5 (lesson 12):

1. **Project settings → Overview → Azure DevOps services** — keep **Boards, Repos, Pipelines** on; you can hide **Test Plans/Artifacts** if unused.
2. **Project settings → Teams** — the default `Contoso-Tasks Team` exists; add members if simulating the team.
3. **Boards → Project configuration → Iterations** — create a couple of sprints (e.g., Sprint 1, Sprint 2) for planning.

## (Optional) Seed Some Work Items

To connect Boards with the delivery (Day 4):

1. **Boards → Backlogs** → create an **Epic**: `Task Management MVP`.
2. Add a **Feature**: `Task API`.
3. Add **User Stories**: `Create task`, `List tasks`, `Health endpoint`.

You'll link these to branches/PRs later for traceability.

## Verification

- [ ] `Contoso-Tasks` project created (Git + Agile).
- [ ] Services configured; team reviewed.
- [ ] Iterations created.
- [ ] (Optional) A starter backlog exists.

## Summary

- Created the `Contoso-Tasks` project with Git and the Agile process.
- Configured services, team, and iterations.
- Optionally seeded a backlog to tie planning to delivery.

➡️ Next: [04 - Create Repository](./04-Create-Repository.md)
