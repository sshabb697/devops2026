# Kubernetes command cheat sheet

Copy-paste friendly. Use **PowerShell** or **bash**.

Longer official list: [kubectl cheat sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)

---

## Cluster and context

```bash
kubectl version --client
kubectl cluster-info
kubectl get nodes
kubectl get ns
kubectl config get-contexts
kubectl config current-context
```

---

## Everyday get / describe / logs

```bash
kubectl get pods
kubectl get pods -o wide
kubectl get all
kubectl describe pod POD_NAME
kubectl logs POD_NAME
kubectl logs POD_NAME -c CONTAINER_NAME
kubectl exec -it POD_NAME -- sh
```

Add `-n NAMESPACE` if the object is not in `default`.

---

## Apply YAML (the normal way)

```bash
kubectl apply -f file.yaml
kubectl delete -f file.yaml
kubectl get -f file.yaml
```

---

## Scale, update, rollback

```bash
kubectl scale deployment NAME --replicas=3
kubectl rollout status deployment/NAME
kubectl rollout history deployment/NAME
kubectl rollout undo deployment/NAME
```

---

## Services and Ingress

```bash
kubectl get svc
kubectl get ingress
kubectl port-forward svc/NAME 8080:80
```

---

## AKS (Days 8–10)

```bash
az login
az group create -n k8s-class-rg -l eastus
az aks get-credentials -g k8s-class-rg -n aks-class --overwrite-existing
az aks list -o table
az group delete -n k8s-class-rg --yes --no-wait
```

---

## If you get stuck

| You see | Try |
| ------- | --- |
| Pending | `describe pod` — often not enough CPU, or image pull |
| ImagePullBackOff | Image name/tag wrong, or no ACR permission |
| CrashLoopBackOff | `kubectl logs POD` — the app is crashing |
| Name already exists | `kubectl delete -f file.yaml` then apply again |
