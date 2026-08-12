# 03 — Compression & Search

**Learning objectives**

- Create and extract `.tar.gz` archives
- Search file contents with `grep`
- Count and sort unique lines

---

## Archive & compress

```bash
# tar = archive (combine files)
tar -cvf backup.tar myfolder/
tar -xvf backup.tar

# gzip compression (most common in DevOps)
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
| `f` | filename (must be last flag before the file name) |

List without extracting:

```bash
tar -tzvf backup.tar.gz
```

---

## Search inside files

```bash
grep "error" app.log
grep -i "failed" /var/log/syslog    # case insensitive
grep -r "password" /etc/nginx/        # recursive
grep -n "listen" nginx.conf           # show line numbers
grep -v INFO app.log                  # invert: lines that do NOT match
grep -c ERROR app.log                 # count matches
```

---

## Find + grep combo

```bash
grep -R "TODO" --include="*.sh" .
find /var/log -name "*.log" -exec grep -l "error" {} \;
```

---

## Sort & unique

```bash
sort names.txt
sort -n numbers.txt       # numeric
uniq sorted.txt           # remove adjacent duplicates (sort first!)
sort names.txt | uniq -c  # count occurrences
```

---

## Knowledge check

1. Which flags create a gzip tar named `logs.tar.gz` from folder `logs/`?
2. How do you show line numbers with grep?
3. Why does `uniq` often follow `sort`?

<details>
<summary>Answers</summary>

1. `tar -czvf logs.tar.gz logs/`
2. `grep -n`
3. `uniq` only collapses **adjacent** duplicates, so sort first.

</details>

➡️ Next: [04 — I/O Redirection](./04-IO-Redirection.md)
