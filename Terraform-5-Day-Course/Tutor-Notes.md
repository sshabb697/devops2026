# Tutor notes (5 days)

## Before Day 1

- Students need Azure CLI + a subscription.
- Install Terraform: [Install Terraform](https://developer.hashicorp.com/terraform/install).
- Decide a **name prefix** (example: `tfclass` + student initials) so storage names do not clash.
- Slides: Marp preview, same as Kubernetes course.

## Daily rhythm

1. Picture on the projector.
2. Lab — students type. Do not click the Portal “for them.”
3. End of day: `terraform destroy` unless they continue tomorrow in the **same folder**.

## Cost

Resource group + storage is cheap. Forgotten storage accounts add up. **Day 5 destroy is required.** You check the Portal for leftover `tfclass-*` groups.

## Common stalls

| Day | Stall | What you do |
| --- | ----- | ----------- |
| 1 | Terraform not in PATH | New terminal after install |
| 1 | Provider download slow | Wait; check proxy |
| 2 | Students edit `.tfstate` | Stop them. Restore from git? State is not in git. Recreate. |
| 3 | Storage name taken | Add random digits |
| 4 | Chicken-egg remote state | Create state storage **once** with CLI or Day 3 leftover — lab explains |
| 5 | Destroy fails | `az group delete` as last resort after explaining it is not the Terraform way |

## Extra reading for you

Student PDF on this PC: `C:\Users\SPALPT145\Terraform Basics to Advanced in One Guide_v1.0 (1).pdf`  
How we mapped it: [Resources/From-Your-Guide.md](./Resources/From-Your-Guide.md)

- [HashiCorp Learn: Azure](https://developer.hashicorp.com/terraform/tutorials/azure-get-started)
- [Azure RM provider docs](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs)
