# 02 — The core workflow and project files

**Learning objectives**

- Name **init → validate → plan → apply → destroy**
- Know that **plan is a preview**, not a change
- Name the usual `.tf` file roles

---

## One-sentence idea

Write files → **init** (download plugins) → **plan** (show) → **apply** (create) → **destroy** (remove).

![Workflow](../images/tf-workflow.png)

---

## What each command does

| Command | Student words |
| ------- | ------------- |
| `terraform init` | First time in a folder. Downloads **providers**. Prepares backend. Creates `.terraform/` |
| `terraform fmt` | Pretty-print the files (habit) |
| `terraform validate` | “Is the HCL legal?” |
| `terraform plan` | Receipt: **add / change / destroy**. Safe. No create |
| `terraform apply` | Do the work. Type `yes`. Then **state** is updated |
| `terraform destroy` | Remove what **this folder’s state** owns |

Plan line you will see: `Plan: 1 to add, 0 to change, 0 to destroy.`

Optional later: `terraform plan -out=tfplan` then `terraform apply tfplan`.

Destroy one object only: `-target=...` — rare; easy to confuse people. Skip in week 1 unless the tutor shows it.

---

## Provider = plug adapter

![Provider](../images/tf-provider.png)

The **azurerm provider** translates your recipe into Azure API calls.

Pin the version (good habit):

```hcl
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {}
}
```

Then a **resource** block is one Azure object.

---

## Who lives in which file?

| File | Job |
| ---- | --- |
| `providers.tf` | Which cloud plugin + version |
| `main.tf` | Resources (the actual things) |
| `variables.tf` | Input blanks |
| `outputs.tf` | Values to print after apply |
| `terraform.tfvars` | Answers for the blanks |
| `backend.tf` | Where **state** is stored (Day 4) |

Terraform reads **all** `.tf` files in the folder. These names are a **habit**, not a law.

**Working order:** providers → resources in `main.tf` → variables → outputs → tfvars → backend when the team is ready.

---

## After apply, state is the notebook

Apply writes `terraform.tfstate`. Keep it private. Class uses **local** state until Day 4.

---

## Knowledge check

1. Does `plan` create a resource group?
2. What does `init` download?
3. What does `destroy` do?

<details>
<summary>Answers</summary>

1. No — it only shows what *would* happen.  
2. Provider plugins (and it prepares the backend).  
3. It deletes the resources this folder created (the ones in state).

</details>

➡️ Next: [Lab 01B](./Lab-01B-First-Apply.md)
