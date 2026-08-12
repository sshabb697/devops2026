# 01 — User Management

---

## Key files

| File | Purpose |
| ---- | ------- |
| `/etc/passwd` | User accounts (name, uid, home, shell) |
| `/etc/shadow` | Encrypted passwords (root only) |
| `/etc/group` | Groups |

```bash
cat /etc/passwd | tail -5
cat /etc/group | grep sudo
id
groups
```

---

## Users & groups (admin commands)

```bash
# Create user (Ubuntu/Debian)
sudo adduser devuser
sudo usermod -aG sudo devuser    # add to sudo group

# Create group
sudo groupadd developers

# Change password
sudo passwd devuser

# Delete user
sudo deluser devuser
```

---

## sudo

Run commands as root (with audit trail):

```bash
sudo apt update
sudo systemctl restart nginx
sudo -i              # root shell (use carefully)
```

`/etc/sudoers` — who may sudo (edit with `visudo` only).

---

## su vs sudo

| Command | Meaning |
| ------- | ------- |
| `su - user` | Switch user (need their password) |
| `sudo cmd` | Run one command as root (your password) |

➡️ Next: [02 — File Permissions](./02-File-Permissions.md)
