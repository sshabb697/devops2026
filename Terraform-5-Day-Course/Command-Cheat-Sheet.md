# Terraform command cheat sheet

Run commands from the folder that contains `.tf` files.

Official docs: [Terraform CLI](https://developer.hashicorp.com/terraform/cli) · [Azure provider](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs)

---

## Everyday loop

```bash
az login
az account show
terraform fmt
terraform init
terraform validate
terraform plan
terraform apply
terraform output
terraform destroy
```

Type `yes` when apply/destroy asks — or use `-auto-approve` only in class when the tutor says so.

Save a plan (optional): `terraform plan -out=tfplan` then `terraform apply tfplan`.

---

## See what Terraform thinks exists

```bash
terraform state list
terraform state show azurerm_resource_group.main
terraform show
terraform providers
```

Refresh state from Azure (no extra creates): `terraform apply -refresh-only`

---

## Variables

```bash
terraform plan -var="location=eastus"
terraform apply -var-file="terraform.tfvars"
```

Environment: `TF_VAR_location=eastus`

---

## Workspaces (optional)

```bash
terraform workspace list
terraform workspace show
terraform workspace new dev
terraform workspace select default
```

---

## Debug

```bash
# PowerShell
$env:TF_LOG="DEBUG"
$env:TF_LOG_PATH="terraform-debug.log"
terraform plan
```

`terraform help plan` for flags.

---

## Azure login reminder

```bash
az login
az account set --subscription "YOUR-SUBSCRIPTION-ID"
```

The `azurerm` provider uses this login.

---

## If you get stuck

| Error | Likely cause |
| ----- | ------------ |
| `No valid credentials` | Run `az login` |
| Storage name already taken | Name must be **globally unique**, lowercase |
| Resource already exists | Import (later) or pick a new name / destroy old one |
| Backend errors | Storage account for state must exist first |
| Locked state | Someone else is applying — wait |
