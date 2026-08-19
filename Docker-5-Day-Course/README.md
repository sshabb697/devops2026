# Docker 5-Day Course

Hands-on Docker for **new DevOps students**. You will run, build, and ship containers the way teams do on real projects.

> Focus: **commands and mental models you need in class and on the job** — not every Docker feature.

Print or keep open: **[Command Cheat Sheet](./Command-Cheat-Sheet.md)**

---

## What you will be able to do

By the end of the week you can:

1. Explain container vs VM and run nginx in a container.
2. Write a Dockerfile, build an image, and run it with a mapped port.
3. Use volumes and networks so data and services survive restarts.
4. Start a multi-container app with Compose and push an image to a registry.
5. Troubleshoot a broken container and apply basic image hygiene.

| Day | Topic | Outcome |
| --- | ----- | ------- |
| [Day 1](./Day-01-Docker-Fundamentals/) | Concepts, install, first containers | Run and inspect containers |
| [Day 2](./Day-02-Images-and-Dockerfile/) | Images, Dockerfile, layers | Build your own image |
| [Day 3](./Day-03-Data-and-Networking/) | Lifecycle, ports, volumes, networks | Persist data and connect services |
| [Day 4](./Day-04-Compose-and-Registry/) | Compose, Hub, multi-stage builds | Ship a small app |
| [Day 5](./Day-05-Ops-Security-Capstone/) | Logs, security, troubleshooting | Fix a real stack |

---

## Prerequisites

- [Linux 5-Day Course](../Linux-5-Day-Course/) completed **or** comfort with `cd`, `ls`, `cat`, and a terminal
- Windows + **WSL2**, macOS, or Linux
- Install **Docker Desktop** (Windows/Mac) or Docker Engine (Linux)
- 8 GB RAM recommended
- Free [Docker Hub](https://hub.docker.com/) account for Day 4 (optional but useful)

---

## How to study

1. Read the **lessons** (concepts + diagrams).
2. Run every **command** yourself.
3. Complete the **lab** at the end of each day.
4. Use the **cheat sheet** when you forget a flag.

Each day is **5–6 hours**.

**If a command fails:** read the error, check `docker ps -a`, and whether the name or port is already in use.

---

## Course layout

```
Docker-5-Day-Course/
├── README.md
├── Command-Cheat-Sheet.md
├── images/
├── sample-app/
├── Day-01-Docker-Fundamentals/
├── Day-02-Images-and-Dockerfile/
├── Day-03-Data-and-Networking/
├── Day-04-Compose-and-Registry/
└── Day-05-Ops-Security-Capstone/
```

---

## Connects to other courses in this repo

| After Docker… | Continue with… |
| ------------- | -------------- |
| Need Linux first | [Linux 5-Day Course](../Linux-5-Day-Course/) |
| CI/CD | [Azure DevOps 6-Day Course](../Azure-DevOps-6-Day-Course/) |
| Cloud VMs | [AZ-104 Azure Administrator](../AZ-104-Azure-Administrator/) |

---

## Course images

| Image | Used in |
| ----- | ------- |
| `images/docker-vm-vs-container.png` | Day 1 — VM vs container |
| `images/docker-architecture.png` | Day 1 — client, daemon, registry |
| `images/docker-image-vs-container.png` | Day 1 — image vs container |
| `images/docker-run-steps.png` | Day 1 — what `docker run` does |
| `images/docker-dockerfile-layers.png` | Day 2 — Dockerfile layers |
| `images/docker-port-mapping.png` | Day 3 — ports |
| `images/docker-volumes.png` | Day 3 — volumes |
| `images/docker-networks.png` | Day 3 — networks |
| `images/docker-compose-app.png` | Day 4 — Compose |
| `images/docker-registry-push-pull.png` | Day 4 — Hub |
| `images/docker-multistage.png` | Day 4 — multi-stage |
