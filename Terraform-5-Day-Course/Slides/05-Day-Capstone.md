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
footer: Terraform 5-Day | Day 5
---

# Day 5 — Plan, fix, delete

**Today:** read the plan. Fix YAML-like HCL. **Clean Azure.**

---

# Read the receipt

| Plan symbol | Meaning |
|-------------|---------|
| `+` | create |
| `~` | change |
| `-` | destroy |

Renaming often means **destroy + create**.

---

# Lab 05A

Folder `lab-broken`  
`terraform validate` fails on purpose  
Fix `locations` → `location`

---

# Troubleshoot

![w:1000](../images/tf-troubleshoot.png)

---

# Lab 05B — required

Capstone website → **destroy**  
Destroy Day 2/3/4 folders  
Delete `tfclass-state-rg` last  
Tutor checks Portal

---

# You can now

init / plan / apply / destroy  
variables · outputs · module · remote state

Next: Terraform in Azure DevOps.

Thank you — **delete leftovers today.**
