# 03 — Setup Linux Lab (WSL / VM)

You need a Linux terminal for all labs. Pick **one** option below.

---

## Option A — WSL2 on Windows (recommended)

### Install

```powershell
# Run PowerShell as Administrator
wsl --install -d Ubuntu-22.04
```

Restart if prompted. Create a Linux username/password when Ubuntu starts.

### Verify

```bash
uname -a
lsb_release -a
whoami
pwd
```

### Update packages

```bash
sudo apt update && sudo apt upgrade -y
```

---

## Option B — Virtual Machine (VirtualBox / Hyper-V)

1. Download [Ubuntu 22.04 Server ISO](https://ubuntu.com/download/server).
2. Create VM: 2 GB RAM, 20 GB disk, network NAT or bridged.
3. Install Ubuntu; enable OpenSSH server when asked.
4. Login and run `sudo apt update`.

---

## Option C — macOS

```bash
# Homebrew + multipass or UTM, or cloud VM
# Simplest: install Ubuntu in Multipass
brew install multipass
multipass launch --name linux-lab --disk 10G --mem 2G
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

✅ **Checkpoint:** You are in Ubuntu, can run `sudo`, and have `~/linux-course/`.

➡️ Next: [04 — Shell Basics](./04-Shell-Basics.md)
