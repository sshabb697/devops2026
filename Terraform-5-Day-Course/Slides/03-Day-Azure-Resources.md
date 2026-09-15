---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section { font-size: 26px; }
  h1 { color: #7B42BC; }
  footer { color: #666; font-size: 14px; }
footer: Terraform 5-Day | Day 3
---

# Day 3 — Storage website

**Today:** a real URL in the browser.

---

# The stack

![w:1000](../images/tf-azure-stack.png)

Resource group → storage → HTML file

---

# Order without a to-do list

You **reference** `azurerm_resource_group.main.name`  
Terraform builds the graph.

Storage names are **world-unique**. We add random letters.

---

# Lab 03A

`prefix` in tfvars = your initials (lowercase)  
`terraform apply`  
Portal shows storage

---

# Lab 03B

`terraform output website_url`  
Open in browser  
Change HTML → apply → refresh

---

# Recap

1. LRS is cheap for class  
2. Static site ≠ app server  
3. Keep or destroy as the tutor says
