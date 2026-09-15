# Lab 04B — State in Azure Storage

**Time:** 50 minutes

This lab has two parts: **create the locker**, then **move the notebook**.

---

## Part A — Create state storage (once) (15 min)

Use **your** unique storage name (lowercase, no hyphens). Example: `tfststu847`.

Bash:

```bash
az group create -n tfclass-state-rg -l eastus
az storage account create -n UNIQUE_NAME -g tfclass-state-rg -l eastus --sku Standard_LRS
az storage container create -n tfstate --account-name UNIQUE_NAME
```

Write the storage name down.

---

## Part B — Backend file (10 min)

1. Copy `backend.tf.example` → `backend.tf` and **uncomment** the `terraform { backend "azurerm" {} }` block.
2. Copy `backend.hcl.example` → `backend.hcl`. Fill in:

- `storage_account_name`
- `key` = `studentYOURINITIALS.tfstate`

`backend.hcl` is personal. It is gitignored.

---

## Part C — Migrate (20 min)

From `lab/`:

```bash
terraform init -backend-config=backend.hcl
```

Answer **yes** to copy state to Azure.

```bash
terraform plan
```

Expected: **no changes** (same resources, new notebook location).

Optional: rename local `terraform.tfstate` to `.old` only after a successful plan — tutor confirms first.

---

## Deliverables

- [ ] `init` used Azure backend
- [ ] Plan is clean

**Do not delete `tfclass-state-rg` until Day 5** if you still need the state.

➡️ **Day 5:** [Workflow and capstone](../Day-05-Workflow-and-Capstone/README.md)
