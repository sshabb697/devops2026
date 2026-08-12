# 01 — User Management

**Learning objectives**

- Identify where Linux stores users and groups
- Create a user and add them to a group
- Contrast `sudo` and `su`

---

## Who am I?

```bash
id
groups
whoami
```

`uid=1000` is a typical first human user. `uid=0` is **root**.

---

## Key files

| File | Purpose |
| ---- | ------- |
| `/etc/passwd` | User accounts (name, uid, home, shell) |
| `/etc/shadow` | Encrypted passwords (root only) |
| `/etc/group` | Groups |

`/etc/passwd` fields (colon-separated):

```
name:x:uid:gid:comment:home:shell
```

```bash
tail -5 /etc/passwd
grep sudo /etc/group
```

---

## Users & groups (admin commands)

```bash
# Create user (Ubuntu/Debian) — interactive, creates home
sudo adduser devuser

# Add to sudo group (can run admin commands)
sudo usermod -aG sudo devuser

# Create group and add user
sudo groupadd developers
sudo usermod -aG developers devuser

# Change password
sudo passwd devuser

# Delete user (and optionally home)
sudo deluser devuser
# sudo deluser --remove-home devuser
```

`-aG` **appends** groups. `usermod -G` without `-a` **replaces** all groups — easy to lock someone out of `sudo`.

---

## sudo

Run commands as root (with an audit trail in `/var/log/auth.log`):

```bash
sudo apt update
sudo systemctl restart nginx
sudo -i              # root shell (use carefully)
```

`/etc/sudoers` — who may sudo. Edit **only** with `sudo visudo` (syntax check). A broken sudoers file can lock you out of admin.

---

## su vs sudo

| Command | Meaning |
| ------- | ------- |
| `su - user` | Switch user (need **their** password) |
| `sudo cmd` | Run one command as root (**your** password, if allowed) |

Prefer `sudo` on Ubuntu. It is logged and you stay yourself.

---

## Knowledge check

1. Which file lists user accounts?
2. Why use `usermod -aG` instead of `usermod -G`?
3. How should you edit sudoers?

<details>
<summary>Answers</summary>

1. `/etc/passwd` (passwords are in `/etc/shadow`).
2. `-a` appends; without it you wipe existing groups.
3. `sudo visudo` only.

</details>

➡️ Next: [02 — File Permissions](./02-File-Permissions.md)
