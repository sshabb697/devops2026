# Lab 05B — Capstone and cleanup

**Time:** 50 minutes  
**Required:** leave Azure clean.

---

## Part A — Capstone apply (20 min)

Folder: `lab-capstone/`

This is Day 3 again, as a checklist. Edit `prefix` in `tfvars`.

```bash
cd lab-capstone
terraform init
terraform plan
terraform apply
terraform output website_url
```

Browser works = pass.

---

## Part B — Destroy capstone (10 min)

```bash
terraform destroy
```

---

## Part C — Destroy earlier days (15 min)

For **each** folder where you still have state (Day 2, 3, 4):

```bash
cd THAT_LAB_FOLDER
terraform destroy
```

If Day 4 used remote state: destroy **work resources first**, then:

```bash
az group delete -n tfclass-state-rg --yes --no-wait
```

---

## Part D — Portal check (5 min)

Search resource groups starting with your prefix / `tfclass`.  
Tutor signs off: **none left**.

---

## You can now

- Explain IaC in one sentence
- Run init / plan / apply / destroy
- Use variables, outputs, a module
- Know why state matters

Next: Terraform in an Azure DevOps pipeline.

Congratulations — 5 days complete.
