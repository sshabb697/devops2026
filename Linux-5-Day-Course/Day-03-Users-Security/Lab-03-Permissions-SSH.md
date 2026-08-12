# Lab 03 — Permissions & SSH

**Time:** 60 minutes

---

## Part A — Permission practice (25 min)

```bash
mkdir -p ~/linux-course/lab03
cd ~/linux-course/lab03

echo '#!/bin/bash' > deploy.sh
echo 'echo Deploying...' >> deploy.sh
chmod 644 deploy.sh
./deploy.sh                    # should fail (no execute)
```

Expected: `Permission denied`.

```bash
chmod u+x deploy.sh
./deploy.sh                    # works
```

Expected: `Deploying...`

```bash
chmod 750 deploy.sh
ls -l deploy.sh

echo 'secret' > api.key
chmod 600 api.key
ls -l api.key
```

Expected:

- `deploy.sh` → `-rwxr-x---` (`750`)
- `api.key` → `-rw-------` (`600`)

Fill in octal for each:

- Script runnable by you, readable/executable by group, closed to others: **`750`**
- Private key file: **`600`**

---

## Part B — Shared directory (15 min)

```bash
mkdir shared
echo "team file" > shared/readme.txt
chmod 770 shared
chmod 660 shared/readme.txt
ls -ld shared
ls -l shared/
```

Expected: directory `rwxrwx---` and file `rw-rw----`.

---

## Part C — SSH keys (20 min)

Works on WSL even without a second VM:

```bash
mkdir -p ~/.ssh
chmod 700 ~/.ssh
ssh-keygen -t ed25519 -f ~/.ssh/lab_key -N ""
chmod 600 ~/.ssh/lab_key
ls -l ~/.ssh/lab_key ~/.ssh/lab_key.pub
cat ~/.ssh/lab_key.pub
```

Expected: private key `600`, public key starts with `ssh-ed25519`.

On a **remote VM** (optional):

```bash
ssh-copy-id -i ~/.ssh/lab_key.pub azureuser@<VM_IP>
ssh -i ~/.ssh/lab_key azureuser@<VM_IP> 'hostname && whoami'
```

---

## Deliverables

- [ ] Used chmod symbolic and octal
- [ ] Created 600 and 750 files
- [ ] Generated SSH key pair
- [ ] (Optional) SSH login with key to a VM

➡️ **Day 4:** [Processes & Systemd](../Day-04-Processes-Packages-Systemd/README.md)
