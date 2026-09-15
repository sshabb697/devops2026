# 02 — State (Terraform’s memory)

**Learning objectives**

- **State** remembers IDs of what was created
- Never edit `terraform.tfstate` in Notepad
- Do not commit state to Git (it can contain secrets)
- Local vs **remote** state (team)

---

## One-sentence idea

The `.tf` files are the **wish**. The **state file** is Terraform’s notebook about Azure.

![State](../images/tf-state.png)

---

## Everyday analogy: a locker list

The school keeps a list: locker 12 belongs to Ana.  
If you throw the list away, the school forgets who has which locker — but the lockers still exist.

If you delete state but keep Azure resources, Terraform will try to **create again** and may fail (“already exists”).

---

## Local vs remote (preview of Day 4)

| Local `terraform.tfstate` | Remote (Azure Blob) |
| ------------------------- | ------------------- |
| Fine for **one** student | Fine for a **team** |
| Easy to lose the file | Shared + backup |
| No lock between two laptops | **Lock** so two applies do not run together |

**Locking** = “bathroom occupied” sign. Wait. Do not force-unlock unless the tutor says the apply is dead.

---

## Knowledge check

1. Is state the same as Azure?
2. Why is remote state better for a team?

<details>
<summary>Answers</summary>

1. No — it is Terraform’s notebook **about** Azure.  
2. One shared notebook, not two copies on two laptops.

</details>

➡️ Next: [Lab 02B](./Lab-02B-State.md)
