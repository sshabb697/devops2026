# Terraform 5-Day Course

Hands-on Terraform for **beginners**. You will write small files, preview changes, and create real Azure resources — then delete them.

> Goal: **describe infrastructure as code** — a recipe Azure can follow every time.

Print or keep open: **[Command Cheat Sheet](./Command-Cheat-Sheet.md)** · Tutors: **[Tutor-Notes.md](./Tutor-Notes.md)** · Slides: **[Slides](./Slides/)** · Guide map: **[Resources/From-Your-Guide.md](./Resources/From-Your-Guide.md)**

---

## What you will be able to do

By Day 5 you can:

1. Explain why clicking the Azure Portal is hard to repeat.
2. Run `init` → `plan` → `apply` → `destroy`.
3. Use variables, outputs, and a simple module.
4. Put state in Azure Storage so two people share one memory.
5. Build a small stack (resource group + storage website) and tear it down.

| Day | Topic | Outcome |
| --- | ----- | ------- |
| [Day 1](./Day-01-IaC-and-First-Apply/) | IaC, install, first apply | Resource group created with Terraform |
| [Day 2](./Day-02-HCL-Variables-State/) | HCL, variables, state | Change location with a variable |
| [Day 3](./Day-03-Azure-Resources/) | Storage + website | Static website URL from Terraform |
| [Day 4](./Day-04-Modules-and-Remote-State/) | Modules + remote state | Reuse a module; state in Azure |
| [Day 5](./Day-05-Workflow-and-Capstone/) | Plan review, fix, cleanup | Capstone + **destroy everything** |

---

## Class timing (every day ≈ 3 hours)

| Block | Minutes |
| ----- | ------- |
| Lesson A + picture | 20 |
| Lab A | 40 |
| Lesson B + picture | 20 |
| Lab B | 50 |
| Recap | 20 |
| Buffer (Azure wait / errors) | 30 |

**After every lesson there is a lab.** Azure `apply` can take a few minutes — that is normal.

---

## Prerequisites

- Comfort with a terminal (`cd`, `ls` / `dir`)
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) and an Azure subscription (student / trial is enough)
- Windows + WSL2, macOS, or Linux
- **Cost:** labs use cheap resources (resource group, storage). **Destroy at the end of each day** if you stop. **Day 5 deletes remaining labs.**

---

## How to teach / study

1. Show the **picture**.
2. Read the **one-sentence idea**.
3. Walk through the **example**.
4. Students complete the **lab**.
5. Use the **cheat sheet** when a command is forgotten.

**If apply fails:** read the error → `az account show` → unique names (storage names are global) → `terraform plan` again.

---

## Course layout

```
Terraform-5-Day-Course/
├── README.md
├── Command-Cheat-Sheet.md
├── Tutor-Notes.md
├── Slides/
├── images/
├── Resources/
└── Day-01- … Day-05- …
```

---

## Connects to other courses

| Before | After |
| ------ | ----- |
| [AZ-104](../AZ-104-Azure-Administrator/) (what a resource group is) | [Azure DevOps](../Azure-DevOps-6-Day-Course/) (run Terraform in a pipeline) |
| [Linux](../Linux-5-Day-Course/) / [Docker](../Docker-5-Day-Course/) | [Kubernetes](../Kubernetes-10-Day-Course/) (later: AKS with Terraform) |

---

## Course images

| Image | Used in |
| ----- | ------- |
| `images/tf-click-vs-code.png` | Day 1 — Portal vs code |
| `images/tf-workflow.png` | Day 1 — init / plan / apply / destroy |
| `images/tf-provider.png` | Day 1 — Provider talks to Azure |
| `images/tf-state.png` | Day 2 — State file |
| `images/tf-variables.png` | Day 2 — Variables |
| `images/tf-azure-stack.png` | Day 3 — RG + storage + website |
| `images/tf-modules.png` | Day 4 — Modules |
| `images/tf-remote-state.png` | Day 4 — Remote state |
| `images/tf-troubleshoot.png` | Day 5 — Fix errors |
