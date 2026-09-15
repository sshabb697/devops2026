# Workspaces (optional — not in the 3-hour lab)

A **workspace** is a second copy of state for the same code (`default`, `dev`, `prod`).

```bash
terraform workspace new dev
terraform workspace list
terraform workspace select default
terraform workspace show
```

You can use the name in a resource: `"${var.prefix}-${terraform.workspace}"`.

**Class choice:** we split environments with **variables + remote state keys**, not workspaces. Workspaces are easy to mix up on one laptop.

If you try them: apply in `dev`, then `select default` before destroy so you do not destroy the wrong copy.
