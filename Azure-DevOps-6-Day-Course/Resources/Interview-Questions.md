# Azure DevOps Interview Questions

A curated set of interview questions grouped by topic, with concise model answers. Use these to test your understanding after completing the course.

---

## DevOps Fundamentals

**1. What is DevOps?**
DevOps is a culture and set of practices that unites software development (Dev) and IT operations (Ops) to shorten the delivery lifecycle and deliver high-quality software continuously through automation, collaboration, and feedback.

**2. What are the key benefits of DevOps?**
Faster time to market, improved collaboration, higher deployment frequency, faster recovery from failures, better quality through automation, and increased reliability.

**3. Explain the DevOps lifecycle.**
Plan → Code → Build → Test → Release → Deploy → Operate → Monitor — a continuous loop where monitoring feedback informs the next plan.

**4. What is the difference between Continuous Integration, Continuous Delivery, and Continuous Deployment?**
- **CI**: Developers merge code frequently; each merge triggers an automated build and tests.
- **Continuous Delivery**: Every change that passes automated tests is automatically released to a repository/staging and is *ready* to deploy with a manual approval.
- **Continuous Deployment**: Every change that passes the pipeline is *automatically* deployed to production with no manual gate.

**5. What is "shift-left" testing?**
Moving testing earlier in the development process so defects are found and fixed sooner and more cheaply.

---

## Azure DevOps Platform

**6. What are the main services in Azure DevOps?**
Azure Boards, Azure Repos, Azure Pipelines, Azure Test Plans, and Azure Artifacts.

**7. What is the hierarchy in Azure DevOps?**
Organization → Project → (Boards, Repos, Pipelines, Test Plans, Artifacts).

**8. What is a process template? Name the built-in ones.**
A process template defines the work item types and workflows for a project. Built-in templates: **Basic**, **Agile**, **Scrum**, and **CMMI**.

**9. What access levels exist in Azure DevOps?**
Stakeholder (free, limited), Basic (free for first 5 users), and Basic + Test Plans (paid).

**10. Difference between a security group and a team?**
A **team** is a group of members used for Boards/backlog organization; a **security group** is used to assign permissions. Teams have an associated default security group.

---

## Azure Repos & Git

**11. What is the difference between Git and TFVC?**
Git is a **distributed** version control system (each clone has full history); TFVC (Team Foundation Version Control) is a **centralized** system.

**12. What is a pull request?**
A request to merge changes from one branch into another, allowing code review, policy enforcement, and discussion before the merge.

**13. What are branch policies?**
Rules enforced on protected branches — e.g., required reviewers, linked work items, build validation, comment resolution — to maintain code quality.

**14. Explain common branching strategies.**
GitFlow (feature/develop/release/hotfix/main), GitHub Flow (feature branches off main + PRs), trunk-based development (short-lived branches, frequent merges to main).

**15. How do you resolve a merge conflict?**
Identify conflicted files, edit to keep the correct content, remove conflict markers, then `git add` and commit.

**16. Difference between merge and rebase?**
Merge creates a merge commit preserving history; rebase replays commits on top of another branch producing a linear history.

---

## Azure Pipelines

**17. What is the difference between Classic and YAML pipelines?**
Classic pipelines are configured through a GUI; YAML pipelines are defined as code in the repository (versioned, reviewable, portable).

**18. What is the structure of a YAML pipeline?**
Pipeline → Stages → Jobs → Steps (tasks/scripts). Stages run sequentially by default; jobs within a stage can run in parallel.

**19. What are agents and agent pools?**
An **agent** is the compute (VM/container/machine) that runs pipeline jobs. An **agent pool** is a collection of agents. Microsoft-hosted pools are managed by Microsoft; self-hosted pools are managed by you.

**20. What are variables and variable groups?**
Variables store reusable values within a pipeline. Variable groups store values shared across multiple pipelines, and can link to Azure Key Vault for secrets.

**21. What are pipeline artifacts?**
Files produced by a build (binaries, packages) that are published and consumed by later stages or release pipelines.

**22. What is a multi-stage pipeline?**
A YAML pipeline that defines multiple stages (e.g., Build, Dev, QA, Prod) enabling CI and CD in a single file.

**23. How do you secure secrets in a pipeline?**
Use secret variables, variable groups linked to Azure Key Vault, and secure files; never hard-code secrets in YAML.

---

## Azure Boards

**24. What are the work item types in the Agile process?**
Epic, Feature, User Story, Task, Bug, Issue.

**25. What is the difference between a backlog and a sprint?**
A backlog is a prioritized list of all work; a sprint is a time-boxed iteration containing a selected subset of that work.

**26. What is a Kanban board vs a Taskboard?**
A Kanban board visualizes the flow of backlog items through columns; a sprint Taskboard shows the tasks within a single sprint.

---

## Deployments & Administration

**27. What is an environment in Azure Pipelines?**
A named collection of deployment targets (VMs, Kubernetes namespaces) used for deployment tracking, approvals, and checks.

**28. What is a service connection?**
A stored, secured credential/endpoint that lets pipelines authenticate to external services (Azure, Docker, GitHub, etc.).

**29. What are approvals and checks?**
Gates applied to environments: approvals require a human to authorize a deployment; checks are automated validations (e.g., Azure Policy, business hours, invoke REST API).

**30. What are audit logs used for?**
They record administrative and security-relevant events across the organization for compliance and investigation.

---

## Scenario / Behavioral

**31. A deployment to production failed. How do you respond?**
Roll back or redeploy the last good version, check pipeline/release logs and monitoring, identify root cause, add a test/guardrail, and document the incident.

**32. How would you design a pipeline for a microservices application?**
Use per-service pipelines or a mono-repo with path filters, build and containerize each service, push to a registry, deploy with multi-stage YAML to environments with approvals, and use templates to reduce duplication.

**33. How do you enforce code quality before merge?**
Branch policies with required reviewers, build validation, linked work items, and automated tests/linting/code-coverage gates.

---

> Tip: Practice explaining each answer out loud in 30–60 seconds. Interviewers value clear, structured reasoning over memorized definitions.
