# Azure Cloud Essentials — Teaching Pack

Practical slides **and labs** for day-to-day Azure cloud work: create resources, grant access, store data, run apps, network safely, and keep things healthy and cheap.

> Focus is real admin / DevOps tasks. Skills also help if students take AZ-104 later — but that is optional.

---

## What you will teach

| Module | Everyday skills | Slides | Lab |
| ------ | --------------- | ------ | --- |
| Intro | What Azure is for; Azure vs Azure DevOps | [00](./Slides/00-Course-Intro.md) | — |
| Fundamentals | Subscriptions, RGs, tags, cost, portal/CLI | [01](./Slides/01-Azure-Fundamentals.md) | [Lab 01](./Labs/01-Portal-Resource-Groups-and-Tags.md) |
| Identity & access | Entra ID, RBAC, Policy, locks | [02](./Slides/02-Identity-Governance.md) | [Lab 02](./Labs/02-Identity-RBAC-and-Policy.md) |
| Storage | Blob, Files, SAS, secure sharing | [03](./Slides/03-Storage.md) | [Lab 03](./Labs/03-Storage-Blob-Files-SAS.md) |
| Compute | VM vs App Service vs containers | [04](./Slides/04-Compute.md) | [Lab 04](./Labs/04-Compute-VM-and-App-Service.md) |
| Networking | VNet, NSG, peering, private access | [05](./Slides/05-Networking.md) | [Lab 05](./Labs/05-Networking-VNet-NSG-Peering.md) |
| Monitor & protect | Metrics, alerts, backup | [06](./Slides/06-Monitor-Backup.md) | [Lab 06](./Labs/06-Monitor-Alerts-and-Backup.md) |
| Daily playbook | Habits & troubleshooting | [07](./Slides/07-Daily-Playbook.md) | [Lab 07 Capstone](./Labs/07-Capstone-Mini-Stack.md) |

Full lab index: [Labs/README.md](./Labs/README.md)

---

## How to present the slides

Files use **[Marp](https://marp.app/)** markdown.

1. Install **Marp for VS Code** in Cursor/VS Code.
2. Open a file under `Slides/` → **Open Preview**.
3. Export → PDF or PowerPoint.

```bash
npx @marp-team/marp-cli Slides/01-Azure-Fundamentals.md -o Slides/01-Azure-Fundamentals.pptx
```

---

## How to learn

Work through modules in order: **read the slides → complete the matching lab**.

Pairs with the [Azure DevOps 6-Day Course](../Azure-DevOps-6-Day-Course/): **this pack = Azure cloud**; **DevOps course = CI/CD tooling**.

---

## Prerequisites

- Basic networking (IP, DNS, firewalls)
- Comfortable with a browser and a terminal
- An [Azure](https://azure.microsoft.com/free/) subscription for labs

---

## Tips

- Prefer understanding **choices** (e.g. App Service vs VM) over memorizing every SKU.
- Reuse one resource group (`rg-lab-<yourname>`) across labs, then delete it when you finish.
- After Module 07 / Lab 07, continue with the DevOps course or .NET deployment workshop if that is next for your class.
