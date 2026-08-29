# Kubernetes 10-Day Course

Hands-on Kubernetes for **new students**, including people who are **not from IT**. Each class is **1 hour**. You will see pictures, a short story, one example, then a lab.

> Goal: **run, scale, and heal apps** on Kubernetes — first on your laptop, then on **Azure Kubernetes Service (AKS)**.

Print or keep open: **[Command Cheat Sheet](./Command-Cheat-Sheet.md)** · Tutors: **[Tutor Notes](./Tutor-Notes.md)** · Class slides: **[Slides](./Slides/)**

This course is written for classroom use. It started from [Kubelabs](https://collabnix.github.io/kubelabs/) and the [AKS workshops](https://github.com/sshabb697/aks-workshops) / [AKS workshop labs](https://github.com/sshabb697/aks-workshop/tree/main/content/labs), and also uses **official Kubernetes docs**, **Microsoft Learn**, **CNCF Phippy**, and **Killercoda**.

**After class (optional):** [Resources/Useful-Links.md](./Resources/Useful-Links.md) · [Optional homework by day](./Resources/Optional-Homework.md)

---

## What you will be able to do

By Day 10 you can:

1. Explain Kubernetes with a simple analogy (hotel manager, not “magic cloud”).
2. Run a Pod, a Deployment, and a Service on a local cluster.
3. Change app settings with ConfigMaps and Secrets (without rebuilding the image).
4. Expose an app with a Service / Ingress.
5. Create a small **AKS** cluster, pull an image from **ACR**, and deploy an app.

| Day | Topic | Outcome | Slides |
| --- | ----- | ------- | ------ |
| [Day 1](./Day-01-Why-Kubernetes/) | Why Kubernetes | Picture in your head: Docker vs Kubernetes | [Deck](./Slides/01-Day-Why-Kubernetes.md) |
| [Day 2](./Day-02-Cluster-and-kubectl/) | Cluster + kubectl | Cluster is running; you can talk to it | [Deck](./Slides/02-Day-Cluster-and-kubectl.md) |
| [Day 3](./Day-03-Pods/) | Pods | Deploy, view, exec, delete a Pod | [Deck](./Slides/03-Day-Pods.md) |
| [Day 4](./Day-04-ReplicaSets-and-Deployments/) | ReplicaSet + Deployment | Scale, update, rollback | [Deck](./Slides/04-Day-ReplicaSets-and-Deployments.md) |
| [Day 5](./Day-05-Services/) | Services | Reach the app by name or public IP | [Deck](./Slides/05-Day-Services.md) |
| [Day 6](./Day-06-ConfigMaps-and-Secrets/) | Config + Secrets | Change config without a new image | [Deck](./Slides/06-Day-ConfigMaps-and-Secrets.md) |
| [Day 7](./Day-07-Storage-and-Ingress/) | Disks + Ingress | Persist a file; one URL, two apps | [Deck](./Slides/07-Day-Storage-and-Ingress.md) |
| [Day 8](./Day-08-AKS-Cluster/) | AKS cluster | Create AKS + ACR and connect kubectl | [Deck](./Slides/08-Day-AKS-Cluster.md) |
| [Day 9](./Day-09-Deploy-to-AKS/) | Deploy to AKS | App live on a LoadBalancer | [Deck](./Slides/09-Day-Deploy-to-AKS.md) |
| [Day 10](./Day-10-Scale-Monitor-Capstone/) | Scale, logs, cleanup | Scale + troubleshoot + delete Azure resources | [Deck](./Slides/10-Day-Scale-Monitor-Capstone.md) |

---

## Class timing (every day = 60 minutes)

| Block | Minutes |
| ----- | ------- |
| Lesson A (talk + picture) | 10 |
| Lab A (students do it) | 15 |
| Lesson B | 10 |
| Lab B | 15 |
| Recap / questions | 10 |

**After every lesson there is a lab.** Do not skip labs. Kubernetes only sticks when you type the commands.

---

## Prerequisites

- [Docker 5-Day Course](../Docker-5-Day-Course/) **or** you can run `docker run nginx`
- Comfort with a terminal (`cd`, `ls` / `dir`)
- Windows + **WSL2** or Docker Desktop, macOS, or Linux
- **Days 1–7:** Docker Desktop with Kubernetes **on**, [minikube](https://minikube.sigs.k8s.io/), or a browser lab ([Killercoda](https://killercoda.com/playgrounds/scenario/kubernetes))
- **Days 8–10:** Azure subscription (student / free trial is enough). AKS is **not free**. Use **1 small node** and **delete the cluster on Day 10**.

---

## How to teach / study

1. Show the **picture**.
2. Read the **one-sentence idea**.
3. Walk through the **example**.
4. Students complete the **lab**.
5. Use the **cheat sheet** when someone forgets a command.

**If a command fails:** read the error, then `kubectl get pods`, `kubectl describe pod NAME`, `kubectl logs NAME`.

---

## Course layout

```
Kubernetes-10-Day-Course/
├── README.md
├── Command-Cheat-Sheet.md
├── Tutor-Notes.md
├── Slides/          ← Marp decks for the projector
├── Resources/       ← extra links, optional homework, bonus probe lab
├── images/
├── manifests/
└── Day-01- … Day-10- …
```

**Show in class:** [Slides/README.md](./Slides/README.md) (install **Marp for VS Code**, then open preview).

---

## Connects to other courses in this repo

| Before this course | After this course |
| ------------------ | ----------------- |
| [Docker 5-Day Course](../Docker-5-Day-Course/) | [Azure DevOps 6-Day Course](../Azure-DevOps-6-Day-Course/) (CI/CD to AKS) |
| [Linux 5-Day Course](../Linux-5-Day-Course/) | [AZ-104](../AZ-104-Azure-Administrator/) (VMs, networking around AKS) |

---

## Course images

| Image | Used in |
| ----- | ------- |
| `images/k8s-why-conductor.png` | Day 1 — Docker vs Kubernetes |
| `images/k8s-architecture.png` | Day 1 — Control plane and workers |
| `images/k8s-kubectl-flow.png` | Day 2 — How kubectl talks to the cluster |
| `images/k8s-pod.png` | Day 3 — What a Pod is |
| `images/k8s-replicaset-deployment.png` | Day 4 — Deployment → ReplicaSet → Pods |
| `images/k8s-service.png` | Day 5 — ClusterIP, NodePort, LoadBalancer |
| `images/k8s-configmap-secret.png` | Day 6 — Settings vs passwords |
| `images/k8s-volume-pvc.png` | Day 7 — PVC and disk |
| `images/k8s-ingress.png` | Day 7 — One door, many apps |
| `images/k8s-aks-managed.png` | Day 8 — What Azure manages |
| `images/k8s-acr-aks-flow.png` | Day 9 — Build → ACR → AKS |
| `images/k8s-troubleshoot.png` | Day 10 — Pod not Ready |
