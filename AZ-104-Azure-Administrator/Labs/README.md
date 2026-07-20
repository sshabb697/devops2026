# Azure Cloud Essentials — Labs

Two lab tracks are available. Use one or both depending on your class plan.

## Track A — Module labs (cloud essentials)

Match the slide modules (identity, storage, compute, networking, monitor, capstone).

| Lab | Topic | Time | After slides |
| --- | ----- | ---- | ------------ |
| [01](./01-Portal-Resource-Groups-and-Tags.md) | Portal, RG, tags, cost, Cloud Shell | 45–60m | Module 01 |
| [02](./02-Identity-RBAC-and-Policy.md) | Groups, RBAC, Policy, locks | 45–60m | Module 02 |
| [03](./03-Storage-Blob-Files-SAS.md) | Storage account, Blob, SAS, Files | 45–60m | Module 03 |
| [04](./04-Compute-VM-and-App-Service.md) | VM + App Service | 60–75m | Module 04 |
| [05](./05-Networking-VNet-NSG-Peering.md) | VNet, NSG, peering | 60–75m | Module 05 |
| [06](./06-Monitor-Alerts-and-Backup.md) | Metrics, alerts, backup | 45–60m | Module 06 |
| [07](./07-Capstone-Mini-Stack.md) | Build a small end-to-end stack | 60–90m | Module 07 |

## Track B — Day 1 infrastructure challenges

Deeper classic infrastructure labs (VNet → VM → Shell → Storage → ARM → Peering → Load Balancer + optional stretch).

**Start here:** [Day1-Infrastructure-Challenges/README.md](./Day1-Infrastructure-Challenges/README.md)

| # | Challenge |
| - | --------- |
| 00 | [Virtual Network](./Day1-Infrastructure-Challenges/challenge-00-vnet.md) |
| 01 | [Virtual Machine](./Day1-Infrastructure-Challenges/challenge-01-vm.md) |
| 02 | [Cloud Shell](./Day1-Infrastructure-Challenges/challenge-02-cloud-shell.md) |
| 03 | [Storage (Blob, SAS, Files)](./Day1-Infrastructure-Challenges/challenge-03-storage.md) |
| 04 | [ARM / Bicep template](./Day1-Infrastructure-Challenges/challenge-04-arm-template.md) |
| 05 | [VNet peering](./Day1-Infrastructure-Challenges/challenge-05-vnet-peering.md) |
| 06 | [Load Balancer](./Day1-Infrastructure-Challenges/challenge-06-load-balancer.md) |
| 07 | [Custom Script Extension](./Day1-Infrastructure-Challenges/challenge-07-custom-script-extension.md) *(optional)* |
| 08 | [Traffic Manager](./Day1-Infrastructure-Challenges/challenge-08-traffic-manager.md) *(optional)* |
| 09 | [Automation & cost](./Day1-Infrastructure-Challenges/challenge-09-automation-cost.md) *(optional)* |

Inspired by [sshabb697/trainingdays day1](https://github.com/sshabb697/trainingdays/tree/master/day1).

---

## Before you start

1. Sign in to [portal.azure.com](https://portal.azure.com) with a subscription you can use.
2. Pick a nearby **region** and reuse it (e.g. `East US`, `Central India`).
3. Replace placeholders:
   - `<yourname>` → short name (`alex`)
   - `<region>` → your chosen region
4. Prefer **cheap SKUs** (Free / B1 / Burstable / Standard LRS).

## Naming convention (module labs)

| Resource | Pattern | Example |
| -------- | ------- | ------- |
| Resource group | `rg-lab-<yourname>` | `rg-lab-alex` |
| Storage | `stlab<yourname><nn>` (globally unique) | `stlabalex01` |
| VM | `vm-lab-<yourname>` | `vm-lab-alex` |
| App Service | `app-lab-<yourname>-<nn>` | `app-lab-alex-01` |
| VNet | `vnet-lab-<yourname>` | `vnet-lab-alex` |

Day 1 challenges use `rg-d1-<yourname>` — see that track’s README.

## Cost & cleanup

```bash
az group delete -n rg-lab-<yourname> --yes --no-wait
az group delete -n rg-d1-<yourname> --yes --no-wait
```

Or in Portal: Resource group → **Delete resource group**.

