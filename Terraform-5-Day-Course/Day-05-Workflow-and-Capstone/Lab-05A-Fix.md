# Lab 05A — Break and fix

**Time:** 40 minutes  
Folder: `Day-05-Workflow-and-Capstone/lab-broken/`

This folder has a **mistake** on purpose.

---

## Part A — See the error (15 min)

```bash
cd lab-broken
terraform init
terraform validate
```

Read the error. Fix `main.tf` (the location line is wrong — it uses a fake attribute).

```bash
terraform validate
```

Must print **Success**.

---

## Part B — Plan only (15 min)

```bash
terraform plan
```

You do **not** have to apply this tiny broken-folder lab. The point is validate + read.

---

## Deliverables

- [ ] `validate` succeeds after your fix

➡️ Next: [02 — Destroy](./02-Destroy.md)
