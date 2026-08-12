# 02 — Vi / Vim Editor

On servers there is often **no GUI** — you edit configs with **vi** or **vim**.

---

## Open and modes

```bash
vi myconfig.conf
vim myconfig.conf    # improved vi (usually installed)
```

| Mode | Purpose | How to enter |
| ---- | ------- | ------------ |
| **Normal** | Navigate, delete, copy | Default; press `Esc` |
| **Insert** | Type text | `i`, `a`, `o` |
| **Command** | Save, quit, search | `:` in Normal mode |

---

## Essential shortcuts (memorize these)

| Key | Action |
| --- | ------ |
| `i` | Insert before cursor |
| `Esc` | Back to Normal mode |
| `:w` | Save |
| `:q` | Quit |
| `:wq` or `ZZ` | Save and quit |
| `:q!` | Quit without saving |
| `dd` | Delete line |
| `yy` | Copy (yank) line |
| `p` | Paste |
| `/word` | Search forward |
| `n` | Next search match |
| `u` | Undo |
| `G` | Go to end of file |
| `gg` | Go to start |

---

## Mini exercise

```bash
cd ~/linux-course
vi practice.txt
# Press i, type a few lines, Esc, :wq
cat practice.txt
vi practice.txt   # edit again
```

---

## Why vi matters for DevOps

- Available on **every** Linux server
- Fast edits to `/etc/nginx/nginx.conf`, YAML, scripts
- Default `EDITOR` on many systems

➡️ Next: [03 — Compression & Search](./03-Compression-Search.md)
