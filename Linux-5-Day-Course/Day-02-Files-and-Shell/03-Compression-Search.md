# 03 — Compression & Search

---

## Archive & compress

```bash
# tar = archive (combine files)
tar -cvf backup.tar myfolder/
tar -xvf backup.tar

# gzip compression
tar -czvf backup.tar.gz myfolder/
tar -xzvf backup.tar.gz

# zip (if installed)
zip -r backup.zip myfolder/
unzip backup.zip
```

| Flag | Meaning |
| ---- | ------- |
| `c` | create |
| `x` | extract |
| `z` | gzip |
| `v` | verbose |
| `f` | filename |

---

## Search inside files

```bash
grep "error" app.log
grep -i "failed" /var/log/syslog    # case insensitive
grep -r "password" /etc/nginx/        # recursive
grep -n "listen" nginx.conf           # show line numbers
```

---

## Find + grep combo

```bash
find /var/log -name "*.log" -exec grep -l "error" {} \;
```

---

## Sort & unique

```bash
sort names.txt
sort -n numbers.txt       # numeric
uniq sorted.txt           # remove adjacent duplicates
sort names.txt | uniq -c  # count occurrences
```

➡️ Next: [04 — I/O Redirection](./04-IO-Redirection.md)
