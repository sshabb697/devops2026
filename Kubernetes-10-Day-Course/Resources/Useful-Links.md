# Useful links

Use **this course first**. These are extra sources that are clear, free, and good for beginners. They are **not** required in the 1-hour class.

---

## Best for non-IT and new students

| Resource | Why it is good |
| -------- | -------------- |
| [The Illustrated Children’s Guide to Kubernetes (Phippy)](https://www.cncf.io/phippy/the-childrens-illustrated-guide-to-kubernetes/) | Story + pictures. Read after Day 1. |
| [Phippy & Friends (CNCF)](https://www.cncf.io/phippy/) | Same characters; extra short stories |
| [Kubernetes Glossary](https://kubernetes.io/docs/reference/glossary/) | One-line meanings of words |
| [Learn Kubernetes Basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/) | Official 6 modules: deploy, expose, scale, update |

---

## Official Kubernetes (bookmark these)

- [What is Kubernetes?](https://kubernetes.io/docs/concepts/overview/)
- [Cluster architecture](https://kubernetes.io/docs/concepts/architecture/)
- [Pod](https://kubernetes.io/docs/concepts/workloads/pods/)
- [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [Service](https://kubernetes.io/docs/concepts/services-networking/service/)
- [ConfigMap](https://kubernetes.io/docs/concepts/configuration/configmap/)
- [Secret](https://kubernetes.io/docs/concepts/configuration/secret/)
- [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
- [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/)
- [Debug applications](https://kubernetes.io/docs/tasks/debug/debug-application/)
- [kubectl cheat sheet (official)](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
- [Hello Minikube](https://kubernetes.io/docs/tutorials/hello-minikube/)
- [Learning environment](https://kubernetes.io/docs/setup/learning-environment/) (minikube, kind, playgrounds)

**ConfigMap lab (official):** [Configure Redis using a ConfigMap](https://kubernetes.io/docs/tutorials/configuration/configure-redis-using-configmap/)

---

## Browser labs (no laptop cluster)

Use if Docker Desktop is slow or a student has a weak PC.

- [Killercoda Kubernetes playground](https://killercoda.com/playgrounds/scenario/kubernetes) — real cluster in the browser (~60 min sessions)
- [Killercoda Kubernetes scenarios](https://killercoda.com/kubernetes)
- [Play with Kubernetes](https://labs.play-with-k8s.com/) (Play-with-K8s; related to Docker labs)
- Official list: [Online playgrounds](https://kubernetes.io/docs/setup/learning-environment/)

---

## Azure / AKS (Days 8–10)

- [What is AKS?](https://learn.microsoft.com/azure/aks/what-is-aks)
- [Microsoft Learn: Introduction to Kubernetes](https://learn.microsoft.com/training/modules/intro-to-kubernetes/) (~53 min)
- [Microsoft Learn: Introduction to Kubernetes on Azure](https://learn.microsoft.com/training/paths/intro-to-kubernetes-on-azure/)
- [Quickstart: AKS with Azure CLI](https://learn.microsoft.com/azure/aks/learn/quick-kubernetes-deploy-cli)
- [Authenticate AKS to ACR](https://learn.microsoft.com/azure/aks/cluster-container-registry-integration)
- [AKS cost / stop a cluster](https://learn.microsoft.com/azure/aks/stop-cluster) (stop is not the same as delete; **this class deletes** the resource group)

---

## Pictures and extra explanations

- [Learnk8s visual guides](https://learnk8s.io/blog) — very clear diagrams (tutor prep)
- [Kubernetes by Example](https://kubernetesbyexample.com/) — short YAML examples per object
- [ingress-nginx](https://kubernetes.github.io/ingress-nginx/) — the controller we mention on Day 7

---

## Original sources this course was built from

- [Kubelabs](https://collabnix.github.io/kubelabs/)
- [aks-workshops](https://github.com/sshabb697/aks-workshops)
- [aks-workshop labs](https://github.com/sshabb697/aks-workshop/tree/main/content/labs)

---

## After this 10-day class (not in the 1-hour plan)

| Topic | Start here |
| ----- | ---------- |
| Helm | [Helm docs](https://helm.sh/docs/) |
| HPA | [Horizontal Pod Autoscaler](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) |
| KEDA | [keda.sh](https://keda.sh/) and [aks-workshops scaling](https://github.com/sshabb697/aks-workshops) |
| GitOps | [Flux](https://fluxcd.io/) / Argo CD |
| CKA exam later | [CKA curriculum](https://www.cncf.io/certification/cka/) — only after you are comfortable |

Homework mapped to each day: [Optional-Homework.md](./Optional-Homework.md)
