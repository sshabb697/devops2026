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
footer: Azure Cloud Essentials | 07 Daily Playbook
---

# Module 07
## Daily Playbook

Habits and a simple order of operations for real Azure work

---

# Your job in one sentence

**Keep workloads running, secure, recoverable, and cost-aware** — using the portal, CLI, and automation.

Everything in this course supports that sentence.

---

# Monday checklist (lightweight)

- [ ] Any **budget / cost** anomalies since last week?  
- [ ] Critical **alerts** firing or silenced wrongly?  
- [ ] Unused lab / old RGs to delete?  
- [ ] Access requests pending (joiners/leavers)?  
- [ ] Backup jobs healthy for Prod?  

10 minutes prevents many Friday fires.

---

# When someone asks “create X”

1. **Which subscription / RG / Env?** (Dev ≠ Prod)  
2. **Who needs access?** (group + least privilege)  
3. **Network?** (VNet/subnet/NSG / public or private)  
4. **Data?** (storage redundancy, backup)  
5. **How will we know it’s healthy?** (metrics + alert)  
6. **Tags + naming** before you click Create  

Skipping 1–2 causes half of cleanup tickets later.

---

# Troubleshooting order (save this)

```
  1. What changed?     → Activity Log / recent deploy
  2. Is it up?         → Metrics / App URL / VM status
  3. Can it connect?   → NSG, DNS, private endpoint, LB probe
  4. Is it authorized? → RBAC, keys/SAS expired, managed identity
  5. Is it capacity?   → CPU, memory, throttling, disk full
  6. Recover           → restart / scale / restore backup
```

Don’t open every port at step 1.

---

# Decision cheatsheet

| Situation | Prefer |
|-----------|--------|
| Web/API, little OS need | App Service |
| Custom OS / agent | VM |
| Temporary file share with partner | SAS (short expiry) |
| Prod data off internet | Private endpoint |
| New teammate access | Group + RG-scoped role |
| Stop accidental delete | Resource lock on Prod |
| Notify on outage | Metric alert + action group |

---

# Cost hygiene (non-negotiable)

- Delete lab RGs when done  
- Hunt orphaned **disks, NICs, public IPs**  
- Right-size or stop idle VMs  
- Watch egress and redundant GRS where LRS would do for Dev  
- Tag for Cost Analysis  

Cloud waste is usually **forgotten resources**, not fancy SKUs.

---

# Security hygiene

- No Owner on subscription “for convenience”  
- No secrets in Git or screenshots  
- Rotate keys if they were shared  
- Prefer managed identity over embedding secrets  
- Review guest users quarterly  

---

# Build a personal lab stack

Practice once end-to-end:

```
  rg-lab-<you>
  ├── VNet + NSG
  ├── App Service or small VM
  ├── Storage (private container)
  ├── Alert on availability/CPU
  └── Tags + (optional) backup
```

Then delete the whole RG. Rebuild from memory next week.

---

# How this ties to DevOps

| Azure skill | Used when you… |
|-------------|----------------|
| RG + App Service | Deploy from pipeline |
| RBAC / service connection | Let pipeline deploy safely |
| VNet / NSG | Secure app environments |
| Monitor / alerts | Know deploys broke Prod |
| Storage | Artifacts, static files, logs |

Next step: [Azure DevOps course](../../Azure-DevOps-6-Day-Course/) / [.NET workshop](../../Azure-DevOps-6-Day-Course/DotNet-Deployment-Workshop/).

---

# Optional: certification later

If you want AZ-104 later, you already practiced the **same skills**.

Add: Microsoft Learn path + practice questions — after you’re comfortable in the portal.

This course stays useful even if you never sit the exam.

---

# Closing

You don’t need to know every Azure service.

You need to:

1. Organize cleanly  
2. Grant least privilege  
3. Choose the right place to run apps  
4. Connect and lock down networks  
5. Watch, alert, and back up  

That’s day-to-day Azure.

---

# You’re ready to practice

Open the portal → create `rg-lab-<you>` → build something small → **delete it**.

Questions welcome — bring real scenarios from your workplace.
