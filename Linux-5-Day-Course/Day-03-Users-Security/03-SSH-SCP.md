# 03 — SSH & SCP

Remote access is how you manage **every Linux server** in the cloud.

---

## Connect with password

```bash
ssh user@192.168.1.50
ssh user@myserver.example.com
ssh -p 2222 user@host    # custom port
exit
```

---

## SSH key pair (recommended)

On your **local** machine (WSL/laptop):

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
# saves to ~/.ssh/id_ed25519 and id_ed25519.pub

cat ~/.ssh/id_ed25519.pub
```

Copy public key to server:

```bash
ssh-copy-id user@server
# or manually append pub key to ~/.ssh/authorized_keys on server
```

Permissions matter:

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
chmod 600 ~/.ssh/id_ed25519
```

---

## SCP — copy files over SSH

```bash
scp localfile.txt user@server:/home/user/
scp user@server:/var/log/app.log ./logs/
scp -r myfolder/ user@server:/opt/
```

---

## SSH config shortcut

`~/.ssh/config`:

```
Host myvm
  HostName 20.10.5.4
  User azureuser
  IdentityFile ~/.ssh/id_ed25519
```

Then: `ssh myvm`

---

## DevOps usage

- Azure VM, AWS EC2, GitHub Actions self-hosted runners
- Ansible, rsync, SFTP all build on SSH
- **Never** share private keys; use keys per machine or CI secret

➡️ Next: [04 — Cron Jobs](./04-Cron-Jobs.md)
