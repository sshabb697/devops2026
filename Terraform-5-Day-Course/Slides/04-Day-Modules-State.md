---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section { font-size: 26px; }
  h1 { color: #7B42BC; }
  footer { color: #666; font-size: 14px; }
footer: Terraform 5-Day | Day 4
---

# Day 4 — Modules and remote state

**Today:** LEGO + shared notebook.

---

# Module = cookie cutter

![w:1000](../images/tf-modules.png)

Root `main.tf` stays short.  
`modules/web` has the details.

---

# Lab 04A

`terraform apply` from `Day-04/lab/`  
Website still works  
Point at the module folder

---

# Remote state

![w:1000](../images/tf-remote-state.png)

Create storage **once** with Azure CLI.  
Then `init -backend-config=backend.hcl`

---

# Lab 04B

Create `tfclass-state-rg` + storage + `tfstate` container  
Uncomment `backend.tf`  
Migrate state — plan should be **empty**

---

# Recap

1. Apply from the **root**  
2. State storage is a chicken-and-egg  
3. Do not delete the state group until Day 5
