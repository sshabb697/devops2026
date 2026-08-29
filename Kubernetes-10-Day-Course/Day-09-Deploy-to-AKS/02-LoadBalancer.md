# 02 — LoadBalancer on AKS

**Learning objectives**

- Azure creates a **public IP** for `type: LoadBalancer`
- It can take a **few minutes**; `EXTERNAL-IP` stays `<pending>` until ready

---

## One-sentence idea

LoadBalancer = Azure puts a **public doorbell** in front of your Service.

Same change as [aks-workshop Exercise 9](https://github.com/sshabb697/aks-workshop/blob/main/content/labs/02.basic-aks.md): ClusterIP → LoadBalancer.

---

## Knowledge check

1. Does LoadBalancer cost extra (public IP / LB)?
2. Should you leave it running all month for a class demo?

<details>
<summary>Answers</summary>

1. Yes, small extra cost.  
2. No — delete on Day 10.

</details>

➡️ Next: [Lab 09B](./Lab-09B-LoadBalancer.md)
