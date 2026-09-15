# 01 — Files, variables, types, and outputs

**Learning objectives**

- Know common file names: `main.tf`, `variables.tf`, `outputs.tf`, `terraform.tfvars`
- A **variable** is a blank the recipe fills later
- Know **string / number / bool** (maps exist too)
- Know **which value wins** if you set a variable three ways

---

## One-sentence idea

**HCL** is Terraform’s language. Variables = **inputs**. Outputs = **results** after apply.

![Variables](../images/tf-variables.png)

---

## Everyday analogy: a form

`variables.tf` = blank fields (name, city).  
`terraform.tfvars` = your answers.  
`main.tf` = the printed letter that uses those answers.  
`outputs.tf` = the stamp on the envelope (ID, URL) you show the class.

---

## Example

```hcl
variable "location" {
  type        = string
  description = "Azure region"
  default     = "eastus"
}

resource "azurerm_resource_group" "main" {
  name     = var.rg_name
  location = var.location
}

output "rg_name" {
  value = azurerm_resource_group.main.name
}
```

Add `type` and `description` when you can. It helps the next student.

---

## Data types (basics only)

| Type | Meaning | Class example |
| ---- | ------- | ------------- |
| `string` | Text | `"eastus"` |
| `number` | Count | `1` |
| `bool` | true/false | `true` |
| `list` | Ordered list | `["eastus", "westus"]` |
| `map` | Key + value | `{ owner = "ana" }` |

Day 2 labs use **string**. Lists/maps show up in tags later.

---

## Three ways to fill a variable (who wins)

Highest first:

1. Command line: `terraform plan -var="location=westus"`
2. Environment: `TF_VAR_location` (PowerShell: `$env:TF_VAR_location="westus"`)
3. `terraform.tfvars` or `*.auto.tfvars`
4. `default` inside `variables.tf` (**lowest**)

---

## Knowledge check

1. Should `terraform.tfvars` with real passwords go to GitHub?
2. What file usually holds `variable` blocks?
3. Does `-var` beat `default`?

<details>
<summary>Answers</summary>

1. No.  
2. `variables.tf` (by habit — Terraform reads all `.tf` files).  
3. Yes.

</details>

➡️ Next: [Lab 02A](./Lab-02A-Variables.md)
