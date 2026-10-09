# 01 — What is a VPC?

**Learning objectives**

- Understand a **VPC** as your own private network in AWS
- Know subnets, CIDR, public vs private

---

## One-sentence idea

A **VPC** is your own private, fenced-off network inside AWS where your servers live.

---

## AWS default VPC (you already have one)

In every region, AWS creates a **default VPC** (usually `172.31.0.0/16`) with subnets in each Availability Zone, an **Internet Gateway**, and routes so instances can get a **public IP**. Many first EC2 launches use this network without extra setup.

You will inspect it in the console in [03 — Default VPC demo](./03-Default-VPC-Demo.md). Later today you build a **custom** VPC (`10.0.0.0/16`) where **you** decide public vs private layout.

---

## Analogy: a gated housing estate

- **VPC** = the whole gated estate, with one big address range.
- **Subnet** = a street inside the estate.
- **Public subnet** = a street with a gate to the main road (the internet).
- **Private subnet** = an inner street with no direct gate — safer for databases.
- **Route table** = the signposts telling traffic which way to go.

---

## CIDR: the address range

A VPC gets an IP range written in **CIDR** notation:

```text
VPC:            10.0.0.0/16     → 65,536 addresses (10.0.0.0 – 10.0.255.255)
 ├ Public subnet  10.0.1.0/24   → 256 addresses, has a route to the internet
 └ Private subnet 10.0.2.0/24   → 256 addresses, no direct internet
```

- `/16` = big (whole VPC). `/24` = smaller slice (one subnet).
- Smaller number after `/` = **more** addresses.

---

## Public vs private — the key difference

| | Public subnet | Private subnet |
| - | ------------- | -------------- |
| Route to internet | Yes, via **Internet Gateway** | No direct route |
| Who goes here | Web servers, load balancers | Databases, app servers |
| Outbound internet | Direct | Via **NAT Gateway** only |

---

## The gateways

- **Internet Gateway (IGW):** the estate's main gate. Lets public-subnet resources talk to the internet both ways.
- **NAT Gateway:** a one-way door. Lets private-subnet resources reach *out* (e.g. download updates) but blocks the internet from reaching *in*.

```text
Public subnet  ─▶ Internet Gateway ─▶ Internet  (two-way)
Private subnet ─▶ NAT Gateway ─▶ IGW ─▶ Internet (outbound only)
```

---

## Knowledge check

1. Where would you put a database — public or private subnet? Why?
2. What does a NAT Gateway allow that a plain private subnet cannot?

<details>
<summary>Answers</summary>

1. Private subnet — databases shouldn't be reachable from the internet; only your app servers talk to them.
2. Outbound internet access (e.g. OS updates) from private instances, without exposing them to inbound traffic.

</details>

➡️ Next: [03 — Default VPC demo](./03-Default-VPC-Demo.md)
