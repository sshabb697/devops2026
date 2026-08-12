# Lab 02 — File Operations

**Time:** 60 minutes

Use the Day 2 pictures while you work: [vi modes](../images/linux-vi-modes.png) · [grep](../images/linux-grep-filter.png) · [tar.gz](../images/linux-tar-archive.png) · [pipes](../images/linux-pipes-redirection.png)

---

## Part A — Vi edit (15 min)

1. `mkdir -p ~/linux-course && vi ~/linux-course/app.conf`
2. Press `i` and add:

   ```
   APP_NAME=Contoso
   PORT=8080
   LOG_LEVEL=info
   ```

3. `Esc`, then `:wq`
4. Display with `cat ~/linux-course/app.conf`

If you get stuck: `Esc` then `:q!` and start again.

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

Expected: two ERROR lines; count is `2`.

Also try:

```bash
grep -v INFO app.log
grep -n WARN app.log
```

---

## Part C — Archive (15 min)

```bash
cd ~/linux-course/lab02
tar -czvf logs-backup.tar.gz logs/
ls -lh logs-backup.tar.gz
mkdir -p restore && cd restore
tar -xzvf ../logs-backup.tar.gz
ls logs/
cat logs/app.log
```

Expected: `restore/logs/app.log` matches the original.

---

## Part D — Pipeline (15 min)

```bash
cd ~/linux-course/lab02/logs
grep -v INFO app.log > errors-only.log
cat errors-only.log
sort app.log | uniq
```

Expected `errors-only.log`: ERROR and WARN lines only (no INFO).

Bonus:

```bash
awk '{print $2}' app.log | sort | uniq -c
```

Expected: counts of INFO / ERROR / WARN.

---

## Deliverables

- [ ] Edited file with vi (`:wq`)
- [ ] Used grep and pipe; ERROR count is 2
- [ ] Created and extracted `.tar.gz`

➡️ **Day 3:** [Users & Security](../Day-03-Users-Security/README.md)
