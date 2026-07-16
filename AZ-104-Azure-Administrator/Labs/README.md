# Azure Cloud Essentials — Labs

Hands-on labs that match the slide modules. Each lab is written for the **Azure Portal** first, with optional CLI where it helps.

## Lab list

| Lab | Topic | Time | After slides |
| --- | ----- | ---- | ------------ |
| [01](./01-Portal-Resource-Groups-and-Tags.md) | Portal, RG, tags, cost, Cloud Shell | 45–60m | Module 01 |
| [02](./02-Identity-RBAC-and-Policy.md) | Groups, RBAC, Policy, locks | 45–60m | Module 02 |
| [03](./03-Storage-Blob-Files-SAS.md) | Storage account, Blob, SAS, Files | 45–60m | Module 03 |
| [04](./04-Compute-VM-and-App-Service.md) | VM + App Service | 60–75m | Module 04 |
| [05](./05-Networking-VNet-NSG-Peering.md) | VNet, NSG, peering | 60–75m | Module 05 |
| [06](./06-Monitor-Alerts-and-Backup.md) | Metrics, alerts, backup | 45–60m | Module 06 |
| [07](./07-Capstone-Mini-Stack.md) | Build a small end-to-end stack | 60–90m | Module 07 |

## Before you start

1. Sign in to [portal.azure.com](https://portal.azure.com) with a subscription you can use.
2. Pick a nearby **region** and reuse it for all labs (e.g. `East US`, `Central India`).
3. Replace placeholders:
   - `<yourname>` → short name (`alex`)
   - `<region>` → your chosen region
4. Prefer **cheap SKUs** (Free / B1 / Burstable / Standard LRS).

## Naming convention

| Resource | Pattern | Example |
| -------- | ------- | ------- |
| Resource group | `rg-lab-<yourname>` | `rg-lab-alex` |
| Storage | `stlab<yourname><nn>` (globally unique) | `stlabalex01` |
| VM | `vm-lab-<yourname>` | `vm-lab-alex` |
| App Service | `app-lab-<yourname>-<nn>` | `app-lab-alex-01` |
| VNet | `vnet-lab-<yourname>` | `vnet-lab-alex` |

## Cost & cleanup

At the end of each lab day:

```bash
az group delete -n rg-lab-<yourname> --yes --no-wait
```

Or in Portal: Resource group → **Delete resource group**.

> Capstone lab (07) asks you to rebuild, then delete — that is intentional practice.

## Instructor tips

- Do a **demo** of the lab’s first half before students start.
- Walk the room during “Checkpoint” sections.
- For Lab 02, either use a second test user or demonstrate RBAC with one student volunteering.
- If subscription blocks public IPs / VMs, skip VM parts and focus on App Service + networking diagrams.
