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
footer: Azure Cloud Essentials | 04 Compute
---

# Module 04
## Compute — where apps run

Pick the right host, deploy it, and access it safely

---

# The question you’ll hear often

> “We have a .NET / Node / Java app — where do we put it?”

| If you need… | Start with… |
|--------------|-------------|
| Fastest path, managed platform | **App Service** |
| Full OS / custom agents / legacy | **Virtual Machine** |
| Same app, many instances | **VM Scale Set** or App Service scale |
| Small container job | **Container Instances / Container Apps** |
| Store images | **Azure Container Registry** |

---

# Virtual Machines — when you need the OS

You manage: patching, agents, IIS/nginx, disks, backups of the OS.

```
  VM = Size + OS disk + NIC (+ data disks) + NSG rules
```

Daily tasks: create, resize, start/stop, attach disk, snapshot, troubleshoot RDP/SSH.

**Cost tip:** stop when idle; delete orphaned disks/IPs.

---

# Connecting without painting a target

| Approach | Use |
|----------|-----|
| Public IP + open RDP/SSH | Labs only, lock to *your* IP |
| **Azure Bastion** | Browser admin access; no public IP on VM |
| VPN / private network | Corporate standard |

Default mindset: **don’t expose management ports to the whole internet**.

---

# Disks & availability (ops view)

- Prefer **managed disks**; snapshot before risky changes  
- Premium SSD for busy Prod; Standard for labs  
- Spread important VMs across **Availability Zones** when the region supports it  
- Scale Sets when you need many identical VMs behind a load balancer  

---

# App Service — everyday web hosting

**PaaS:** you deploy code/package; Azure runs the platform.

Daily tasks:

- Create Web App + runtime (.NET, Node, …)
- Deploy from zip / DevOps pipeline / GitHub
- Scale up (bigger plan) or out (more instances)
- Slot swap (staging → production)
- Custom domain + HTTPS

This is what your DevOps course deploys to most often.

---

# Containers — lightweight packaging

| Service | Day-to-day use |
|---------|----------------|
| **ACR** | Private place for your images |
| **ACI** | Run a container quickly without Kubernetes |
| **Container Apps** | Modern apps with scale-to-zero, revisions |

Flow: build image → push ACR → run in ACI/Container Apps (or AKS later).

---

# Templates — stop clicking twice

If you’ll create the same stack again:

- **Bicep / ARM** (Azure-native)
- Or Terraform (common in many teams)

Portal is fine for learning. Templates are how teams stay consistent.

---

# Decision guide (teach this hard)

```
  Need OS-level control? ──yes──► VM / Scale Set
           │
           no
           ▼
  Standard web/API? ──yes──► App Service
           │
           no
           ▼
  Already containerized? ──yes──► Container Apps / ACI (+ ACR)
```

---

# Demo (25 min)

1. Create a small Linux or Windows VM — show disks/NIC/NSG  
2. Restrict SSH/RDP; mention Bastion  
3. Create **App Service** ( Free/B1 ) → browse default page  
4. Point out Deployment Center / how a pipeline would publish  
5. Optional: show ACR blade and “why images live here”  

---

# Scenarios

1. Internal line-of-business web API, team knows .NET, no desire to patch Windows  
2. Vendor appliance that “must be a VM”  
3. Nightly batch that runs 20 minutes in a container  

---

# Summary

- Match **control vs convenience** (VM vs App Service vs containers)  
- Protect admin access (Bastion / NSG)  
- Turn machines off; clean disks  
- Automate repeats with templates / pipelines  

---

# Next

➡️ **Module 05 — Networking**

How resources talk — and how you stop the wrong traffic
