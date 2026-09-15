# Lab 02B — Outputs and state list

**Time:** 50 minutes  
Same folder as Lab 02A (`lab/`).

---

## Part A — Outputs (15 min)

```bash
terraform output
terraform output rg_name
```

Expected: the resource group name.

---

## Part B — Peek at state (safely) (20 min)

```bash
terraform state list
terraform state show azurerm_resource_group.main
```

Look at `id` and `location`. **Do not** open `.tfstate` in an editor to “fix” it.

---

## Part C — Destroy or keep (15 min)

If you continue Day 3 in a **new** folder, destroy this lab:

```bash
terraform destroy
```

---

## Deliverables

- [ ] `terraform output` works
- [ ] `terraform state list` shows the resource group

➡️ **Day 3:** [Azure resources](../Day-03-Azure-Resources/README.md)
