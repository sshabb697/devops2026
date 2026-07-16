# Lab 05 — Networking: VNet, NSG & Peering

**Time:** 60–75 minutes  
**Goal:** Design a simple VNet with subnets, control traffic with an NSG, and connect two VNets with peering.

## Prerequisites

- `rg-lab-<yourname>`  
- Basic IP/CIDR comfort (instructor can draw on whiteboard)  

> If Lab 04 created a VM VNet automatically, you can **reuse** it or create fresh VNets below for clarity.

---

## Part A — Create VNet-A (15 min)

1. **Create a resource → Virtual network**.
2. Basics:
   - Name: `vnet-lab-<yourname>-a`
   - RG: `rg-lab-<yourname>`
   - Region: `<region>`
3. **IP addresses** tab:
   - Address space: `10.10.0.0/16`
   - Subnet `app`: `10.10.1.0/24`
   - Add subnet `data`: `10.10.2.0/24`
4. Tags: `Env=Lab`, `Owner=<yourname>`
5. Create.

✅ **Checkpoint:** VNet-A shows two subnets: `app` and `data`.

---

## Part B — NSG for the app subnet (15 min)

1. **Create a resource → Network security group**.
2. Name: `nsg-lab-<yourname>-app` · same RG/region.
3. Open NSG → **Inbound security rules → Add**:

| Priority | Name | Port | Protocol | Source | Destination | Action |
| -------- | ---- | ---- | -------- | ------ | ----------- | ------ |
| 100 | Allow-HTTPS | 443 | TCP | Any / Internet | Any | Allow |
| 110 | Allow-SSH-MyIP | 22 | TCP | My IP | Any | Allow |

4. **Subnets → Associate** → select `vnet-lab-<yourname>-a` / subnet `app`.

✅ **Checkpoint:** NSG associated to `app` subnet; default deny still protects other ports.

**Discuss:** Why associate NSG to subnet instead of only to one NIC?

---

## Part C — Create VNet-B (10 min)

1. Create second VNet: `vnet-lab-<yourname>-b`
2. Address space: `10.20.0.0/16` (**must not overlap** VNet-A)
3. One subnet `shared`: `10.20.1.0/24`
4. Same RG/region/tags.

✅ **Checkpoint:** Two VNets with non-overlapping CIDRs.

---

## Part D — Peer the VNets (15 min)

1. Open `vnet-lab-<yourname>-a` → **Peerings → Add**.
2. Peering settings (names can vary slightly in portal):
   - This VNet peering name: `peer-a-to-b`
   - Remote VNet: `vnet-lab-<yourname>-b`
   - Allow traffic both directions (defaults are usually fine for lab)
   - Remote peering name: `peer-b-to-a` (portal often creates both)
3. Create → wait until peering status is **Connected** on both sides.

✅ **Checkpoint:** Both VNets show peering **Connected**.

---

## Part E — Optional VM connectivity test (15–20 min)

Only if you have quota/time:

1. Create a tiny VM in VNet-A `app` subnet (`vm-a-<yourname>`).
2. Create a tiny VM in VNet-B `shared` subnet (`vm-b-<yourname>`).
3. NSG: allow SSH from your IP on both; allow ICMP or SSH from the other VNet’s address space if you want a connectivity test.
4. SSH to vm-a → `ping` or `ssh` to vm-b’s **private** IP.

If ping is blocked by NSG/OS firewall, use: “peering Connected + private IPs listed” as success, and discuss what else is needed for traffic.

✅ **Checkpoint:** You can explain how traffic would flow A → peering → B.

---

## Part F — Private access discussion (10 min)

Open any storage account (Lab 03) → **Networking**.

Walk through (create private endpoint only if instructor OK):

- Public access + firewall  
- Private endpoint idea: NIC in `data` subnet with private IP  

Sketch on paper:

```
  User → App (app subnet)
           │
           └── private endpoint → Storage (data subnet)
```

---

## Deliverables

- [ ] VNet-A with `app` + `data` subnets  
- [ ] NSG on `app` with HTTPS + restricted SSH  
- [ ] VNet-B with non-overlapping range  
- [ ] Peering Connected both ways  
- [ ] (Optional) Private IP connectivity test  

## Cleanup

Peerings/VNets are cheap; VMs are not — **deallocate/delete VMs** after class.

```bash
az network vnet peering list -g rg-lab-<yourname> --vnet-name vnet-lab-<yourname>-a -o table
```

## Reflection

1. Why can’t two peered VNets use the same `10.0.0.0/16`?  
2. What does “peering is not transitive” mean for three VNets?  
3. First three checks when “VM cannot reach storage”?

➡️ Next: [Lab 06 — Monitor & Backup](./06-Monitor-Alerts-and-Backup.md)
