# 15 - Hands-On Lab: Set Up Your Azure DevOps Environment

## Goal

Create your own Azure DevOps organization and project, configure a process, and invite a user. You will use this environment for the rest of the course.

**Estimated time:** 60 minutes

## Prerequisites

- A web browser.
- A Microsoft account (or work/school account). If you don't have one, create a free account at [account.microsoft.com](https://account.microsoft.com).

---

## Part 1 — Create an Organization

1. Go to [https://dev.azure.com](https://dev.azure.com) and sign in.
2. If prompted, click **Continue** to create your first organization, or select **New organization** from the bottom-left.
3. Enter:
   - **Organization name:** something unique, e.g., `yourname-devops-course`.
   - **Region:** choose the one closest to you.
4. Complete the CAPTCHA and click **Continue**.

✅ **Checkpoint:** You can access `https://dev.azure.com/<your-org>`.

---

## Part 2 — Create a Project

1. From the organization page, click **+ New project**.
2. Configure:
   - **Project name:** `Course-Project`
   - **Description:** `Project for the Azure DevOps 6-Day Course`
   - **Visibility:** Private
3. Expand **Advanced**:
   - **Version control:** Git
   - **Work item process:** Agile
4. Click **Create**.

✅ **Checkpoint:** Your project opens with Boards, Repos, Pipelines, etc. in the left navigation.

---

## Part 3 — Explore the Five Services

Click through the left navigation and note what each does:

- [ ] **Overview** — Summary, Wiki, Dashboards
- [ ] **Boards** — Work items, Backlogs, Sprints
- [ ] **Repos** — An empty Git repository named after your project
- [ ] **Pipelines** — Pipelines, Environments, Releases
- [ ] **Test Plans** — (may be hidden if not licensed)
- [ ] **Artifacts** — Package feeds

> If a service you don't need is showing, you can hide it under **Project settings → Overview → Azure DevOps services**.

---

## Part 4 — Review the Process

1. Go to **Organization settings → Boards → Process**.
2. Observe the built-in processes: Basic, Agile, Scrum, CMMI.
3. Note which one your project uses (Agile).

**Optional:** Create an inherited process:
1. Select **Agile → ⋯ → Create inherited process**.
2. Name it `Course-Agile`.
3. (Don't apply it yet — just observe the customization options.)

---

## Part 5 — Manage Users & Access Levels

1. Go to **Organization settings → Users**.
2. Click **Add users** and (optionally) invite a colleague or a secondary email.
   - **Access level:** choose **Stakeholder** (free) to practice.
   - **Add to project:** `Course-Project`.
3. Observe the access level options (Stakeholder, Basic, Basic + Test Plans).

> If you don't have a second email, just review the screen and cancel — no need to actually invite someone.

---

## Part 6 — Review Permissions

1. Go to **Project settings → Permissions**.
2. Explore the built-in groups: **Project Administrators, Contributors, Readers**.
3. Click **Contributors** and review the permissions list (note the Allow / Deny / Not set states).

---

## Deliverables / Verification

By the end of this lab you should have:

- [ ] An Azure DevOps **organization**.
- [ ] A **project** named `Course-Project` using Git + Agile.
- [ ] Explored all five services.
- [ ] Reviewed processes, users, access levels, and permissions.

---

## Reflection Questions

1. Why did we choose **Agile** as the process? When might **Scrum** or **Basic** be better?
2. If you wanted a colleague to only view and comment on work items, which access level would you assign?
3. Where would you go to add a build agent pool — project or organization settings?

---

🎉 **Congratulations!** You've completed Day 1. Tomorrow you'll start putting code into Azure Repos.

➡️ Continue to [Day 2 — Azure Repos & Git](../Day-02-Azure-Repos-Git/README.md)
