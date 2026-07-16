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
  code { font-size: 20px; }
footer: Azure Cloud Essentials | 01 Fundamentals
---

# Module 01
## Azure Fundamentals

How the cloud is organized — and how you work in it every day

---

# Why this module matters

Before you create a VM or a website, you need to know:

- Where does the bill go?
- Where should this resource live?
- How do I find it again next week?
- How do I avoid leaving expensive junk running?

**Organization + habits** beat random clicking in the portal.

---

# Cloud in one slide

**On‑prem:** buy servers → wait → own hardware → pay even when idle

**Azure:** request capacity → minutes later → pay for what you use → someone else runs the datacenter

You still own: **architecture, access, data, and cost discipline**.

---

# IaaS vs PaaS vs SaaS (choose workload style)

| Model | You manage | Good when… | Examples |
|-------|------------|------------|----------|
| **IaaS** | OS + app | Need full control / custom software | Virtual Machines |
| **PaaS** | App + data | Want to ship features, not patch OS | App Service, many databases |
| **SaaS** | Config | Use a finished product | Microsoft 365 |

**Daily tip:** Prefer PaaS when you don’t *need* the OS.

---

# Regions & availability (practical)

| Concept | Why you care |
|---------|--------------|
| **Region** | Latency to users; data residency; which services exist |
| **Availability Zone** | Survive one datacenter failure in the region |
| **Paired region** | Some DR / geo-redundant features |

Pick region for **users + compliance + cost**, not by habit.

---

# The hierarchy you will live in

```
  Management Group (optional — big orgs)
         │
         ▼
  Subscription          ← billing & many access boundaries
         │
         ▼
  Resource Group        ← “folder” for an app / env
         │
         ▼
  Resources             ← VM, Storage, VNet, App Service…
```

**Rule of thumb:** one app + one environment → one resource group  
(e.g. `rg-contoso-web-dev`)

---

# Subscription vs resource group

**Subscription**
- Who pays
- Company or team boundary
- Quotas and policies often applied here

**Resource Group**
- Lifecycle together (deploy / delete as a set)
- Good place for RBAC (“Dev team owns this RG”)
- Delete RG → deletes almost everything inside

---

# Tags — your future self will thank you

| Tag | Example | Why |
|-----|---------|-----|
| Env | Dev / Test / Prod | Separate risk |
| Owner | email or team | Who to call |
| CostCenter | FIN-100 | Chargeback |
| App | ContosoWeb | Find related resources |

Without tags, Cost Management becomes guesswork.

---

# Resource locks (production safety)

| Lock | Effect |
|------|--------|
| **CanNotDelete** | Edit OK; delete blocked |
| **ReadOnly** | Almost no changes |

Use on Prod RGs and critical networking.  
Stops “I deleted the wrong thing on Friday evening.”

---

# Tools for daily work

| Tool | Use it when… |
|------|----------------|
| **Portal** | Explore, one-off, show someone |
| **Cloud Shell** | Quick CLI in the browser |
| **Azure CLI / PowerShell** | Repeatable tasks, scripts |
| **Bicep / ARM / Terraform** | Same environment every time |

Start with Portal → graduate scripts for anything you’ll do twice.

---

# CLI you’ll use this week

```bash
az login
az account show
az group create -n rg-lab-alex -l eastus --tags Owner=alex Env=Lab
az group list -o table
az group delete -n rg-lab-alex --yes --no-wait
```

Create → list → delete. That’s 80% of lab hygiene.

---

# Cost — part of the job

Daily habits:

- Stop / deallocate VMs when idle (disks may still cost)
- Delete unused public IPs, disks, NICs, load balancers
- Prefer Burstable / Free / Basic for labs
- Set a **budget alert** on the subscription
- Review Cost Analysis by **tag** weekly

---

# Demo (10–15 min)

1. Portal home → Subscriptions → Resource groups  
2. Create `rg-lab-demo` + tags  
3. Open Cost Management → show “what costs look like”  
4. Cloud Shell → `az group list -o table`  
5. Add a **CanNotDelete** lock, then remove it  

---

# Scenario — discuss

> New project “Inventory API” for Dev.  
> Where do you create it? What do you name the RG? Which tags?  
> Who should be Owner vs Contributor?

---

# Summary

- Organize with **subscription → RG → resources**
- Tag everything; lock production
- Prefer PaaS when possible
- Treat **cost** as a daily ops task

---

# Next

➡️ **Module 02 — Identity & Access**

Who can do what — without opening the whole subscription
