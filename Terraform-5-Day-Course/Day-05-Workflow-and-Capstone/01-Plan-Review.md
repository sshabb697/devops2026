# 01 — Read the plan

**Learning objectives**

- Colors of a plan: **create +**, **change ~**, **destroy -**
- Never apply a plan you did not read if it destroys a database

---

## One-sentence idea

`terraform plan` is the **dress rehearsal**. `apply` is opening night.

---

## Everyday analogy: a shopping receipt

Before you pay, you check: did it add 3 apples or delete your fridge?

In class, unexpected **destroy** of a resource group means you renamed it — Azure cannot “rename”; Terraform replaces.

---

## Good habit every time

```bash
terraform fmt
terraform validate
terraform plan
```

Then apply.

---

## Knowledge check

1. Changing a storage account **name** usually does what?
2. Is `-auto-approve` for beginners in production?

<details>
<summary>Answers</summary>

1. Destroy + create (new name).  
2. No. Class only, when the tutor says so.

</details>

➡️ Next: [Lab 05A](./Lab-05A-Fix.md)
