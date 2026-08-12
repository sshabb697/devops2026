# 04 — Shell Basics

Essential navigation and file commands. Practice every command in your terminal.

---

## Where am I?

```bash
pwd          # print working directory
whoami       # current user
hostname     # machine name
```

---

## List and inspect

```bash
ls              # list files
ls -l           # long format (permissions, size, date)
ls -la          # include hidden files (start with .)
ls -lt          # sort by time modified
ls -ltr         # oldest first
```

---

## Change directory

```bash
cd /home/you/projects    # absolute path (from /)
cd projects              # relative path (from current dir)
cd ..                    # up one level
cd ~                       # home directory
cd -                       # previous directory
```

### Absolute vs relative path

| Type | Starts with | Example |
| ---- | ----------- | ------- |
| Absolute | `/` | `/home/student/linux-course` |
| Relative | current dir | `day01/lab` |

---

## Create directories and files

```bash
mkdir asia
mkdir europe africa america
mkdir -p asia/india/mumbai    # parent folders created automatically

touch notes.txt               # empty file
echo "Hello Linux" > hello.txt
cat hello.txt
```

---

## Copy, move, delete

```bash
cp hello.txt backup/hello.txt
cp -r mydir mydir-copy          # recursive (directories)

mv oldname.txt newname.txt      # rename
mv file.txt ../                 # move

rm file.txt                     # delete file
rm -r mydir                     # delete directory (careful!)
```

---

## View file content

```bash
cat file.txt        # full file (small files)
less file.txt       # scrollable (q to quit)
head -n 5 file.txt  # first 5 lines
tail -n 20 file.txt # last 20 lines
tail -f /var/log/syslog   # follow log live (needs permission)
```

---

## Get help

```bash
man ls              # manual page
ls --help           # quick help
whatis ls
```

---

## Command history & shortcuts

| Shortcut | Action |
| -------- | ------ |
| `↑` / `↓` | Previous/next command |
| `Tab` | Auto-complete |
| `Ctrl + C` | Cancel running command |
| `Ctrl + L` | Clear screen |
| `history` | Show command history |

---

## Knowledge check

1. Difference between `cp` and `mv`?
2. What does `mkdir -p a/b/c` do?
3. How do you list hidden files?

➡️ Next: [05 — Filesystem Hierarchy](./05-Filesystem-Hierarchy.md)
