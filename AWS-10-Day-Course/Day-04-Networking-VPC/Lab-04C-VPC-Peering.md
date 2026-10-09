# Lab 04C — VPC peering (step-by-step)

**Time:** 45–60 minutes (extension lab)  
**Goal:** Two VPCs peered; **ping** from an instance in VPC-A to a **private IP** in VPC-B.

**Prerequisites:** Comfortable with EC2 launch and security groups (Day 3).

> **Cost:** Two `t2.micro` instances for ~1 hour. **No NAT Gateway** required if you use **public subnets** only for SSH, then test **private** IPs over peering.

---

## Before you start — naming

Use your initials everywhere:

| Resource | Example name |
| -------- | ------------ |
| VPC A | `vpc-a-<initials>` · CIDR `10.1.0.0/16` |
| VPC B | `vpc-b-<initials>` · CIDR `10.2.0.0/16` |
| Peering | `peer-a-to-b-<initials>` |
| Instances | `server-a-<initials>`, `server-b-<initials>` |

---

## Part 1 — Create VPC-A (10 min)

### Step 1.1 — Open the VPC wizard

1. AWS Console → **VPC**.
2. Click **Create VPC**.
3. Select **VPC and more**.

### Step 1.2 — Configure VPC-A

| Field | Value |
| ----- | ----- |
| Name tag | `vpc-a-<initials>` |
| IPv4 CIDR | `10.1.0.0/16` |
| Availability Zones | **1** |
| Public subnets | **1** |
| Private subnets | **0** |
| NAT gateways | **None** |
| VPC endpoints | None |

4. Click **Create VPC**. Wait until status is **Available**.

### Step 1.3 — Verify VPC-A

1. **VPCs** → select `vpc-a-<initials>`.
2. Note the **VPC ID** (e.g. `vpc-0abc…`) in your notes.
3. **Subnets** → confirm one **public** subnet in `10.1.x.x/24` range.

✅ **Checkpoint 1:** VPC-A exists with **one public subnet**, no overlapping CIDR with `10.2.0.0/16`.

---

## Part 2 — Create VPC-B (8 min)

Repeat Part 1 with:

| Field | Value |
| ----- | ----- |
| Name | `vpc-b-<initials>` |
| CIDR | `10.2.0.0/16` |
| Public subnets | **1** |
| Private / NAT | **0** / **None** |

✅ **Checkpoint 2:** VPC-B exists; CIDR is `10.2.0.0/16`.

---

## Part 3 — Launch EC2 in each VPC (12 min)

### Step 3.1 — Security group for VPC-A (server-a)

1. **EC2 → Security Groups → Create**.
2. Name `sg-server-a-<initials>`, VPC = **vpc-a**.
3. **Inbound rules:**

| Type | Port | Source | Why |
| ---- | ---- | ------ | --- |
| SSH | 22 | **My IP** | You SSH from laptop |
| All ICMP - IPv4 | All | `10.2.0.0/16` | Ping from VPC-B after peering |

4. Create.

### Step 3.2 — Launch server-a

1. **EC2 → Launch instance**.
2. Name: `server-a-<initials>`.
3. AMI: **Amazon Linux 2023**, type `t2.micro`.
4. Key pair: your class key.
5. **Network settings → Edit:**
   - VPC: **vpc-a**
   - Subnet: **public** subnet of vpc-a
   - **Auto-assign public IP:** Enable
   - Security group: `sg-server-a-<initials>`
6. Launch.

### Step 3.3 — Security group and instance in VPC-B

1. Create `sg-server-b-<initials>` in **vpc-b** with:
   - SSH **22** from **My IP**
   - ICMP from `10.1.0.0/16`
2. Launch `server-b-<initials>` in vpc-b **public** subnet, public IP enabled.

### Step 3.4 — Record private IPs

1. **EC2 → Instances**.
2. Copy **Private IPv4** for server-a and server-b (e.g. `10.1.1.13`, `10.2.1.139`).

✅ **Checkpoint 3:** Both instances **running**; you have both **private** IPs written down.

---

## Part 4 — Create peering connection (8 min)

### Step 4.1 — Request peering

1. **VPC → Peering connections → Create peering connection**.
2. **Name:** `peer-a-to-b-<initials>`.
3. **Requester VPC:** `vpc-a-<initials>`.
4. **Accepter:** **My account**, same Region, **vpc-b-<initials>`.
5. **Create peering connection**.

### Step 4.2 — Accept (same account)

1. Select the new connection — state **Pending acceptance**.
2. **Actions → Accept request**.
3. Wait until **Status** = **Active**.

✅ **Checkpoint 4:** Peering status is **Active** (routing not done yet).

---

## Part 5 — Update route tables (10 min)

You need **one route per VPC** pointing at the **other VPC’s CIDR** through the peering connection.

### Step 5.1 — Route in VPC-A

1. **VPC → Route tables**.
2. Find the route table associated with vpc-a’s **public** subnet (check **Subnet associations** tab).
3. Select it → **Routes → Edit routes → Add route**:

| Destination | Target |
| ----------- | ------ |
| `10.2.0.0/16` | **Peering connection** → `peer-a-to-b-<initials>` |

4. **Save changes**.

### Step 5.2 — Route in VPC-B

1. Open the route table for vpc-b’s public subnet.
2. **Add route:**

| Destination | Target |
| ----------- | ------ |
| `10.1.0.0/16` | Same **peering connection** |

3. Save.

✅ **Checkpoint 5:** Each side has a route to the **remote /16** via `pcx-…`.

---

## Part 6 — Test connectivity (8 min)

### Step 6.1 — SSH to server-a

```bash
ssh -i class-key.pem ec2-user@<SERVER_A_PUBLIC_IP>
```

### Step 6.2 — Ping server-b private IP

```bash
ping -c 4 <SERVER_B_PRIVATE_IP>
```

Expected: replies from `10.2.x.x`.

### Step 6.3 — Optional reverse test

SSH to server-b and ping server-a’s **private** IP.

✅ **Checkpoint 6:** Ping works both directions (or at least A → B).

---

## Part 7 — Cleanup (5 min)

Delete in this order to avoid dependency errors:

1. **Terminate** `server-a` and `server-b`.
2. **VPC → Peering connections** → select peering → **Actions → Delete**.
3. **Delete VPCs** `vpc-a` and `vpc-b` (deletes subnets, IGWs, route tables attached).

Or use **VPC → Your VPCs → Actions → Delete** for each after instances are gone.

---

## If you get stuck

| Symptom | Fix |
| ------- | --- |
| Peering won’t create | CIDRs overlap — must be `10.1/16` and `10.2/16`, not two `10.0/16` |
| Active but ping fails | Missing route on **one** side; wrong route table (subnet not associated) |
| Request timeout | Security group missing ICMP or wrong source CIDR |
| Cannot SSH | Wrong public IP; SG not **My IP**; instance not in public subnet |

---

## Deliverables

- [ ] Screenshot: peering **Active**
- [ ] Screenshot: route table showing `10.2.0.0/16 → pcx-…` (or reverse)
- [ ] Terminal output: successful `ping` to remote private IP
- [ ] All peering lab resources **deleted**

➡️ Next: [05 — Elastic Load Balancing](./05-Elastic-Load-Balancing.md) → [Lab 04D](./Lab-04D-Application-Load-Balancer.md)
