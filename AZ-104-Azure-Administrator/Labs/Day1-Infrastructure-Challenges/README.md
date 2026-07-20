# Day 1 — Azure Infrastructure Challenges

Hands-on challenges inspired by [trainingdays/day1](https://github.com/sshabb697/trainingdays/tree/master/day1), rewritten with **step-by-step instructions** for this course.

Focus: **networking, VMs, storage, Cloud Shell, ARM/Bicep, load balancing**, plus optional stretch labs.

## Challenge list

| # | Challenge | Time | Required? |
| - | --------- | ---- | --------- |
| [00](./challenge-00-vnet.md) | Create a Virtual Network (+ public IP) | 30–40m | Yes |
| [01](./challenge-01-vm.md) | Create a Virtual Machine in the portal | 40–50m | Yes |
| [02](./challenge-02-cloud-shell.md) | Cloud Shell — manage Azure from the browser | 30–40m | Yes |
| [03](./challenge-03-storage.md) | Storage — Blob, SAS, File Share | 45–60m | Yes |
| [04](./challenge-04-arm-template.md) | Deploy with an ARM / Bicep template | 45–60m | Yes |
| [05](./challenge-05-vnet-peering.md) | Connect two VNets with peering | 40–50m | Yes |
| [06](./challenge-06-load-balancer.md) | Public Load Balancer in front of web VMs | 50–70m | Yes |
| [07](./challenge-07-custom-script-extension.md) | Custom Script Extension (post-deploy config) | 40–50m | Optional |
| [08](./challenge-08-traffic-manager.md) | Traffic Manager across regions | 45–60m | Optional |
| [09](./challenge-09-automation-cost.md) | Automation + cost awareness | 40–50m | Optional |

## Before you start

1. Sign in at [portal.azure.com](https://portal.azure.com).
2. Pick one region and reuse it: `<region>` (e.g. `Central India`, `East US`, `West Europe`).
3. Replace `<yourname>` with a short unique id (`alex`, `student03`).
4. Prefer cheap sizes: **B1s / B2s**, **Standard SSD**, **LRS**.

## Naming (use consistently)

| Type | Pattern | Example |
| ---- | ------- | ------- |
| Resource group | `rg-d1-<yourname>` | `rg-d1-alex` |
| VNet | `vnet-d1-<yourname>-a` | `vnet-d1-alex-a` |
| Subnet | `snet-d1-<yourname>-app` | `snet-d1-alex-app` |
| Public IP | `pip-d1-<yourname>-vm` | `pip-d1-alex-vm` |
| VM | `vm-d1-<yourname>-01` | `vm-d1-alex-01` |
| Storage | `std1<yourname>01` | `std1alex01` |

## Suggested path

```
00 VNet → 01 VM → 02 Cloud Shell → 03 Storage
       → 04 ARM → 05 Peering → 06 Load Balancer
       → (optional) 07 CSE → 08 Traffic Manager → 09 Automation
```

## Cleanup

When you finish Day 1 challenges:

```bash
az group list --query "[?starts_with(name,'rg-d1-')].name" -o tsv
# delete each lab RG you created, e.g.:
az group delete -n rg-d1-<yourname> --yes --no-wait
```

## How this relates to the other labs

| This track | Module labs in `../Labs/` |
| ---------- | ------------------------- |
| Infra building blocks (VNet, VM, storage, LB) | Broader cloud essentials (RBAC, Policy, App Service, Monitor, Capstone) |

Do **both** if you have time: Module labs for daily admin skills; Day 1 challenges for classic infrastructure depth.

## Credit

Challenge ideas adapted from [sshabb697/trainingdays day1](https://github.com/sshabb697/trainingdays/tree/master/day1) (Azure Dev College style training). Steps rewritten for this repository.
