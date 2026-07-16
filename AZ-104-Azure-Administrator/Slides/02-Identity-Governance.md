---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section { font-size: 28px; }
  h1 { color: #0078d4; }
  h2 { color: #106ebe; }
  table { font-size: 22px; }
footer: Azure Cloud Essentials | 02 Identity & Access
---

# Module 02
## Identity & Access

Give people (and apps) the access they need — and nothing more

---

# Why this matters every week

Common tickets:

- “Add the new developer to the Dev project”
- “Vendor needs temporary read access”
- “Who deleted that resource?”
- “Please don’t give everyone Owner on the subscription”

Access design is **security + speed**. Bad access slows teams *and* causes incidents.

---

# Microsoft Entra ID (directory)

Central place for:

- Users and groups
- Guest (external) users
- App registrations / service principals (automation)

```
  People & apps  →  Entra ID  →  Azure resources (via RBAC)
```

Still different from classic on‑prem Active Directory — but they often work together.

---

# Groups first (habit)

| Do this | Avoid this |
|---------|------------|
| Create group `grp-app-dev` | Assigning roles to 20 individuals |
| Put users in the group | Forgetting to remove leavers |
| Assign RBAC to the group | Mystery direct assignments |

When someone joins/leaves → change **group membership**, not 15 role assignments.

---

# Azure RBAC in plain language

**Who** + **what they can do** + **where**

```
  User / Group / App     Role (Owner, Reader…)     Scope (sub / RG / resource)
           \                    |                         /
            \___________________|________________________/
                     Role assignment
```

Access inherits downward (subscription → RG → resource).

---

# Roles you’ll use constantly

| Role | Daily meaning |
|------|----------------|
| **Reader** | Look, don’t touch |
| **Contributor** | Create/change resources; **cannot** grant access |
| **Owner** | Everything + can grant access — use sparingly |
| **User Access Administrator** | Manage access only |
| Job roles (e.g. VM Contributor) | Narrower than Contributor |

**Golden rule:** prefer Contributor on **one RG**, not Owner on the whole subscription.

---

# Scope examples (real life)

| Request | Sensible assignment |
|---------|---------------------|
| Dev team builds Contoso Web (Dev) | Contributor on `rg-contoso-web-dev` |
| Auditor needs visibility | Reader on subscription or MG |
| Pipeline deploys to App Service | Service principal + limited role on that app/RG |
| Help desk resets nothing in Azure | Don’t grant Azure roles at all |

---

# Guests & temporary access

- Invite external users as **Guests** (B2B)
- Put them in a group with a **time-boxed** need
- Prefer Reader / data-plane roles over Owner
- Remove guests when the project ends

Self-service password reset (SSPR) reduces help-desk load for your own users.

---

# Azure Policy — guardrails, not people

| RBAC | Policy |
|------|--------|
| *Who* is allowed to act | *What* configuration is allowed |
| “Alex can create resources here” | “Everything must have tag Env” |
| | “No public storage accounts in Prod” |

Use Policy so mistakes are blocked **even for Contributors**.

---

# Locks + Policy + RBAC together

```
  RBAC     → right people
  Policy   → right configurations
  Locks    → hard stop on delete/change for critical resources
  Tags     → find & cost-allocate
```

That’s everyday governance — not bureaucracy for its own sake.

---

# Demo (15 min)

1. Create / pick a user or guest  
2. Create group `grp-lab-contributors`  
3. Assign **Reader** on `rg-lab-demo` → show they cannot create  
4. Switch to **Contributor** → create a cheap resource  
5. Assign Policy: require tag `Env`  
6. Try creating without tag → discuss the result  

---

# Scenarios — what would you do?

1. Intern needs to *see* Prod metrics but not change anything  
2. Vendor uploads files to one storage account for 3 days  
3. Someone asks for Owner “because Contributor couldn’t assign access to a teammate”

---

# Summary

- Use **groups** + **least privilege** + **smallest scope**
- Contributor ≠ can manage access
- Policy catches bad configurations; RBAC manages people
- Review access when people join, leave, or change projects

---

# Next

➡️ **Module 03 — Storage**

Where files live, how to share them safely, how to not leak keys
