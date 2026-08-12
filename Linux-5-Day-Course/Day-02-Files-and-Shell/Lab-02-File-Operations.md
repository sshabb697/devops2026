# Lab 02 — File Operations

**Time:** 60 minutes

---

## Part A — Vi edit (15 min)

1. `vi ~/linux-course/app.conf`
2. Add:
   ```
   APP_NAME=Contoso
   PORT=8080
   LOG_LEVEL=info
   ```
3. Save and quit. Display with `cat`.

---

## Part B — Search & filter (15 min)

```bash
mkdir -p ~/linux-course/lab02/logs
cd ~/linux-course/lab02/logs

cat <<EOF > app.log
2026-01-01 INFO Server started
2026-01-01 ERROR Connection refused
2026-01-01 INFO Request OK
2026-01-01 ERROR Timeout
2026-01-01 WARN Retrying
EOF

grep ERROR app.log
grep -c ERROR app.log
grep ERROR app.log | wc -l
```

---

## Part C — Archive (15 min)

```bash
cd ~/linux-course/lab02
tar -czvf logs-backup.tar.gz logs/
ls -lh logs-backup.tar.gz
mkdir restore && cd restore
tar -xzvf ../logs-backup.tar.gz
ls logs/
```

---

## Part D — Pipeline (15 min)

```bash
cd ~/linux-course/lab02/logs
cat app.log | grep -v INFO > errors-only.log
cat errors-only.log
sort app.log | uniq
```

---

## Deliverables

- [ ] Edited file with vi
- [ ] Used grep and pipe
- [ ] Created and extracted `.tar.gz`

➡️ **Day 3:** [Users & Security](../Day-03-Users-Security/README.md)
