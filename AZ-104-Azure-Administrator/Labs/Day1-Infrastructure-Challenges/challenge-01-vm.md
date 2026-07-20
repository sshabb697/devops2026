# Challenge 01 — Create a Virtual Machine (Portal)

**Time:** 40–50 minutes  
**You will learn:** Create a VM, see what resources Azure creates with it, and attach it to your Day 1 VNet.

## Prerequisites

- [Challenge 00](./challenge-00-vnet.md) complete (`rg-d1-<yourname>`, VNet, Public IP)

---

## Step 1 — Start the VM wizard

1. Portal → **+ Create a resource** → **Virtual machine** → **Create**.
2. **Basics** tab:

| Field | Value |
| ----- | ----- |
| Resource group | `rg-d1-<yourname>` |
| Virtual machine name | `vm-d1-<yourname>-01` |
| Region | `<region>` |
| Availability options | **No infrastructure redundancy required** (lab) *or* Availability set if your instructor requires it |
| Image | **Ubuntu 22.04 LTS** *or* **Windows Server 2022** (instructor choice) |
| Size | `Standard_B1s` or `Standard_B2s` |
| Username | e.g. `azureuser` (not `admin` / `Administrator` / `root`) |
| Password / SSH key | Complex password **or** SSH public key |
| Public inbound ports | Allow **SSH (22)** for Linux or **RDP (3389)** for Windows |

3. **Disks:** OS disk **Standard SSD**.
4. **Networking:**

| Field | Value |
| ----- | ----- |
| Virtual network | `vnet-d1-<yourname>-a` |
| Subnet | `snet-d1-<yourname>-app` |
| Public IP | Select existing `pip-d1-<yourname>-vm` |
| NIC NSG | Basic — allow SSH or RDP only |

5. **Management:** Boot diagnostics = **Disable** (optional, saves a bit of storage noise).
6. **Tags:** `Owner=<yourname>`, `Env=Lab`, `Day=Day1`.
7. **Review + create → Create**. Wait until deployment finishes.

---

## Step 2 — Explore what was created

Open `rg-d1-<yourname>` → **Overview** / **Resources**. You should see roughly:

| Resource | Role |
| -------- | ---- |
| Virtual machine | Compute |
| Network interface (NIC) | Connects VM to VNet |
| Public IP | Internet address |
| NSG | Firewall rules |
| OS disk | Managed disk |
| VNet (already existed) | Network |

✅ **Checkpoint:** You can explain each resource in one sentence.

---

## Step 3 — Harden NSG (important)

1. Open the VM → **Networking**.
2. Edit the inbound rule for SSH/RDP:
   - Source: **My IP address** (not Any / 0.0.0.0/0).
3. Save.

✅ **Checkpoint:** Management port is limited to your IP.

---

## Step 4 — Connect

**Linux:**

```bash
ssh azureuser@<public-ip-or-dns>
```

**Windows:** VM → **Connect → RDP** → download RDP file → sign in with your username/password.

Optional inside the VM:

```bash
# Linux
hostname && uname -a
```

---

## Deliverables

- [ ] VM running in your Day 1 VNet
- [ ] Existing public IP attached
- [ ] NSG restricted to your IP
- [ ] Successful SSH or RDP login

## Cost tip

When you stop for the day: VM → **Stop** (deallocates). Disk still costs a little.

➡️ Next: [Challenge 02 — Cloud Shell](./challenge-02-cloud-shell.md)
