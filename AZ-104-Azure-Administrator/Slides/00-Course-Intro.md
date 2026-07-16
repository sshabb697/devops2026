---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section { font-size: 28px; }
  h1 { color: #0078d4; }
  h2 { color: #106ebe; }
  table { font-size: 22px; }
  footer { color: #666; font-size: 14px; }
footer: Azure Cloud Essentials | Intro
---

# Azure Cloud Essentials
## Skills for day-to-day Azure work

Create, secure, run, connect, and keep cloud resources healthy

---

# Who this is for

People who will **use Azure at work**:

- Developers deploying apps
- Admins / support engineers
- DevOps / platform beginners
- Anyone who opens the Azure portal and thinks “where do I start?”

**Goal:** confidence for Monday morning tasks — not memorizing exam weights.

---

# What “day-to-day Azure” looks like

Typical requests you will get:

- “Create a place for this app to run”
- “Give the new joiner access — but only to Dev”
- “Upload these files / share them safely”
- “Why can’t the server reach the database?”
- “We got a bill spike — what happened?”
- “Something is down — how do we know next time?”

This course answers those with **concepts + demos + labs**.

---

# Course map

| # | Module | You will learn to… |
|---|--------|--------------------|
| 01 | Fundamentals | Organize subscriptions, RGs, tags, cost |
| 02 | Identity & access | Grant least-privilege access safely |
| 03 | Storage | Store and share data the right way |
| 04 | Compute | Choose VM vs App Service vs containers |
| 05 | Networking | Connect and lock down traffic |
| 06 | Monitor & protect | See problems early; recover data |
| 07 | Daily playbook | Habits and troubleshooting order |

---

# How we will learn

1. **Why it matters** — real workplace story
2. **How it works** — simple diagram
3. **Demo** — Azure Portal / CLI
4. **Lab** — you build it
5. **Scenario** — “what would you do if…?”

> Prefer understanding **choices** over memorizing every product name.

---

# Azure vs Azure DevOps

| Azure (this course) | Azure DevOps |
|---------------------|--------------|
| Cloud platform — where apps and data live | Tools — Git, Pipelines, Boards |
| VMs, VNets, Storage, App Service | Build, test, deploy automation |
| “Create and run infrastructure” | “Automate delivery” |

You usually need **both**: host on Azure, ship with DevOps pipelines.

---

# Student setup

- [ ] Microsoft account + Azure subscription
- [ ] [portal.azure.com](https://portal.azure.com)
- [ ] Optional: Azure CLI + VS Code
- [ ] Second screen helps for labs

---

# Lab ground rules (save money & chaos)

- One RG per person: `rg-lab-<yourname>`
- Always tag: `Owner`, `Env=Lab`
- Prefer cheap SKUs (Free / B1 / Burstable)
- **Delete** the RG when the lab is done
- Never put real production secrets in lab accounts

---

# What success looks like

By the end you can:

1. Create a clean resource group and explain what belongs in it
2. Give a teammate access without over-permissioning
3. Store files and share them with a time-limited link
4. Deploy a simple web app (App Service or VM)
5. Draw a basic VNet + NSG for that app
6. Set an alert and know where to look when something fails

---

# Labs

Each module has a matching hands-on lab under `Labs/`:

Portal & tags → RBAC → Storage → VM/App Service → VNet → Alerts → **Capstone**

---

# Next

➡️ **Module 01 — Azure Fundamentals** · then **[Lab 01](../Labs/01-Portal-Resource-Groups-and-Tags.md)**

How Azure is organized · Portal & CLI · Cost awareness
