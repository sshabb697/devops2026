# Challenge 00 — Create a Virtual Network

**Time:** 30–40 minutes  
**You will learn:** Create a resource group, VNet, subnet, and public IP using the Azure Portal and a clear naming convention.

## Goal

Build the network foundation for later VM challenges:

```
rg-d1-<yourname>
 └── vnet-d1-<yourname>-a   (10.1.0.0/16)
      └── snet-d1-<yourname>-app   (10.1.0.0/24)
 └── pip-d1-<yourname>-vm   (public IP for the next lab)
```

---

## Step 1 — Sign in

1. Open [https://portal.azure.com](https://portal.azure.com).
2. Confirm you are in the correct **subscription** (top search → **Subscriptions**).
3. Tip: use a private/incognito window if you have multiple Microsoft accounts.

---

## Step 2 — Create a resource group

1. Click **+ Create a resource** → search **Resource group** → **Create**.  
   Or go to **Resource groups → Create**.
2. Fill in:

| Field | Value |
| ----- | ----- |
| Subscription | Your subscription |
| Resource group | `rg-d1-<yourname>` |
| Region | `<region>` |

3. **Tags** tab:

| Name | Value |
| ---- | ----- |
| Owner | `<yourname>` |
| Env | Lab |
| Day | Day1 |

4. **Review + create → Create**.

✅ **Checkpoint:** RG appears under Resource groups.

---

## Step 3 — Create the Virtual Network

1. **+ Create a resource** → search **Virtual network** → **Create**.
2. **Basics:**

| Field | Value |
| ----- | ----- |
| Resource group | `rg-d1-<yourname>` |
| Name | `vnet-d1-<yourname>-a` |
| Region | Same as RG |

3. **IP addresses** tab:
   - Address space: `10.1.0.0/16`
   - Remove default subnet if needed; add:

| Subnet name | Address range |
| ----------- | ------------- |
| `snet-d1-<yourname>-app` | `10.1.0.0/24` |

4. Tags: same as above (`Owner`, `Env=Lab`, `Day=Day1`).
5. **Review + create → Create**.

✅ **Checkpoint:** VNet shows one subnet `snet-d1-<yourname>-app`.

---

## Step 4 — Create a Public IP

1. **+ Create a resource** → search **Public IP address** → **Create**.
2. Settings:

| Field | Value |
| ----- | ----- |
| Resource group | `rg-d1-<yourname>` |
| Region | `<region>` |
| Name | `pip-d1-<yourname>-vm` |
| IP Version | IPv4 |
| SKU | **Standard** (recommended) |
| Assignment | Static |
| DNS name label | something unique, e.g. `d1vm-<yourname>-01` |

3. Tags → **Review + create → Create**.

✅ **Checkpoint:** Public IP resource exists and shows an address (or “Allocated” after attach in Challenge 01).

---

## Naming reference

See [Azure naming abbreviations](https://learn.microsoft.com/azure/cloud-adoption-framework/ready/azure-best-practices/resource-abbreviations) (`vnet-`, `snet-`, `pip-`, `rg-`).

---

## Deliverables

- [ ] Resource group `rg-d1-<yourname>`
- [ ] VNet `10.1.0.0/16` with app subnet `/24`
- [ ] Public IP ready for the VM lab
- [ ] Tags applied

## Cleanup

Keep this RG for Challenges 01–03. Delete only if your instructor says so.

➡️ Next: [Challenge 01 — Create a VM](./challenge-01-vm.md)
