# 01 — Why Services exist

**Learning objectives**

- Pod IPs **change** when Pods restart
- A **Service** is a stable **name + load balancer** in front of Pods that share a label

---

## One-sentence idea

A Service is the **front desk phone number**. Guests (Pods) change rooms; the number stays.

![Service types](../images/k8s-service.png)

---

## Everyday analogy: pizza shop

Chefs (Pods) come and go. The shop phone number (**Service**) stays. Callers do not need each chef’s personal number.

The Service finds Pods with **selectors** (stickers from Day 3): `app: hello`.

---

## Knowledge check

1. If you bookmark a Pod IP, what happens after a restart?
2. What must match: Service selector and Pod labels?

<details>
<summary>Answers</summary>

1. The bookmark breaks.  
2. Yes — otherwise the Service has no backends.

</details>

➡️ Next: [Lab 05A](./Lab-05A-ClusterIP.md)
