# Lab 09B — Public IP

**Time:** 15 minutes

---

## Part A — Patch the Service (5 min)

```bash
kubectl apply -f hello-lb.yaml
kubectl get svc hello -n class -w
```

Wait until `EXTERNAL-IP` is a real address (not `<pending>`). `Ctrl+C`.

---

## Part B — Browser (5 min)

Open `http://EXTERNAL-IP` (http, not https). nginx welcome page.

---

## Part C — Optional ACR image (if time)

Tutors who want the full [02.basic-aks ACR build](https://github.com/sshabb697/aks-workshop/blob/main/content/labs/02.basic-aks.md) path:

```bash
az acr build --registry $ACR --image hello:1.0 .
```

Then set the Deployment image to `$ACR.azurecr.io/hello:1.0`. Skip if students have no Dockerfile handy — nginx is enough.

---

## Deliverables

- [ ] Screenshot of nginx on the public IP

➡️ **Day 10:** [Scale, monitor, capstone](../Day-10-Scale-Monitor-Capstone/README.md)
