---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section { font-size: 26px; }
  h1 { color: #7B42BC; }
  h2 { color: #5C4EE5; }
  table { font-size: 20px; }
  footer { color: #666; font-size: 14px; }
footer: Terraform 5-Day | Day 1
---

# Day 1 — Why Terraform

**Today:** install, login, create **one** resource group.

---

# Clicking vs a recipe

![w:1050](../images/tf-click-vs-code.png)

---

# Cooking story

Recipe = `.tf` files  
Cook = `terraform apply`  
Friend can cook the same dish next week

---

# Declarative vs click / CLI

You write **what** you want (a resource group).  
Terraform decides **how** to talk to Azure.

Run apply twice → still **one** group (idempotent).  
`az group create` is a **step**. Terraform is a **picture**.

---

# Lab 01A

`terraform version`  
`az login`  
`az account show`

---

# The four commands

![w:1050](../images/tf-workflow.png)

**plan** does **not** create anything.  
Line to remember: `1 to add, 0 to change, 0 to destroy`.

Usual files: `providers.tf` · `main.tf` · later `variables.tf` / `outputs.tf`

---

# Provider = plug

![w:1000](../images/tf-provider.png)

---

# Lab 01B

Folder `Day-01/lab/`

```bash
terraform init
terraform plan
terraform apply
```

See the group in the Portal. Then `destroy` (unless tutor says keep).

---

# Recap

1. Terraform talks **to** Azure  
2. Plan = preview  
3. Change the RG name so students do not clash
