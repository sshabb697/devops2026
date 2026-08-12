# 03 — Package Management

---

## Two major families

| Family | Distros | Package | Manager |
| ------ | ------- | ------- | ------- |
| Debian | Ubuntu, Debian | `.deb` | **apt** / dpkg |
| Red Hat | RHEL, CentOS, Amazon Linux | `.rpm` | **yum** / **dnf** / rpm |

Most cloud VMs and WSL Ubuntu use **apt**.

---

## APT (Ubuntu / Debian)

```bash
sudo apt update                     # refresh package index
sudo apt upgrade                    # install updates
sudo apt install nginx curl tree    # install packages
sudo apt remove nginx               # remove (keep config)
sudo apt purge nginx                # remove + config
apt search nginx
apt show nginx
dpkg -l | grep nginx                # list installed .deb packages
```

---

## YUM / DNF (RHEL family)

```bash
sudo yum update
sudo yum install nginx
sudo yum remove nginx
sudo dnf install nginx              # newer RHEL/Fedora
rpm -qa | grep nginx
```

---

## Low-level tools

```bash
# Debian
sudo dpkg -i package.deb
sudo apt install -f                 # fix broken deps

# Red Hat
sudo rpm -ivh package.rpm
sudo yum localinstall package.rpm
```

---

## Repositories

Packages come from **repos** configured in:

- Ubuntu: `/etc/apt/sources.list`, `/etc/apt/sources.list.d/`
- RHEL: `/etc/yum.repos.d/`

DevOps: pin versions in Docker images and IaC; avoid manual drift on prod servers.

---

## Practice

```bash
sudo apt update
sudo apt install -y tree htop
tree --version
htop --version
```

➡️ Next: [04 — Systemd Services](./04-Systemd-Services.md)
