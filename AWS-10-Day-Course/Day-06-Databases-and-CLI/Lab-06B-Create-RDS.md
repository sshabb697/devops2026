# Lab 06B — Create and connect to RDS

**Time:** 15 minutes
RDS takes ~10 minutes to create — **start Part A first**, then read while it builds.

---

## Part A — Create the database (5 min to click, ~10 to build)

1. **RDS → Create database**.
2. **Standard create**, engine **MySQL**.
3. **Template: Free tier**.
4. Settings:
   - DB instance identifier: `class-db`
   - Master username: `admin`
   - Master password: choose one (write it down).
5. Instance class: `db.t3.micro`. Storage: 20 GB.
6. **Connectivity:**
   - VPC: your `class-vpc` (or default).
   - **Public access: Yes** (only for this quick class test).
   - Create a new security group `class-db-sg`.
7. Add tag **Project = aws-class**. **Create database.**

While it builds (~10 min), do Part B.

---

## Part B — Prepare to connect (4 min)

1. Note the **endpoint** once available: `class-db.xxxx.REGION.rds.amazonaws.com`.
2. Edit the `class-db-sg` security group → **Inbound** → allow **MySQL/Aurora (3306)** from **My IP**.
3. Install a MySQL client if needed:
   ```bash
   # Amazon Linux / RHEL
   sudo dnf install -y mariadb105
   # macOS
   brew install mysql-client
   ```

---

## Part C — Connect and run SQL (6 min)

```bash
mysql -h class-db.xxxx.REGION.rds.amazonaws.com -u admin -p
```
Then:
```sql
SELECT VERSION();
CREATE DATABASE cafe;
USE cafe;
CREATE TABLE menu (id INT, item VARCHAR(50), price DECIMAL(5,2));
INSERT INTO menu VALUES (1, 'Latte', 3.50);
SELECT * FROM menu;
```

You just used a fully managed database — no server to patch.

---

## End of day — delete the database 💸

```bash
aws rds delete-db-instance --db-instance-identifier class-db --skip-final-snapshot
```
Or console → **Modify/Delete** → uncheck "create final snapshot".

---

## If you get stuck

| Problem | Fix |
| ------- | --- |
| Connection times out | Security group must allow 3306 from **My IP**; public access = Yes. |
| Still "Creating" | Wait — RDS takes ~10 min. Teach the CLI meanwhile. |
| Access denied (SQL) | Wrong master username/password. |

---

## Deliverables

- [ ] `class-db` running (Free tier, tagged)
- [ ] Connected with the MySQL client and ran SQL
- [ ] **Deleted** the database at end of day

➡️ Next day: [Day 7 — Infrastructure as Code](../Day-07-Infrastructure-as-Code/)
