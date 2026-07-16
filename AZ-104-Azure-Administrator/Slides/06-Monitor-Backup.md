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
footer: Azure Cloud Essentials | 06 Monitor & Protect
---

# Module 06
## Monitor & Protect

Know when something breaks — and get data/systems back

---

# Why this is daily work

Without monitoring:

- Users tell you it’s down (too late)
- You don’t know if it was CPU, disk, or a bad deploy
- Nobody knows who changed Prod yesterday

Without backup:

- Ransomware / accidental delete = career-limiting moment

---

# Azure Monitor — one place to look

```
  Your resources
       │
       ▼
  Azure Monitor
  ├── Metrics     → charts (CPU, requests, latency)
  ├── Logs        → query history (Log Analytics)
  ├── Alerts      → notify when bad things happen
  └── Insights    → curated views (VM, apps, …)
```

---

# Metrics vs logs (practical)

| | Metrics | Logs |
|--|---------|------|
| Feel like | Graphs | Searchable events |
| Example | CPU > 80% | App error messages, Activity Log |
| Good for | Capacity, health trends | Root cause, audit |

You’ll use **both**.

---

# Activity Log — “who changed what?”

Control-plane history:

- Who created / deleted / modified a resource
- Failed deployments
- Role assignments (in many cases)

Send important logs to a **Log Analytics workspace** so history isn’t short-lived.

---

# Alerts that people actually respond to

**Signal → condition → action group**

| Signal | Example |
|--------|---------|
| Metric | App response time high |
| Activity | Resource deleted in Prod RG |
| Log query | Many failed logins |

**Action group:** email, Teams/webhook, SMS, ticket system.

Tip: alert on **symptoms users feel**, not every tiny blip.

---

# Network Watcher — when “it can’t connect”

Handy tools:

- **IP flow verify** — would NSG allow this?
- **Next hop** — where does the packet go?
- **Connection troubleshoot** — path between two points
- **Effective security rules** — what NSG actually applies

Use before randomly opening ports.

---

# Backup — protect data and VMs

```
  Recovery Services vault
  ├── Backup policy (schedule + retention)
  └── Protected items (VMs, Azure Files, …)
```

Habits:

- Backup Prod VMs and critical file shares
- Test a **restore** once — backups you’ve never restored are theoretical
- Soft delete / immutability where ransomware is a concern

---

# Backup vs disaster recovery

| Need | Tool |
|------|------|
| “Restore last night’s data / VM” | **Azure Backup** |
| “Primary region is unavailable — run elsewhere” | **Site Recovery (ASR)** |

Most teams need backup on day one; full DR is a planned project.

---

# Demo (20 min)

1. Open Metrics on a VM or App Service  
2. Create alert + action group (your email)  
3. Show Activity Log for recent changes  
4. Create Recovery Services vault — enable backup on a lab VM (or walk through)  
5. Optional: Network Watcher → IP flow verify  

---

# Scenarios

1. Finance asks: who deleted the production NSG?  
2. Website is up but slow every Monday morning  
3. Junior admin wiped a data disk — what should already have been in place?  

---

# Summary

- Metrics for health; logs for investigation  
- Alerts + action groups = on-call awareness  
- Activity Log for change audit  
- Backup early; know Backup vs DR  

---

# Next

➡️ **Module 07 — Daily Playbook**

Habits, checklists, and a troubleshooting order you can reuse
