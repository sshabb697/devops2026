# 03 — Disk & Storage

**Learning objectives**

- List disks and mounts (`lsblk`, `df`)
- Explain mount and `/etc/fstab`
- Describe LVM at a high level
- Free space in an emergency

---

## Block devices & partitions

```bash
lsblk
sudo fdisk -l                     # partition table
ls -l /dev/sd* /dev/nvme* 2>/dev/null
```

Typical naming: `/dev/sda1` (first disk, first partition), `/dev/nvme0n1p1` (NVMe).

---

## Filesystems & mount

```bash
df -hT
findmnt
cat /etc/fstab                    # mounts at boot
```

Mount temporarily:

```bash
sudo mkdir -p /mnt/data
sudo mount /dev/sdb1 /mnt/data
df -h /mnt/data
sudo umount /mnt/data
```

`/etc/fstab` example (do not copy blindly):

```
UUID=xxxx-xxxx  /mnt/data  ext4  defaults  0  2
```

Wrong fstab can prevent boot — take a snapshot before editing on a VM.

---

## LVM (awareness)

**Logical Volume Manager** — flexible disk pooling on servers.

```bash
sudo pvs                          # physical volumes
sudo vgs                          # volume groups
sudo lvs                          # logical volumes
```

Flow: **disk → PV → VG → LV → filesystem → mount**

Common on Azure/RHEL VMs when expanding the OS disk.

---

## DAS / NAS / SAN (concept)

| Type | Description |
| ---- | ----------- |
| DAS | Disk attached directly to one server |
| NAS | File share over network (NFS, SMB) |
| SAN | Block storage over network (iSCSI, FC) |

Cloud: Azure Managed Disks ≈ block storage attached to a VM.

---

## Disk full emergency

```bash
df -h
sudo du -xh /var | sort -h | tail -20
sudo journalctl --disk-usage
sudo journalctl --vacuum-size=500M
sudo apt clean                    # clear apt cache
```

Typical culprits: `/var/log`, Docker images, leftover `*.tar.gz` in `/tmp` or home.

---

## Knowledge check

1. Command to see disks and mount points in a tree?
2. What file controls mounts at boot?
3. First command when “disk full”?

<details>
<summary>Answers</summary>

1. `lsblk` (and `df -h` for usage).
2. `/etc/fstab`
3. `df -h`, then `du` to find large directories.

</details>

➡️ Next: [Lab 05 — Capstone](./Lab-05-Capstone.md)
