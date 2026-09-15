# Lab 03A — Storage account

**Time:** 40 minutes  
Folder: `Day-03-Azure-Resources/lab/`

Edit `terraform.tfvars` `prefix` to your initials (lowercase letters only).

```bash
cd lab
terraform init
terraform plan
terraform apply
```

```bash
terraform output
```

You should see a storage account name.

Portal: open the resource group → storage account exists.

**Do not destroy yet** — Lab 03B adds the website.

---

## If name is taken

`prefix` + random suffix should be unique. Change `prefix` and apply again.

---

## Deliverables

- [ ] Storage account in the Portal

➡️ Next: [02 — Website](./02-Website.md)
