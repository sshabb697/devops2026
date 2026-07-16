# Lab 04 — Compute: VM & App Service

**Time:** 60–75 minutes  
**Goal:** Create a small VM with locked-down access, then host a simple site on App Service and compare the two approaches.

## Prerequisites

- `rg-lab-<yourname>`  
- Permission to create compute resources  
- If your subscription blocks VMs or public IPs, do **Part B only** (App Service)

---

## Part A — Create a Linux VM (25–30 min)

1. **Create a resource → Virtual machine**.
2. Basics:
   - RG: `rg-lab-<yourname>`
   - Name: `vm-lab-<yourname>`
   - Region: `<region>`
   - Image: **Ubuntu** (20.04/22.04 LTS) or instructor choice
   - Size: **Burstable** small size (e.g. `B1s` / `B2ats_v2`) — cheapest available
   - Authentication: **SSH public key** (preferred) or password for lab
   - Username: `azureuser`
3. **Disks:** OS disk Standard SSD is fine.
4. **Networking:**
   - Create new VNet or use existing — note the name (e.g. `vm-lab-<yourname>-vnet`)
   - Public IP: Yes (for lab)  
   - NIC NSG: **Basic** → Public inbound ports: allow **SSH (22)** only  
5. Tags: `Env=Lab`, `Owner=<yourname>`
6. **Review + create → Create**. Wait for deployment.

### Harden the NSG (5 min)

1. Open the VM → **Networking** / NSG.
2. Inbound rule for SSH: change source from **Any** to **My IP address** (or your training room IP range).
3. Confirm no RDP/other management ports are open.

### Connect (5 min)

```bash
ssh azureuser@<public-ip>
```

Or use **Serial console** / **Bastion** if SSH from your PC is blocked.

Inside the VM (optional):

```bash
uname -a
exit
```

✅ **Checkpoint:** VM is **Running**; SSH restricted to your IP (or Bastion discussed).

### Cost control

Portal → VM → **Stop** when you move to Part B (deallocates compute; disk still costs a little).

---

## Part B — Create an App Service web app (20–25 min)

1. **Create a resource → Web App**.
2. Basics:
   - RG: `rg-lab-<yourname>`
   - Name: `app-lab-<yourname>-01` (globally unique)
   - Publish: **Code**
   - Runtime: **.NET 8** or **Node 20 LTS** (instructor choice)
   - OS: **Linux**
   - Region: `<region>`
   - App Service Plan: create new — **Free F1** if available, else **Basic B1**
3. Tags: `Env=Lab`, `Owner=<yourname>`
4. Create → open the App Service.

### Browse & explore (10 min)

1. Click **Browse** / default URL: `https://app-lab-<yourname>-01.azurewebsites.net`
2. You should see the default welcome page (or runtime splash).
3. Open these blades and note what they’re for:
   - **Deployment Center** — where GitHub / Azure DevOps would connect  
   - **Configuration** — app settings / connection strings  
   - **Scale up** / **Scale out** — bigger plan vs more instances  
   - **Log stream** — live logs  

✅ **Checkpoint:** Public HTTPS URL loads without you managing an OS.

---

## Part C — Compare (10 min discussion / write answers)

| Question | VM | App Service |
| -------- | -- | ----------- |
| Who patches the OS? | | |
| How do you deploy app code? | | |
| Typical admin ports? | | |
| Which fits a simple company web API? | | |

Write 2–3 sentences: **When would you still choose a VM?**

---

## Stretch (optional)

- Enable **Azure Bastion** on the VM’s VNet (costs money — instructor approval).  
- Deploy a tiny zip to App Service (**Advanced Tools / Kudu** or `az webapp deploy`) if time allows.  
- Link to [.NET Deployment Workshop](../../Azure-DevOps-6-Day-Course/DotNet-Deployment-Workshop/) for pipeline deploy later.

---

## Deliverables

- [ ] VM created and NSG tightened (or skipped with instructor OK)  
- [ ] App Service reachable over HTTPS  
- [ ] Written comparison of VM vs App Service  

## Cleanup

**Stop** the VM. Delete VM + NIC + public IP + NSG + disks if not needed for Lab 05/07.

Keep App Service if you’ll use it in the capstone; otherwise delete to save quota.

```bash
az vm deallocate -g rg-lab-<yourname> -n vm-lab-<yourname>
# or full delete when finished:
# az vm delete -g rg-lab-<yourname> -n vm-lab-<yourname> --yes
```

## Reflection

1. What still costs money when a VM is stopped?  
2. Why is App Service popular for DevOps pipelines?  
3. What’s risky about SSH open to the whole internet?

➡️ Next: [Lab 05 — Networking](./05-Networking-VNet-NSG-Peering.md)
