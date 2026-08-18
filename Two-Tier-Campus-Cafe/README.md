# Campus Cafe — two-tier demo

A small **campus cafeteria** app for teaching a classic two-tier layout:

| Tier | Role | This project |
| ---- | ---- | ------------ |
| **1 · Web** | Apache + PHP | `web/` — HTML UI, reads/writes MySQL |
| **2 · Database** | MySQL / MariaDB | `db/init.sql` — menu + orders |

Inspired by the idea behind [KodeKloud learning-app-ecommerce](https://github.com/kodekloudhub/learning-app-ecommerce) (web + DB, env-based host), but this is a **new app** with its own schema and UI.

```
Browser  →  Web server (PHP)  →  Database (MySQL)
              index.php              menu_items
              health.php             orders
```

On one VM, `DB_HOST=localhost`. On two VMs, set `DB_HOST` to the database server’s IP.

## Quick start (Docker)

From this folder:

```bash
docker compose up --build
```

Open [http://localhost:8080](http://localhost:8080). Health: [http://localhost:8080/health.php](http://localhost:8080/health.php).

Stop with `docker compose down`. Add `-v` to drop the database volume.

## What students should notice

- The **menu is not hard-coded** in PHP; it comes from `SELECT` on `menu_items`.
- **Place an order** runs `INSERT INTO orders`.
- The green/red badge shows whether the web tier can reach the DB host.
- `/health.php` is useful later for load balancers and pipeline smoke tests.

Demo passwords (`cafeuser` / `cafepass`) are for the classroom only.

## Deploy on two Linux VMs (Ubuntu)

Use two machines: **web** and **db**. Open **3306/tcp** from web → db only, and **80/tcp** to the web VM.

### Database VM

```bash
sudo apt update
sudo apt install -y mysql-server
sudo systemctl enable --now mysql
```

Allow the web VM (replace `WEB_IP`):

```bash
sudo mysql <<'SQL'
CREATE DATABASE campuscafe;
CREATE USER 'cafeuser'@'WEB_IP' IDENTIFIED BY 'cafepass';
GRANT ALL PRIVILEGES ON campuscafe.* TO 'cafeuser'@'WEB_IP';
FLUSH PRIVILEGES;
SQL

sudo mysql campuscafe < /path/to/db/init.sql
```

If MySQL only listens on localhost, bind it to the private IP in `/etc/mysql/mysql.conf.d/mysqld.cnf` (`bind-address = 0.0.0.0` or the NIC IP) and restart `mysql`.

### Web VM

```bash
sudo apt update
sudo apt install -y apache2 php php-mysql git
sudo systemctl enable --now apache2
```

Copy `web/` into the document root (example):

```bash
sudo rm -rf /var/www/html/*
sudo cp -r web/. /var/www/html/
sudo tee /var/www/html/.env >/dev/null <<EOF
DB_HOST=DB_IP
DB_USER=cafeuser
DB_PASSWORD=cafepass
DB_NAME=campuscafe
EOF
```

Browse to `http://WEB_IP`. Change `DB_HOST` and reload to show students that the app talks to a **separate** database host.

### Single-node (web + DB on one VM)

Install Apache, PHP, and MySQL on the same machine. Create the user as `'cafeuser'@'localhost'`, load `init.sql`, and set `DB_HOST=localhost` in `/var/www/html/.env`.

## Project layout

```
Two-Tier-Campus-Cafe/
  docker-compose.yml   # web + db for a laptop demo
  db/init.sql          # schema and seed data
  web/
    index.php          # UI + menu/orders
    health.php         # JSON health for monitoring labs
    config.php         # env / .env loader
    db.php             # mysqli helper
    Dockerfile
    assets/style.css
```

## Troubleshooting

| Symptom | Check |
| ------- | ----- |
| Red “DB unreachable” badge | `DB_HOST`, firewall 3306, MySQL `bind-address`, user host (`'cafeuser'@'WEB_IP'`) |
| Empty menu | `init.sql` was not loaded; `GET /health.php` should show `menu_items` |
| Orders do not appear | Form POST failed validation, or DB user lacks INSERT |
