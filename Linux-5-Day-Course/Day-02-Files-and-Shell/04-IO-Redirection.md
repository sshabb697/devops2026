# 04 — I/O Redirection & Pipes

The power of Linux: **chain small tools**.

---

## Standard streams

| Stream | Number | Default |
| ------ | ------ | ------- |
| stdin | 0 | keyboard |
| stdout | 1 | terminal |
| stderr | 2 | terminal |

---

## Redirection

```bash
echo "hello" > file.txt       # stdout to file (overwrite)
echo "more" >> file.txt       # append
cmd 2> errors.log             # stderr to file
cmd > out.log 2>&1            # stdout + stderr to same file
cmd &> all.log                # shorthand (bash)
```

---

## Pipes

```bash
ls -la | less
cat access.log | grep "404" | wc -l
ps aux | grep nginx
df -h | grep ^/dev
```

Output of left command → input of right command.

---

## Here documents (useful in scripts)

```bash
cat <<EOF > config.txt
server_name localhost;
port 8080
EOF
```

---

## Real DevOps examples

```bash
# Count error lines in log
grep -c ERROR /var/log/app.log

# Top 10 IP addresses in access log
awk '{print $1}' access.log | sort | uniq -c | sort -rn | head

# Check if port listening
ss -tlnp | grep :80
```

➡️ Next: [Lab 02](./Lab-02-File-Operations.md)
