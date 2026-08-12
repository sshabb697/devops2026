# 02 — Vi / Vim Editor

On servers there is often **no GUI** — you edit configs with **vi** or **vim**.

**Learning objectives**

- Switch between Normal, Insert, and Command mode
- Save, quit, undo, search, delete a line

If vi feels hostile: `nano file.txt` also works. Still learn vi — it is on **every** server.

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

**Golden rule:** if keys do weird things, press **Esc** until you are in Normal mode.

```
  Esc
  ┌──────────┐     i / a / o      ┌──────────┐
  │  NORMAL  │ ───────────────►   │  INSERT  │
  │  (Esc)   │ ◄───────────────   │  (type)  │
  └────┬─────┘                    └──────────┘
       │ :
       ▼
  ┌──────────┐
  │ COMMAND  │  :w  :q  :wq  :q!
  └──────────┘
```

---

## Essential shortcuts (memorize these)

| Key | Action |
| --- | ------ |
| `i` | Insert before cursor |
| `a` | Insert after cursor |
| `o` | New line below |
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
| `:set number` | Show line numbers |

---

## Mini exercise

```bash
cd ~/linux-course
vi practice.txt
```

1. Press `i`
2. Type three lines of text
3. `Esc`
4. `:wq`
5. `cat practice.txt`
6. Open again, search with `/`, undo with `u`, quit with `:q!` if you want to discard

**Stuck in vi?** `Esc`, then `:q!` — leaves without saving.

---

## Why vi matters for DevOps

- Available on **every** Linux server
- Fast edits to `/etc/nginx/nginx.conf`, YAML, scripts
- Default `EDITOR` on many systems (`crontab -e` often opens vi)

---

## Knowledge check

1. How do you save and quit?
2. How do you quit **without** saving?
3. You are typing and letters disappear / commands run — what do you press?

<details>
<summary>Answers</summary>

1. `Esc` then `:wq`
2. `Esc` then `:q!`
3. `Esc` — you were not in Insert mode.

</details>

➡️ Next: [03 — Compression & Search](./03-Compression-Search.md)
