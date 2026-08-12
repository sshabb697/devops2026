# 03 — Package Management

**Learning objectives**

- Contrast `apt` (Debian) and `dnf`/`yum` (RHEL)
- Update the index, then install a package
- Explain `remove` vs `purge`

---

## Two major families

| Family | Distros | Package | Manager |
| ------ | ------- | ------- | ------- |
| Debian | Ubuntu, Debian | `.deb` | **apt** / dpkg |
| Red Hat | RHEL, Rocky, Amazon Linux | `.rpm` | **yum** / **dnf** / rpm |

Most cloud VMs and WSL Ubuntu use **apt**.

---

## APT (Ubuntu / Debian)

```bash
sudo apt update                     # refresh package index (metadata)
sudo apt upgrade                    # install newer versions of installed pkgs
sudo apt install nginx curl tree    # install packages
sudo apt remove nginx               # remove (keep config in /etc)
sudo apt purge nginx                # remove + config
apt search nginx
apt show nginx
dpkg -l | grep nginx                # list installed .deb packages
```

**Always `apt update` before `apt install`** on a new VM — otherwise you may get “package not found” or old versions.

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

Prefer `apt`/`dnf` over raw `dpkg`/`rpm` so **dependencies** install too.

---

## Repositories

Packages come from **repos** configured in:

- Ubuntu: `/etc/apt/sources.list`, `/etc/apt/sources.list.d/`
- RHEL: `/etc/yum.repos.d/`

DevOps: pin versions in Docker images and IaC; avoid one-off `apt install` drift on prod servers.

---

## Practice

```bash
sudo apt update
sudo apt install -y tree htop
tree --version
htop --version
```

---

## Knowledge check

1. Difference between `apt update` and `apt upgrade`?
2. `remove` vs `purge`?
3. Why not install with `dpkg -i` only?

<details>
<summary>Answers</summary>

1. `update` refreshes the package list; `upgrade` installs newer packages.
2. `remove` keeps config files; `purge` deletes them too.
3. `dpkg` does not resolve dependencies — `apt` does.

</details>

➡️ Next: [04 — Systemd Services](./04-Systemd-Services.md)
