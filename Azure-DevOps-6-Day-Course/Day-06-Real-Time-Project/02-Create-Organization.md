# 02 - Create Organization

## Overview

The first step is an Azure DevOps **organization** to house the Contoso Tasks project. If you already created one on Day 1, you can reuse it — or create a fresh one to practice.

## Steps

1. Go to [https://dev.azure.com](https://dev.azure.com) and sign in.
2. Select **New organization** (bottom-left) or follow the prompt.
3. Enter:
   - **Organization name:** e.g., `contoso-tasks-<yourname>` (must be globally unique).
   - **Region:** the one closest to your team.
4. Complete the CAPTCHA → **Continue**.

Your org URL will be `https://dev.azure.com/contoso-tasks-<yourname>`.

## Configure the Organization

Apply what you learned on Day 5 (lesson 11):

1. **Organization settings → Security → Policies** — review/tighten:
   - Restrict PAT creation / set max lifetime (optional for the lab).
   - Keep third-party app access limited.
2. **(Optional) Microsoft Entra ID** — connect a tenant if you have one (centralized identity).
3. **Organization settings → Billing** — note the free tier; link an Azure subscription only if you need more.

## Add Users (Simulated Team)

If you want to model the Contoso team (Day 1, lesson 12–13):

1. **Organization settings → Users → Add users**.
2. Add (or simulate) team members with appropriate **access levels**:
   - Developers → **Basic**.
   - Product Owner → **Stakeholder** (free).
   - QA → **Basic** (+ Test Plans if testing).
3. Add them to the project later (next lessons).

> No second email? Just review the screen — you can complete the project solo.

## Verification

- [ ] Organization created and reachable at its URL.
- [ ] Security policies reviewed.
- [ ] (Optional) Users/access levels considered.

## Summary

- Created (or reused) an organization for Contoso Tasks.
- Reviewed org security policies and (optionally) connected Entra ID.
- Considered team members and their access levels.

➡️ Next: [03 - Create Project](./03-Create-Project.md)
