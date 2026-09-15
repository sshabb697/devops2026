# Lab 02A — Variables

**Time:** 40 minutes  
Folder: `Day-02-HCL-Variables-State/lab/`

---

## Part A — Set your names (10 min)

Edit `terraform.tfvars`:

- `rg_name` — include your initials
- `location` — tutor’s region (often `eastus`)

---

## Part B — Plan and apply (25 min)

```bash
cd lab
terraform init
terraform plan
terraform apply
```

Change `location` in `tfvars` (only if the tutor agrees — moving a RG **recreates** it). For class, change a **tag** instead:

Edit `main.tf` tag `owner = "your-name"`, then `terraform plan`. You should see **1 to change**.

```bash
terraform apply
```

**Optional:** set a variable from the terminal (this beats `default`):

PowerShell: `$env:TF_VAR_owner="from-cli"` then `terraform plan` — you should see that owner.

---

## Deliverables

- [ ] Plan used values from `terraform.tfvars`
- [ ] A tag update showed in plan

➡️ Next: [02 — State](./02-State.md)
