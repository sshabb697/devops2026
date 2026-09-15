# How we used *Terraform Basics to Advanced in One Guide*

Your PDF: `C:\Users\SPALPT145\Terraform Basics to Advanced in One Guide_v1.0 (1).pdf`  
(Author: Govardhana Miriyala Kannaiah / [TechOpsExamples](https://www.techopsexamples.com/).)

We **did not copy the book**. Students learn in this course’s simple English and Azure labs. Tutors may keep the PDF for extra reading.

| Guide chapter | Where it lives in this course |
| ------------- | ------------------------------ |
| 1 Fundamentals (declarative, architecture, vs other IaC) | [Day 1 — Why Terraform](../Day-01-IaC-and-First-Apply/01-Why-Terraform.md) |
| 2 Setup (install, providers, state, backends) | Lab 01A, Day 1 providers, [Day 2 state](../Day-02-HCL-Variables-State/02-State.md), Day 4 backend |
| 3 Core workflow + file names | [Day 1 — workflow](../Day-01-IaC-and-First-Apply/02-Four-Commands.md) |
| 4 Modules + environments | [Day 4 modules](../Day-04-Modules-and-Remote-State/01-Modules.md), [workspaces optional](../Day-04-Modules-and-Remote-State/03-Workspaces-Optional.md) |
| 5 Variables, types, outputs | [Day 2 variables](../Day-02-HCL-Variables-State/01-Variables.md) |
| 6 Dependencies, secrets, scale | [Day 3 implicit/explicit](../Day-03-Azure-Resources/01-Resources.md); secrets = don’t commit tfvars |
| 7 Provisioners / lifecycle | Mention only on [Day 5](../Day-05-Workflow-and-Capstone/02-Destroy.md) — last resort |
| 8 Debugging (`TF_LOG`) | Day 5 + cheat sheet |
| 9 Must-know commands | [Command-Cheat-Sheet.md](../Command-Cheat-Sheet.md) |

Guide examples are often **AWS**. This class uses **Azure** so it matches the rest of devops2026.
