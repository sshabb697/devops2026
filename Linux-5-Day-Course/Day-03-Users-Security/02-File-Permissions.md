# 02 — File Permissions

![Linux file permissions rwx](../images/linux-file-permissions-rwx.png)

---

## Read `ls -l`

```bash
-rwxr-xr-- 1 alice developers 4096 Jan 10 09:00 deploy.sh
│└┬┘└┬┘└┬┘
│ │  │  └── others: r--
│ │  └───── group:  r-x
│ └──────── user:   rwx
└────────── type:   - (file)
```

| Permission | Letter | Octal |
| ---------- | ------ | ----- |
| Read | r | 4 |
| Write | w | 2 |
| Execute | x | 1 |

---

## chmod — symbolic

```bash
chmod u+x script.sh           # user + execute
chmod g-w file.txt            # group - write
chmod o=r file.txt            # others = read only
chmod u=rwx,g=rx,o= script.sh
```

---

## chmod — numeric (octal)

```bash
chmod 755 script.sh    # rwxr-xr-x  (common for scripts)
chmod 644 file.txt     # rw-r--r--  (common for configs)
chmod 600 secret.key   # rw-------  (SSH private keys)
chmod 700 ~/.ssh       # rwx------  (SSH directory)
```

| Mode | Octal | Use |
| ---- | ----- | --- |
| rwxr-xr-x | 755 | executables, dirs |
| rw-r--r-- | 644 | normal files |
| rw-r----- | 640 | group-readable configs |
| rwx------ | 700 | private dir |

---

## chown & chgrp

```bash
sudo chown bob:developers app.conf
sudo chown bob app.conf
sudo chgrp www-data /var/www/html -R
```

---

## umask (default permissions)

```bash
umask
umask 022    # typical: files 644, dirs 755
```

---

## Special bits (awareness)

| Bit | Effect |
| --- | ------ |
| setuid | Run as file owner (`/usr/bin/passwd`) |
| setgid | Run as group; dirs inherit group |
| sticky | Only owner deletes files in dir (`/tmp`) |

```bash
ls -ld /tmp    # often drwxrwxrwt
```

➡️ Next: [03 — SSH & SCP](./03-SSH-SCP.md)
