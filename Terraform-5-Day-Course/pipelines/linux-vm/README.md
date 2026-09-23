# Azure DevOps pipeline — Linux VM with Terraform

This pipeline runs the Terraform in [06_vm_linux](https://github.com/sshabb697/terraform-course/tree/main/06_vm_linux). It uses **Terraform extension tasks** (`TerraformInstaller@1`, `TerraformTaskV4@4`), not Azure CLI scripts.

Install [Terraform by Charles Zipp](https://marketplace.visualstudio.com/items?itemName=charleszipp.azure-pipelines-tasks-terraform). If you use Microsoft DevLabs, change `TerraformTaskV4@4` to `TerraformTask@5`.

---

## What the pipeline does

| Parameter `action` | Result |
| ------------------ | ------ |
| `plan` (default) | `fmt` / `init` / `validate` / `plan` only — **no VM** |
| `apply` | Creates the Linux VM (needs approval if you use the Environment) |
| `destroy` | Deletes the VM and related resources |

CI on `main` runs **plan only**. Apply and destroy are **manual** runs (set the parameter).

---

## One-time Azure setup

### 1. Remote state (required in a pipeline)

The agent is a new machine every run. **Local state is lost.** Uncomment and fill `06_vm_linux/backend.tf`, or pass `-backend-config` as the YAML does.

```bash
az group create -n tfstate-rg -l westeurope
az storage account create -n UNIQUE_STATE_ACCOUNT -g tfstate-rg --sku Standard_LRS
az storage container create -n tfstate --account-name UNIQUE_STATE_ACCOUNT
```

### 2. Azure DevOps service connection

Project settings → **Service connections** → Azure Resource Manager → **Workload identity federation** (or service principal).

Name it exactly: `azure-terraform` (or change `azureServiceConnection` in the YAML).

The identity needs **Contributor** on the subscription (or a resource group you deploy into).

### 3. Pipeline variables (Library)

Create variable group **`terraform-linux-vm`**:

| Variable | Example |
| -------- | ------- |
| `TF_BACKEND_RG` | `tfstate-rg` |
| `TF_BACKEND_STORAGE` | your unique storage account name |
| `TF_BACKEND_CONTAINER` | `tfstate` |
| `TF_BACKEND_KEY` | `06-vm-linux.tfstate` |

No passwords in the repo. The VM uses an SSH key Terraform generates. The private key is in **state** — keep remote state private. Do not print `tls_private_key` in logs.

Optional: in `outputs.tf` add `sensitive = true` on `tls_private_key`.

### 4. Environment (recommended)

Pipelines → **Environments** → `linux-vm-apply` → Approvals and checks → add yourself. Apply/destroy wait for a click.

---

## Create the pipeline

1. Repos: this YAML is in the repo (path below).
2. Pipelines → New pipeline → Azure Repos or GitHub → existing YAML.
3. Select `Terraform-5-Day-Course/pipelines/linux-vm/azure-pipelines-linux-vm.yml` **or** copy the file to `azure-pipelines.yml` in `terraform-course`.
4. If the folder is `06_vm_linux` at repo root, leave `workingDirectory` as `06_vm_linux`.

---

## Run apply

1. Run pipeline → **Run**
2. Set `action` = `apply`
3. Approve the environment
4. When finished: Azure Portal → resource group `my_terraform_rg` (from `terraform.tfvars`) → Linux VM

SSH: get the private key from Terraform state (securely), user `azureuser`. Prefer downloading from a locked storage account, not from pipeline logs.

---

## Cost and security

- VM size `Standard_DS1_v2` is **not free**. Destroy when class ends.
- The NSG allows **SSH from the internet** (`source_address_prefix = "*"`). For real work, lock it to your IP.
- Ubuntu **18.04-LTS** may be retired on new Azure. If apply fails on the image, change `source_image_reference` to Ubuntu 22.04 (`publisher = Canonical`, `offer = 0001-com-ubuntu-server-jammy`, `sku = 22_04-lts`).
- Dynamic public IP + newer Azure often wants **Standard / Static**. If Azure errors on the public IP, change `allocation_method` to `Static` and add `sku = "Standard"`.

Official Terraform-in-pipeline tutorial: [HashiCorp: Azure Pipelines](https://developer.hashicorp.com/terraform/tutorials/automation/azure-pipelines).
