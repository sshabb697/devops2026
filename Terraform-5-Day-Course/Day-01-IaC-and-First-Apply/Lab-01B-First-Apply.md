# Lab 01B — First resource group

**Time:** 50 minutes  
Folder: `Day-01-IaC-and-First-Apply/lab/`

---

## Part A — Copy the files (5 min)

Open `lab/main.tf` and `lab/providers.tf`. Change `tfclass` in the resource group name to **your initials** so names do not clash.

---

## Part B — The loop (30 min)

```bash
cd lab
terraform init
terraform fmt
terraform validate
terraform plan
terraform apply
```

Type `yes`. Wait.

Portal: search your resource group. It should exist.

```bash
terraform show
```

---

## Part C — Destroy (15 min)

```bash
terraform destroy
```

Type `yes`. Portal: the group is gone.

If the tutor says keep it for Day 2, skip destroy and **tell the tutor**.

---

## If you get stuck

| Error | Fix |
| ----- | --- |
| credentials | `az login` |
| `subscription_id` required | You have provider 4.x — see comment in `providers.tf` |
| name exists | Change the resource group name |

---

## Deliverables

- [ ] `apply` created a resource group
- [ ] You saw it in the Portal
- [ ] You know how to `destroy`

➡️ **Day 2:** [HCL, variables, state](../Day-02-HCL-Variables-State/README.md)
