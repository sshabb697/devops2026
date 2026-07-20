# Challenge 05 — VNet Peering

**Time:** 40–50 minutes  
**You will learn:** Connect two VNets so resources can talk using private IPs.

## Target architecture

```
  vnet-d1-<yourname>-a (10.1.0.0/16)     vnet-d1-<yourname>-b (10.2.0.0/16)
  └── snet-app 10.1.0.0/24               └── snet-shared 10.2.0.0/24
       └── vm-a (optional)                    └── vm-b (optional)
              ▲                                      ▲
              └──────────── peering ─────────────────┘
```

Address spaces **must not overlap**.

---

## Step 1 — Create second VNet

1. Create Virtual network:
   - Name: `vnet-d1-<yourname>-b`
   - RG: `rg-d1-<yourname>` (or new `rg-d1-<yourname>-peer`)
   - Address space: `10.2.0.0/16`
   - Subnet: `snet-d1-<yourname>-shared` → `10.2.0.0/24`
2. Tags: `Owner`, `Env=Lab`, `Day=Day1`.

✅ **Checkpoint:** Two VNets with different CIDRs.

---

## Step 2 — Create peering (both directions)

1. Open `vnet-d1-<yourname>-a` → **Peerings → Add**.
2. Settings:

| Field | Value |
| ----- | ----- |
| Peering link name (this VNet) | `peer-a-to-b` |
| Virtual network | `vnet-d1-<yourname>-b` |
| Peering link name (remote) | `peer-b-to-a` |
| Traffic to remote VNet | Allow |
| Traffic forwarded | Allow (lab default OK) |

3. **Add**. Wait until both peerings show **Connected**.

Portal often creates the reverse peering in the same wizard.

✅ **Checkpoint:** Peering status **Connected** on both VNets.

---

## Step 3 — Optional connectivity test

If you already have `vm-d1-<yourname>-01` on VNet A:

1. Create a small second VM on VNet B (`vm-d1-<yourname>-02`), B1s, same credentials pattern.
2. NSG: allow SSH/RDP from your IP; allow ICMP or SSH from `10.1.0.0/16` ↔ `10.2.0.0/16` as needed.
3. From VM A, ping or SSH to VM B’s **private** IP (not public).

```
# From vm-a
ping <private-ip-of-vm-b>
```

> If ping fails, check NSG and Windows firewall — peering Connected is still success for the networking goal.

---

## Step 4 — Know the gotchas

| Rule | Why it matters |
| ---- | -------------- |
| No overlapping IPs | Peering will fail or routing breaks |
| Not transitive | A↔B and B↔C does **not** mean A↔C |
| NSG still applies | Peering ≠ open firewall |

---

## Deliverables

- [ ] Second VNet created  
- [ ] Bidirectional peering **Connected**  
- [ ] (Optional) Private IP test between VMs  

## Cleanup

Delete extra VMs after the test. Keep peering if continuing to Challenge 06 in a fresh RG, or delete the peer lab RG when done.

➡️ Next: [Challenge 06 — Load Balancer](./challenge-06-load-balancer.md)
