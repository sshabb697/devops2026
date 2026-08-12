# 03 — Disk & Storage

---

## Block devices & partitions

```bash
lsblk
sudo fdisk -l                     # partition table
ls -l /dev/sd*
```

Typical naming: `/dev/sda1` (first disk, first partition), `/dev/nvme0n1p1` (NVMe).

---

## Filesystems & mount

```bash
df -hT
mount | column -t
cat /etc/fstab                    # mounts at boot
```

Mount temporarily:

```bash
sudo mkdir /mnt/data
sudo mount /dev/sdb1 /mnt/data
sudo umount /mnt/data
```

---

## LVM (awareness)

**Logical Volume Manager** — flexible disk pooling on servers.

```bash
sudo pvs                          # physical volumes
sudo vgs                          # volume groups
sudo lvs                          # logical volumes
```

Flow: **disk → PV → VG → LV → filesystem → mount**

Common on Azure/RHEL VMs when expanding OS disk.

---

## DAS / NAS / SAN (concept)

| Type | Description |
| ---- | ----------- |
| DAS | Disk attached directly to one server |
| NAS | File share over network (NFS, SMB) |
| SAN | Block storage over network (iSCSI, FC) |

Cloud: Azure Managed Disks ≈ block storage attached to VM.

---

## Disk full emergency

```bash
df -h
sudo du -xh / | sort -h | tail -20
sudo journalctl --disk-usage
sudo journalctl --vacuum-size=500M
sudo apt clean                    # clear apt cache
```

➡️ Next: [Lab 05 — Capstone](./Lab-05-Capstone.md)
