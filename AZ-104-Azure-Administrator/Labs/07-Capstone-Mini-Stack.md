# Lab 07 — Capstone: Mini App Stack

**Time:** 60–90 minutes  
**Goal:** Build a small, realistic stack from scratch (or clean up and rebuild), then prove you can operate it day-to-day.

## Scenario

Contoso needs a **Dev** environment for a simple web app:

- Isolated resource group  
- Network foundation  
- Place to run the web app  
- Storage for uploads  
- Alert when something looks wrong  
- Clear tags and least-privilege thinking  

You are the cloud admin for the afternoon.

---

## Success criteria

Your stack must include:

| # | Requirement | Done |
| - | ----------- | ---- |
| 1 | RG `rg-capstone-<yourname>` with tags Owner, Env=Dev, App=ContosoWeb | ☐ |
| 2 | VNet with at least `app` and `data` subnets + NSG on `app` | ☐ |
| 3 | **Either** App Service **or** VM hosting a reachable web endpoint | ☐ |
| 4 | Storage account + private container `uploads` | ☐ |
| 5 | Short-lived read SAS demonstrated for one blob | ☐ |
| 6 | Action group + at least one alert rule on the compute resource | ☐ |
| 7 | Written answers to the ops questions below | ☐ |

Stretch (bonus):

- [ ] Peering to a second VNet  
- [ ] Policy requiring `Env` tag on the capstone RG  
- [ ] Backup enabled on VM or Azure Files  
- [ ] Delete lock on the RG (remove before cleanup)

---

## Suggested build order

```
  1. Resource group + tags
  2. VNet + subnets + NSG
  3. App Service (recommended) or VM
  4. Storage + container + sample upload + SAS
  5. Action group + alert
  6. Verify checklist + cleanup plan
```

Use Portal, CLI, or mix — your choice.

### Quick CLI starters (optional)

```bash
az group create -n rg-capstone-<yourname> -l <region> \
  --tags Owner=<yourname> Env=Dev App=ContosoWeb

az network vnet create -g rg-capstone-<yourname> -n vnet-capstone-<yourname> \
  --address-prefix 10.30.0.0/16 \
  --subnet-name app --subnet-prefix 10.30.1.0/24

az network vnet subnet create -g rg-capstone-<yourname> \
  --vnet-name vnet-capstone-<yourname> -n data --address-prefix 10.30.2.0/24
```

---

## Verification script (manual)

1. Browse your app URL or VM web page — works over HTTPS/HTTP as designed.  
2. Upload `hello.txt` to `uploads` → open with SAS in private window.  
3. Monitor → Alerts → your rule is **Enabled**.  
4. IAM on RG: explain who has access and why (even if only you).  
5. Cost: estimate what you’d turn off tonight.

---

## Ops questions (write short answers)

1. A new developer joins Contoso — how do you grant access **without** subscription Owner?  
2. Finance wants to know cost of ContosoWeb Dev — what did you set up to make that easy?  
3. Security says storage must not be public — what did you configure?  
4. At 2 AM the site is down — where do you look first (order of checks)?  
5. Tomorrow you must recreate this in Test — what would you automate next (Bicep/Terraform/pipeline)?

---

## Instructor demo / grading rubric (suggested)

| Level | Evidence |
| ----- | -------- |
| **Pass** | All 7 success criteria |
| **Strong** | Pass + one stretch item + clear ops answers |
| **Excellent** | Strong + can explain NSG rules and alert condition without notes |

---

## Cleanup (required)

When the instructor ends the lab:

```bash
az group delete -n rg-capstone-<yourname> --yes --no-wait
# Also delete older lab RG if finished with the course:
# az group delete -n rg-lab-<yourname> --yes --no-wait
```

Confirm in Portal that deletions completed (disks/IPs sometimes linger — delete orphans).

---

## After this lab

You have practiced the **daily Azure loop**:

**Organize → Secure access → Network → Run → Store → Watch → Clean up**

Continue with:

- [Daily Playbook slides](../Slides/07-Daily-Playbook.md)  
- [Azure DevOps 6-Day Course](../../Azure-DevOps-6-Day-Course/)  
- [.NET Deployment Workshop](../../Azure-DevOps-6-Day-Course/DotNet-Deployment-Workshop/) (deploy App Service from a pipeline)
