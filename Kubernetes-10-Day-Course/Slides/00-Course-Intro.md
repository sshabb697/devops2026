---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section { font-size: 28px; }
  h1 { color: #0078d4; }
  h2 { color: #106ebe; }
  table { font-size: 22px; }
  footer { color: #666; font-size: 14px; }
footer: Kubernetes 10-Day Course | Intro
---

# Kubernetes in 10 days
## Simple English. Pictures. Labs.

**1 hour a day.** First your laptop. Then Azure (AKS).

---

# Who this class is for

- New to IT is OK
- You already saw **Docker** (or can run `docker run nginx`)
- We use short words and one picture at a time

You will **type commands**. Watching only is not enough.

---

# What Kubernetes is (one line)

**Docker** runs one container.

**Kubernetes** looks after **many** containers:
start them, put them on machines, restart them if they die.

---

# 10 days at a glance

| Days | Place | You learn |
|------|--------|-----------|
| 1–7 | Laptop | Pod, Deployment, Service |
| 8–9 | Azure AKS | Real cloud cluster |
| 10 | Azure | Scale, logs, **delete** (stop the bill) |

---

# Every class = 60 minutes

| Time | What we do |
|------|------------|
| 10 min | Lesson A (picture) |
| 15 min | **Lab A** — you type |
| 10 min | Lesson B |
| 15 min | **Lab B** — you type |
| 10 min | Questions |

---

# Rules that keep the class calm

1. If a command fails, **read the error**.
2. Then: `kubectl get pods`
3. Then: `kubectl describe` and `kubectl logs`
4. Days 8–10 cost money → **1 small node** → **delete on Day 10**

---

# Open these every day

- Course: `Kubernetes-10-Day-Course/README.md`
- Commands: `Command-Cheat-Sheet.md`
- Today’s folder: `Day-01` … `Day-10`

---

# Extra learning (not in the 1 hour)

After Day 1: read **Phippy** (picture story).

No laptop cluster? Use **Killercoda** in the browser.

Full list: `Resources/Useful-Links.md`

**Next:** Day 1 slides — Why Kubernetes
