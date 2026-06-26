# 15 - Hands-On Lab: Plan Work with Azure Boards

## Goal

Build a small but complete plan: create an Epic → Feature → User Stories → Tasks/Bug, plan a sprint with capacity, customize the board, save a query with a chart, and pin it to a dashboard.

**Estimated time:** 60 minutes

## Prerequisites

- Completed Day 1 lab (project using the **Agile** process).

---

## Part 1 — Create the Hierarchy

1. **Boards → Backlogs**, set the level selector to **Epics**.
2. **+ New Epic:** `Online Checkout Experience`.
3. Open the Epic → add a child **Feature:** `Payment Processing`.
4. Open the Feature → add child **User Stories**:
   - `As a customer, I can pay with a credit card`
   - `As a customer, I see a receipt after payment`
5. For each story, fill **Description**, **Acceptance Criteria**, and set **Story Points** (e.g., 5 and 3).

✅ **Checkpoint:** The Stories backlog shows your two stories under the Feature/Epic.

---

## Part 2 — Add Tasks and a Bug

1. Open the first story → add child **Tasks**:
   - `Build payment form UI` (Remaining Work: 6)
   - `Integrate payment SDK` (Remaining Work: 8)
   - `Write unit tests` (Remaining Work: 4)
2. Create a **Bug:** `Checkout button unresponsive on mobile` with repro steps, **Severity: High**, **Priority: 1**.

✅ **Checkpoint:** Tasks appear under the story; the bug is on the backlog.

---

## Part 3 — Set Up a Sprint

1. **Project settings → Boards → Project configuration → Iterations** — confirm **Sprint 1** has dates (set them if needed).
2. **Team settings → Iterations** — ensure your team is subscribed to Sprint 1.
3. **Boards → Backlogs** → drag your two stories (and the bug) into **Sprint 1** (planning pane on the right).

---

## Part 4 — Plan Capacity

1. **Boards → Sprints → Capacity**.
2. Add yourself, set **6 hours/day**, activity **Development**.
3. Open the **Taskboard** — confirm tasks show remaining hours.
4. Check the **Work details** pane for over-allocation (red bars).

✅ **Checkpoint:** Capacity is set; the burndown will populate as you update tasks.

---

## Part 5 — Customize the Kanban Board

1. **Boards → Boards** (Stories).
2. **Board settings (gear)**:
   - **Columns:** add a `Code Review` column between Active and Resolved.
   - **Card fields:** show Story Points and Tags.
   - **WIP limit:** set a limit of 2 on the `Code Review` column.
3. Drag a card across columns and watch the state update.

✅ **Checkpoint:** Your board reflects a custom workflow with a WIP limit.

---

## Part 6 — Create a Query + Chart

1. **Boards → Queries → New query**:
   ```
   Work Item Type = User Story
   AND Iteration Path = @CurrentIteration
   ```
2. **Run** and **Save** as `Sprint Stories` under **Shared Queries**.
3. Open the **Charts** tab → **New chart** → Pie by **State**.

---

## Part 7 — Build a Dashboard

1. **Overview → Dashboards → + New Dashboard** → `Team Delivery`.
2. **Edit → Add widget**:
   - **Sprint Burndown**.
   - **Chart for Work Items** → point it at your `Sprint Stories` query.
   - **Query Tile** → count of active bugs.
3. **Save**.

✅ **Checkpoint:** A dashboard shows burndown, story states, and bug count.

---

## Deliverables / Verification

- [ ] Epic → Feature → 2 Stories → Tasks created and linked.
- [ ] A Bug with severity/priority.
- [ ] Stories planned into Sprint 1 with capacity set.
- [ ] Customized Kanban board (column + WIP limit).
- [ ] A saved shared query with a chart.
- [ ] A dashboard with at least three widgets.

---

## Reflection Questions

1. How does the work item hierarchy help leadership and developers see different levels?
2. Why estimate stories in points but tasks in hours?
3. What would the WIP limit on `Code Review` tell you if it's always full?

---

🎉 **Well done!** You can now plan and track work. Tomorrow you'll secure and govern deployments in Azure DevOps.

➡️ Continue to [Day 5 — Deployments & Administration](../Day-05-Deployments-and-Administration/README.md)
