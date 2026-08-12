# 02 — Linux Architecture

**Learning objectives**

- Name the five layers from hardware to applications
- Explain what the **kernel** does vs what the **shell** does
- Recall the boot path at a high level (GRUB → kernel → systemd)

---

## The layers (visual)

![Linux architecture layers](../images/linux-architecture-layers.png)

---

## Layer by layer

### 1. Hardware
CPU, RAM, disk, network card — physical or virtual (VM/hypervisor).

### 2. Linux kernel
Core of the OS. Manages:
- **Processes** — who runs when
- **Memory** — RAM allocation
- **Filesystem** — read/write storage
- **Network** — packets in/out
- **Device drivers** — talk to hardware

You rarely talk to the kernel directly. Commands and libraries do that for you.

### 3. System libraries & utilities
Shared code (`glibc`) and commands like `ls`, `cp`, `systemctl`.

### 4. Shell
Your command interpreter — usually **Bash**. You type commands; the shell finds the program (`PATH`) and asks the kernel to run it.

### 5. User applications
Browsers, `docker`, `nginx`, VS Code, your scripts.

---

## Boot sequence (awareness)

```
Power on → Firmware (BIOS/UEFI) → Bootloader (GRUB)
         → Kernel loads → systemd (PID 1) → services → login prompt
```

When a server “won’t boot,” admins check GRUB, disk, and systemd. Day 4 covers services.

---

## Kernel vs shell vs application

| You type… | Handled by… |
| --------- | ----------- |
| `ls -la` | Shell runs `/usr/bin/ls` |
| `systemctl restart nginx` | Shell → systemd → nginx service |
| `docker run` | Shell → docker daemon → container |

---

## Knowledge check

1. What does the kernel manage?
2. What is PID 1 on modern Linux?
3. Where does Bash fit in the stack?

<details>
<summary>Answers</summary>

1. Processes, memory, filesystem, network, drivers.
2. `systemd` (the first user-space process).
3. Between utilities/libraries and your applications — it is the command interpreter.

</details>

➡️ Next: [03 — Setup WSL / VM](./03-Setup-WSL-VM.md)
