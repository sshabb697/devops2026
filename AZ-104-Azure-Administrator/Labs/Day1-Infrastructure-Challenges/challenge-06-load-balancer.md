# Challenge 06 — Load Balancer for a Web Farm

**Time:** 50–70 minutes  
**You will learn:** Place a **public Azure Load Balancer** in front of two web VMs and verify traffic distribution / failover.

## Target architecture

```
  Internet → Public IP → Load Balancer (port 80)
                           ├── vm-web-01  (IIS or nginx)
                           └── vm-web-02  (IIS or nginx)
```

---

## Part A — Create the lab resource group

1. Create RG: `rg-d1-<yourname>-lb` in `<region>`.
2. Create VNet: `vnet-d1-lb` · `10.10.0.0/16` · subnet `snet-web` `10.10.1.0/24`.

---

## Part B — Create two web VMs (25 min)

Create **two** VMs in the same VNet/subnet:

| Setting | VM 1 | VM 2 |
| ------- | ---- | ---- |
| Name | `vm-web-01` | `vm-web-02` |
| Size | B1s / B2s | B1s / B2s |
| Image | Windows Server 2022 **or** Ubuntu 22.04 | same |
| Public IP | **None** (LB will be the front door) | **None** |
| NSG | Allow **HTTP 80** from AzureLoadBalancer + Internet (or Any for lab); allow SSH/RDP from My IP | same |

### Install a simple web page

**Windows (PowerShell as admin after RDP):**

```powershell
Install-WindowsFeature -name Web-Server -IncludeManagementTools
"<h1>Served by $($env:COMPUTERNAME)</h1>" | Out-File C:\inetpub\wwwroot\index.html -Encoding utf8
```

**Linux (after SSH):**

```bash
sudo apt-get update && sudo apt-get install -y nginx
echo "<h1>Served by $(hostname)</h1>" | sudo tee /var/www/html/index.html
sudo systemctl enable --now nginx
```

Use **Bastion** or temporarily a public IP for setup, then remove public IPs if you added them only for install.

✅ **Checkpoint:** Each VM serves a page that shows its own hostname (test via private IP from a jump box, or keep a temp public IP during setup).

---

## Part C — Create the Load Balancer (15 min)

1. **+ Create a resource → Load Balancer → Create**.
2. Basics:

| Field | Value |
| ----- | ----- |
| Resource group | `rg-d1-<yourname>-lb` |
| Name | `lb-wwwfarm` |
| Region | `<region>` |
| Type | **Public** |
| SKU | **Standard** |
| Tier | Regional |

3. **Frontend IP:** add new public IP `pip-wwwfarm` (Standard, Static).
4. **Backend pool:** create `bepool-web` → add NICs of `vm-web-01` and `vm-web-02`.
5. **Health probe:**
   - Name: `probe-http`
   - Protocol: TCP (or HTTP path `/`)
   - Port: **80**
6. **Load balancing rule:**
   - Name: `rule-http`
   - Frontend port **80** → Backend port **80**
   - Backend pool: `bepool-web`
   - Health probe: `probe-http`
7. Create / save all components. Wait until LB provisioning finishes.

---

## Part D — Test (10 min)

1. Copy the Load Balancer frontend **public IP**.
2. Browse: `http://<lb-public-ip>/`
3. Refresh several times — you should see **hostname** alternate between the two VMs (not always guaranteed per browser connection reuse; try private window / curl).

```bash
curl http://<lb-public-ip>/
```

✅ **Checkpoint:** Page loads through the LB IP.

---

## Part E — Failover test (optional)

1. **Stop** `vm-web-01`.
2. Wait for probe to mark it down (about 1–2 minutes).
3. Browse again — traffic should still work via `vm-web-02`.
4. Start `vm-web-01` again and confirm it returns to the pool.

---

## Deliverables

- [ ] Two web VMs behind one public Load Balancer  
- [ ] Health probe on port 80  
- [ ] LB rule forwarding HTTP  
- [ ] Browser/curl test succeeded  
- [ ] (Optional) Stopped one VM; site stayed up  

## Cleanup

```bash
az group delete -n rg-d1-<yourname>-lb --yes --no-wait
```

➡️ Next (optional): [Challenge 07 — Custom Script Extension](./challenge-07-custom-script-extension.md)
