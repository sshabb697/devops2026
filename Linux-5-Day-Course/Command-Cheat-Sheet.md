# Linux Command Cheat Sheet

Keep this open while you work. Commands assume **Ubuntu / Debian** unless noted.

---

## Day 1 — Navigation

| Command | What it does |
| ------- | ------------ |
| `pwd` | Print current directory |
| `whoami` | Current user |
| `ls -la` | List all files (including hidden) |
| `cd /path` | Absolute path |
| `cd folder` | Relative path |
| `cd ..` | Up one level |
| `cd ~` or `cd` | Home directory |
| `mkdir -p a/b/c` | Create nested folders |
| `touch file` | Create empty file |
| `echo "text" > file` | Write (overwrite) |
| `cat file` | Print file |
| `cp -r src dest` | Copy (recursive for dirs) |
| `mv old new` | Move or rename |
| `rm file` | Delete file |
| `rm -r dir` | Delete directory |
| `man ls` / `ls --help` | Help |
| `echo $PATH` | Where the shell looks for commands |
| `which ls` | Full path of a command |

---

## Day 2 — Files, vi, search, pipes

| Command | What it does |
| ------- | ------------ |
| `find . -name "*.log"` | Find files by name |
| `ln -s target link` | Symbolic link |
| `du -sh *` | Size of items in this folder |
| `df -h` | Disk free space |
| `vi file` | Edit (`i` insert, `Esc`, `:wq` save+quit, `:q!` abort) |
| `tar -czvf a.tar.gz dir/` | Create gzip archive |
| `tar -xzvf a.tar.gz` | Extract gzip archive |
| `grep -n ERROR file` | Search text (show line numbers) |
| `grep -i word file` | Case-insensitive search |
| `cmd > out.txt` | Overwrite stdout |
| `cmd >> out.txt` | Append stdout |
| `cmd 2> err.txt` | Redirect errors |
| `cmd \| grep x` | Pipe stdout to next command |
| `wc -l file` | Count lines |

---

## Day 3 — Users, permissions, SSH, cron

| Command | What it does |
| ------- | ------------ |
| `id` / `groups` | Your UID and groups |
| `sudo adduser name` | Create user |
| `sudo usermod -aG sudo name` | Add to sudo group |
| `chmod 755 file` | rwxr-xr-x |
| `chmod 644 file` | rw-r--r-- |
| `chmod 600 file` | rw------- (secrets / keys) |
| `sudo chown user:group file` | Change owner |
| `ssh user@host` | Remote login |
| `ssh-keygen -t ed25519` | Create SSH key pair |
| `ssh-copy-id user@host` | Install public key |
| `scp file user@host:/path` | Copy over SSH |
| `crontab -e` | Edit scheduled jobs |
| `crontab -l` | List cron jobs |

**Octal reminder:** r=4, w=2, x=1. Example: `7 = rwx`, `6 = rw-`, `5 = r-x`, `4 = r--`.

---

## Day 4 — Processes, packages, systemd

| Command | What it does |
| ------- | ------------ |
| `ps aux` | All processes |
| `top` / `htop` | Live CPU/memory |
| `sleep 60 &` | Background job |
| `jobs` | List background jobs |
| `kill PID` | SIGTERM (graceful) |
| `kill -9 PID` | SIGKILL (force) |
| `free -h` | RAM and swap |
| `uptime` | Load averages |
| `sudo apt update` | Refresh package index |
| `sudo apt install pkg` | Install package |
| `systemctl status name` | Service status |
| `sudo systemctl start/stop/restart name` | Control service |
| `sudo systemctl enable --now name` | Start now + on boot |
| `journalctl -u name -n 50` | Service logs |

---

## Day 5 — Network & storage

| Command | What it does |
| ------- | ------------ |
| `ip a` | IP addresses |
| `ip route` | Routing table |
| `ping -c 4 8.8.8.8` | Test IP connectivity |
| `ping -c 4 google.com` | Test DNS + connectivity |
| `ss -tulpn` | Listening ports |
| `dig name +short` | DNS lookup |
| `curl -I http://localhost` | HTTP headers |
| `lsblk` | Disks and partitions |
| `df -hT` | Mounted filesystems |
| `sudo mount /dev/sdb1 /mnt` | Mount disk |
| `cat /etc/fstab` | Mounts at boot |

**Quick diagnosis:** ping IP works but name fails → DNS. Connection refused → service down. Timed out → firewall.

---

## Safety rules

- Prefer `rm file` over `rm -rf /` — never run recursive delete from `/`.
- Never share `id_ed25519` (private key). Public key (`.pub`) is OK to copy.
- Edit sudoers only with `sudo visudo`.
- On production: `kill` first, `kill -9` only if it will not stop.
