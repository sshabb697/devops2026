# Tutor notes (10 × 1 hour)

Use this when **you** teach. Students follow the Day folders.

## Before Day 1

- Confirm Docker course (or equivalent) is done.
- Print [Command Cheat Sheet](./Command-Cheat-Sheet.md) and the architecture picture.
- Days 8–10: one Azure subscription plan (shared vs per student). **One node. Delete Day 10.**

## Daily rhythm

1. Open the **Marp deck** for that day (`Slides/0N-Day-….md`) — projector.
2. Students type (15 min lab). Do not lecture through the lab.
3. Repeat for lesson B.
4. Last 10 min: recap slides at the end of the deck.

How to present: [Slides/README.md](./Slides/README.md). Day 1 also has [00-Course-Intro.md](./Slides/00-Course-Intro.md) (5 minutes).

## Common stalls

| Day | Stall | What you do |
| --- | ----- | ------------ |
| 2 | Kubernetes never becomes Ready | Restart Docker Desktop; wait; then minikube as backup |
| 3 | port-forward confusion | They must leave that terminal open |
| 5 | ClusterIP “not working in Chrome” | Expected — use port-forward |
| 8 | AKS create timeout | Start create **first**, talk theory while it runs |
| 9 | EXTERNAL-IP pending | Wait 3–5 min; check quota / region |
| 10 | Forgot delete | You delete leftover `k8s-class-rg` after class |

## If Docker Desktop fails (Day 2)

Send the student to [Killercoda Kubernetes playground](https://killercoda.com/playgrounds/scenario/kubernetes). Do not burn the hour on install.

## Optional after class

Point to [Resources/Optional-Homework.md](./Resources/Optional-Homework.md). Best first homework after Day 1: [Phippy / Children’s Guide](https://www.cncf.io/phippy/the-childrens-illustrated-guide-to-kubernetes/).

If Day 4 finishes early: [Bonus liveness lab](./Resources/Bonus-Liveness.md).

Full link list: [Resources/Useful-Links.md](./Resources/Useful-Links.md)

## Sources mixed into this course

- [Kubelabs](https://collabnix.github.io/kubelabs/)
- [aks-workshops](https://github.com/sshabb697/aks-workshops) and [aks-workshop labs](https://github.com/sshabb697/aks-workshop/tree/main/content/labs)
- [Kubernetes official tutorials](https://kubernetes.io/docs/tutorials/kubernetes-basics/)
- [Microsoft Learn: Intro to Kubernetes](https://learn.microsoft.com/training/modules/intro-to-kubernetes/)
- [CNCF Phippy](https://www.cncf.io/phippy/)
- [Killercoda](https://killercoda.com/kubernetes)
