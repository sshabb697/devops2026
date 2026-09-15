# Lab 04A — Use a module

**Time:** 40 minutes  
Folder: `Day-04-Modules-and-Remote-State/lab/`

Edit `terraform.tfvars` `prefix`.

```bash
cd lab
terraform init
terraform plan
terraform apply
terraform output website_url
```

Open the URL. Same result as Day 3, but **root `main.tf` is short**.

Look at `modules/web/` — that is the cookie cutter.

Leave this applied for Lab 04B if possible.

---

## Deliverables

- [ ] Website works
- [ ] You can point to the module folder

➡️ Next: [02 — Remote state](./02-Remote-State.md)
