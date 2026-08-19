# 03 — Install and verify

Pick **one** path. You only need a working `docker` command.

---

## Option A — Windows (recommended for this class)

1. Install **Docker Desktop** from docker.com.
2. Enable **WSL2** backend (Settings → General).
3. Open Ubuntu WSL **or** PowerShell and run:

```bash
docker version
docker info
docker run --rm hello-world
```

Expected: a “Hello from Docker!” message. That proves pull + run works.

---

## Option B — macOS

Install Docker Desktop for Mac, start it, then the same three commands.

---

## Option C — Linux VM

Follow Docker’s official Engine install for Ubuntu, then add your user to the `docker` group and **log out and back in**.

```bash
docker run --rm hello-world
```

---

## Common install problems

| Problem | Fix |
| ------- | --- |
| `docker: command not found` | Desktop not installed, or terminal opened before install |
| `Cannot connect to the Docker daemon` | Start Docker Desktop and wait until it says running |
| WSL: engine not found | Enable WSL integration in Desktop → Resources → WSL |
| Permission denied on Linux | User not in `docker` group, or use `sudo docker` for class |

---

## Lab workspace

```bash
mkdir -p ~/docker-course/day01
cd ~/docker-course/day01
docker version > docker-version.txt
```

✅ Checkpoint: `hello-world` ran once.

➡️ Next: [04 — Images and run](./04-Images-and-Run.md)
