# Lab 01 — Shell Navigation

**Time:** 60 minutes  
**Goal:** Build a directory tree using only the shell.

Work in **Ubuntu** (WSL or VM), not PowerShell.

---

## Setup

```bash
cd ~
mkdir -p linux-course/lab01
cd linux-course/lab01
pwd
```

Expected: `/home/<you>/linux-course/lab01`

---

## Part A — Create the structure (20 min)

Create this tree:

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

**Try yourself first**, then compare:

```bash
mkdir -p continents/asia/india/mumbai
mkdir -p continents/europe
mkdir -p continents/africa/egypt/cairo
echo "Mumbai" > continents/asia/india/mumbai/city.txt
echo "Cairo" > continents/africa/egypt/cairo/city.txt
echo "Day 1 complete" > notes.txt
```

Verify:

```bash
find continents -type f
sudo apt install -y tree
tree continents
```

Expected `find` output includes:

```
continents/asia/india/mumbai/city.txt
continents/africa/egypt/cairo/city.txt
```

✅ **Checkpoint:** `find` or `tree` shows both city files.

---

## Part B — Navigation practice (15 min)

1. `cd continents/asia/india/mumbai` → `pwd` → `cat city.txt`  
   Expected: `Mumbai`
2. `cd ../../../../` → `pwd`  
   Expected: you are back in `lab01`
3. Absolute path: `cat ~/linux-course/lab01/notes.txt`  
   Expected: `Day 1 complete`
4. Relative path from `lab01`: `cat continents/africa/egypt/cairo/city.txt`  
   Expected: `Cairo`

---

## Part C — Copy, move, rename (15 min)

```bash
cp continents/asia/india/mumbai/city.txt continents/europe/city.txt
mv continents/europe/city.txt continents/europe/london-city.txt
echo "London" > continents/europe/london-city.txt
ls -la continents/europe/
cat continents/europe/london-city.txt
```

Expected: `london-city.txt` contains `London`. Original Mumbai file is unchanged:

```bash
cat continents/asia/india/mumbai/city.txt
```

---

## Part D — Explore system directories (10 min)

```bash
ls /etc | wc -l
ls /var/log | head
ls -ld /tmp /home /root
```

Write one sentence: what do you expect to find in `/etc` vs `/var/log`?

Suggested answer: `/etc` holds configuration; `/var/log` holds log files.

---

## If you get stuck

| Error | Likely cause |
| ----- | ------------ |
| `No such file or directory` | Wrong folder — `pwd` and `cd ~/linux-course/lab01` |
| `Permission denied` on `/root` | Normal for a regular user — use `ls -ld /root` |
| `tree: command not found` | `sudo apt install -y tree` or use `find` |

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
