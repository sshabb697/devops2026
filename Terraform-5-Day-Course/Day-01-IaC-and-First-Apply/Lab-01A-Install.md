# Lab 01A — Install Terraform and login to Azure

**Time:** 40 minutes

---

## Part A — Install Terraform (15 min)

Follow [Install Terraform](https://developer.hashicorp.com/terraform/install) for your OS.

**Windows (easy):** use the installer or `winget install Hashicorp.Terraform`

New terminal, then:

```bash
terraform version
```

Expected: a version number (1.5 or newer is fine).

---

## Part B — Azure CLI login (15 min)

```bash
az login
az account show --query name -o tsv
```

Confirm this is the **class** subscription, not a production one.

```bash
az version
```

---

## Part C — Empty folder (10 min)

```bash
mkdir tf-class
cd tf-class
```

Keep this folder for the week. All labs live in copies under `Terraform-5-Day-Course/Day-0N-.../lab`.

---

## Deliverables

- [ ] `terraform version` works
- [ ] `az account show` shows the right subscription

➡️ Next: [02 — Four commands](./02-Four-Commands.md)
