---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section { font-size: 26px; }
  h1 { color: #7B42BC; }
  table { font-size: 20px; }
  footer { color: #666; font-size: 14px; }
footer: Terraform 5-Day | Day 2
---

# Day 2 — Variables and state

**Today:** blanks in the form. Do not edit state by hand.

---

# Variables fill blanks

![w:1050](../images/tf-variables.png)

`variables.tf` = questions  
`terraform.tfvars` = answers  
`main.tf` = the letter  
`-var` / `TF_VAR_` beat `default`

---

# Lab 02A

Edit `terraform.tfvars`  
`terraform plan` / `apply`  
Change a **tag**, plan again → **1 to change**

---

# State = memory

![w:1050](../images/tf-state.png)

Wish = `.tf`  
Notebook = `.tfstate`  
Reality = Azure

---

# Lab 02B

```bash
terraform output
terraform state list
terraform state show azurerm_resource_group.main
```

Never Notepad the `.tfstate` file.

---

# Recap

1. No secrets in Git  
2. State is not Azure itself  
3. Two laptops need **remote** state (Day 4)
