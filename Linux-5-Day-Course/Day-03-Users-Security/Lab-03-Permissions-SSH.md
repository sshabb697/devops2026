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

chmod u+x deploy.sh
./deploy.sh                    # works

chmod 750 deploy.sh
ls -l deploy.sh

echo 'secret' > api.key
chmod 600 api.key
ls -l api.key
```

Fill in octal for each:
- Script runnable by you, readable by group: `___`
- Private key file: `___`

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

---

## Part C — SSH keys (20 min)

If you have a second VM or WSL only, simulate locally:

```bash
ssh-keygen -t ed25519 -f ~/.ssh/lab_key -N ""
chmod 600 ~/.ssh/lab_key
cat ~/.ssh/lab_key.pub
```

On a **remote VM** (Azure lab VM from AZ-104 course):

```bash
ssh-copy-id -i ~/.ssh/lab_key.pub azureuser@<VM_IP>
ssh -i ~/.ssh/lab_key azureuser@<VM_IP> 'hostname && whoami'
```

---

## Deliverables

- [ ] Used chmod symbolic and octal
- [ ] Created 600 and 750 files/dirs
- [ ] Generated SSH key pair
- [ ] (Optional) SSH login with key to a VM

➡️ **Day 4:** [Processes & Systemd](../Day-04-Processes-Packages-Systemd/README.md)
