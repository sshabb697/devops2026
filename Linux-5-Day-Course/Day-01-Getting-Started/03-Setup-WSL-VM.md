# 03 — Setup Linux Lab (WSL / VM)

You need a Linux terminal for all labs. Pick **one** option below.

**Checkpoint at the end:** `uname -a` shows Linux, `sudo` works, and `~/linux-course` exists.

---

## Option A — WSL2 on Windows (recommended)

### Install

```powershell
# Run PowerShell as Administrator
wsl --install -d Ubuntu-22.04
```

Restart if prompted. Create a Linux username/password when Ubuntu starts.

Open Ubuntu from the Start menu (or `wsl` in PowerShell). This is a **Linux** shell — not PowerShell.

### Verify

```bash
uname -a
lsb_release -a
whoami
pwd
```

Expected: `Linux` in `uname`, Ubuntu in `lsb_release`, `pwd` is `/home/<you>`.

### Update packages

```bash
sudo apt update && sudo apt upgrade -y
```

`sudo` asks for **your** Linux password (not Windows).

### Common WSL issues

| Problem | Fix |
| ------- | --- |
| `wsl` not found | Enable Virtual Machine Platform + WSL in Windows Features, reboot |
| Ubuntu stuck at install | `wsl --update` then retry |
| Commands look like PowerShell | You are not inside Ubuntu — open the Ubuntu app |

---

## Option B — Virtual Machine (VirtualBox / Hyper-V)

1. Download Ubuntu 22.04 Server ISO from ubuntu.com/download/server.
2. Create VM: 2 GB RAM, 20 GB disk, network NAT or bridged.
3. Install Ubuntu; enable OpenSSH server when asked.
4. Login and run `sudo apt update`.

---

## Option C — macOS

```bash
brew install multipass
multipass launch 22.04 --name linux-lab --disk 10G --memory 2G
multipass shell linux-lab
```

---

## Lab workspace

Create a folder for all course work:

```bash
mkdir -p ~/linux-course/day01
cd ~/linux-course/day01
echo "Linux lab ready" > readme.txt
cat readme.txt
```

You should see: `Linux lab ready`

✅ **Checkpoint:** You are in Ubuntu, can run `sudo`, and have `~/linux-course/`.

➡️ Next: [04 — Shell Basics](./04-Shell-Basics.md)
