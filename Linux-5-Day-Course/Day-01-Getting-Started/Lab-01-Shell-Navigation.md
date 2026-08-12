# Lab 01 — Shell Navigation

**Time:** 60 minutes  
**Goal:** Build a directory tree using only the shell.

---

## Setup

```bash
cd ~
mkdir -p linux-course/lab01
cd linux-course/lab01
pwd
```

---

## Part A — Create the structure (20 min)

Create this tree (replace `student` with your username):

```
linux-course/lab01/
├── continents/
│   ├── asia/
│   │   └── india/
│   │       └── mumbai/
│   │           └── city.txt
│   ├── europe/
│   └── africa/
│       └── egypt/
│           └── cairo/
│               └── city.txt
└── notes.txt
```

**Commands (try yourself first, then check):**

```bash
mkdir -p continents/asia/india/mumbai
mkdir -p continents/europe
mkdir -p continents/africa/egypt/cairo
touch continents/asia/india/mumbai/city.txt
touch continents/africa/egypt/cairo/city.txt
echo "Mumbai" > continents/asia/india/mumbai/city.txt
echo "Cairo" > continents/africa/egypt/cairo/city.txt
echo "Day 1 complete" > notes.txt
```

Verify:

```bash
find continents -type f
tree continents   # install: sudo apt install tree
```

✅ **Checkpoint:** `find` or `tree` shows all files.

---

## Part B — Navigation practice (15 min)

1. `cd continents/asia/india/mumbai` → `pwd` → `cat city.txt`
2. `cd ../../../../` → confirm you are back at `lab01`
3. Use **absolute path**: `cat ~/linux-course/lab01/notes.txt`
4. Use **relative path** from `lab01`: `cat continents/africa/egypt/cairo/city.txt`

---

## Part C — Copy, move, rename (15 min)

```bash
# Rename a folder (fix typo exercise)
mkdir -p continents/asia/india/munbai
mv continents/asia/india/munbai continents/asia/india/mumbai-backup 2>/dev/null || true

# Copy city file
cp continents/asia/india/mumbai/city.txt continents/europe/city.txt

# Move a file
mv continents/europe/city.txt continents/europe/london-city.txt

# List with details
ls -la continents/europe/
```

---

## Part D — Explore system directories (10 min)

```bash
ls /etc | wc -l
ls /var/log | head
ls -ld /tmp /home /root
```

Write one sentence: what do you expect to find in `/etc` vs `/var/log`?

---

## Deliverables

- [ ] Directory tree created under `~/linux-course/lab01`
- [ ] Used absolute and relative paths
- [ ] Used `cp`, `mv`, `mkdir -p`, `cat`, `ls -la`
- [ ] Can explain `/etc` and `/var/log`

## Cleanup (optional)

```bash
rm -rf ~/linux-course/lab01
```

➡️ **Day 2:** [Files and Shell](../Day-02-Files-and-Shell/README.md)
