# 01 — File Management (Advanced)

Beyond Day 1 basics — links, wildcards, and finding files.

---

## Wildcards (globs)

```bash
ls *.txt              # all .txt in current dir
ls lab*               # starts with lab
ls file?.txt          # file1.txt, fileA.txt (? = one char)
ls [abc]*             # starts with a, b, or c
```

---

## Find files

```bash
find . -name "*.log"
find /var/log -type f -mtime -1    # modified last 24h
find . -type d -name "config"
find . -size +10M                  # larger than 10MB
```

---

## Links

```bash
# Hard link (same inode, same file data)
ln original.txt hardlink.txt

# Symbolic link (shortcut to path)
ln -s /etc/nginx/nginx.conf ~/nginx.conf
ls -l
```

| Type | If original deleted |
| ---- | ------------------- |
| Hard link | Data remains until all links removed |
| Symbolic | Broken link |

---

## Disk usage

```bash
du -sh *                # size of each item in dir
du -sh /var/log
df -h                   # filesystem free space
```

---

## File types (Linux)

First character in `ls -l`:
- `-` regular file
- `d` directory
- `l` symlink

➡️ Next: [02 — Vi Editor](./02-Vi-Editor.md)
