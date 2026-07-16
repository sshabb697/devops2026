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
footer: Azure Cloud Essentials | 05 Networking
---

# Module 05
## Networking

Make connectivity work — and keep the wrong traffic out

---

# Tickets this module prevents

- “App works on my VM but not from the office”
- “We opened port 22 to * and got scanned”
- “Dev and Prod VNets need to talk privately”
- “Storage should not be on the public internet”
- “Website is slow / only one VM — need a load balancer”

---

# VNet & subnets (your private space in Azure)

```
  VNet 10.0.0.0/16
  ├── app-subnet     10.0.1.0/24   ← web / App Service VNet integration
  ├── data-subnet    10.0.2.0/24   ← databases / private endpoints
  └── AzureBastionSubnet 10.0.3.0/26
```

Plan address space early — overlapping IPs break peering and hybrid later.

---

# NSG — your cloud firewall rules

Attach to **subnet** (common) and/or **NIC**.

Examples:

| Priority | Rule |
|----------|------|
| 100 | Allow 443 from Internet → app subnet |
| 110 | Allow 22 from Bastion subnet only |
| 4096 | Rely on defaults / deny the rest |

**ASG** = name groups of NICs (“web-servers”) so rules stay readable.

---

# Safe defaults for labs & Prod

- Don’t expose RDP/SSH to `Any` / `0.0.0.0/0`
- Open only the app ports you need
- Prefer Bastion or VPN for admin
- Document temporary “allow my IP” rules — and remove them

---

# Peering — connect two VNets

```
  VNet-Dev  ←── peering ──►  VNet-Shared
```

Use when: shared services (DNS, jump box) or app tiers in separate VNets.

Remember:

- Address spaces must **not** overlap  
- Peering is **not** transitive by default (A–B and B–C ≠ A–C)  

---

# Reaching PaaS privately

| Approach | Idea |
|----------|------|
| Public + firewall IP allow list | Simple; still public endpoint |
| Service endpoints | Harden path from VNet to Azure service |
| **Private endpoint** | Private IP inside your VNet for Storage/SQL/Key Vault/… |

Prod habit: **private endpoint + disable public access** for sensitive data.

---

# DNS (enough for daily work)

- Azure-provided DNS works for many labs  
- **Private DNS zones** pair with private endpoints (name → private IP)  
- Wrong DNS = “connected but name doesn’t resolve” — very common  

---

# Spreading traffic

| Service | Layer | Use when |
|---------|-------|----------|
| **Load Balancer** | TCP/UDP (L4) | VMs / Scale Sets |
| **Application Gateway** | HTTP (L7) | Path routing, WAF |
| Front Door | Global HTTP | Multi-region web entry |

Start with LB for VM farms; App Gateway when you need HTTP features.

---

# Hybrid awareness

| Option | Role |
|--------|------|
| VPN Gateway | Encrypted tunnel over internet to on-prem |
| ExpressRoute | Private circuit (enterprise) |
| Bastion | Admin into Azure VNets |

You design Azure networking so it fits the company’s existing network.

---

# Demo (25 min)

1. Create VNet with `app` + `data` subnets  
2. Put a VM in `app`; NSG allow SSH/RDP only from you / Bastion  
3. Create second VNet → peer  
4. Show private IPs; discuss what NSG must allow for cross-talk  
5. Diagram private endpoint to storage (create if time)  

---

# Scenarios — troubleshoot order

> “VM cannot reach Azure SQL / storage”

1. NSG effective rules?  
2. Correct subnet / route?  
3. Public firewall on the PaaS service?  
4. Private endpoint + DNS correct?  
5. App using the right hostname?  

---

# Summary

- Design VNets/subnets on purpose  
- NSG = allow what you need, nothing else  
- Peer for private connectivity between VNets  
- Prefer private endpoints for sensitive PaaS  
- Know L4 vs L7 load balancing  

---

# Next

➡️ **Module 06 — Monitor & Protect**

See problems early · recover when things go wrong
