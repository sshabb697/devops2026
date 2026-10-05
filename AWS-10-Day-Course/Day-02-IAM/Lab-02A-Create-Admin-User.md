# Lab 02A — Create an admin user + group

**Time:** 15 minutes
**Why:** You should never do daily work as root. By the end you'll log in as your own IAM admin user.

---

## Part A — Secure root first (3 min)

1. Signed in as root, go to **IAM**.
2. If prompted, **Add MFA** for the root user (use an authenticator app). Highly recommended.

---

## Part B — Create a group with admin rights (5 min)

1. **IAM → User groups → Create group**.
2. Name: `admins`.
3. Attach policy: search and tick **AdministratorAccess**.
4. **Create group**.

---

## Part C — Create your user (7 min)

1. **IAM → Users → Create user**.
2. User name: `your-name-admin`.
3. Tick **Provide user access to the AWS Management Console** → *I want to create an IAM user*.
4. Set a password. Add the user to the **admins** group. Create.
5. **Copy the sign-in URL** (looks like `https://ACCOUNTID.signin.aws.amazon.com/console`).
6. **Sign out of root.** Sign in with the new user at that URL.

> From now on, **always log in as this IAM user**, not root.

---

## If you get stuck

| Problem | Fix |
| ------- | --- |
| Can't find AdministratorAccess | It's an AWS **managed** policy — search exactly that name. |
| Sign-in URL fails | Use the 12-digit account ID; check caps in the username. |

---

## Deliverables

- [ ] `admins` group with AdministratorAccess
- [ ] Your IAM admin user created and **logged in as them**
- [ ] (Recommended) MFA on root

➡️ Next: [02 — Least privilege and roles](./02-Least-Privilege-and-Roles.md)
