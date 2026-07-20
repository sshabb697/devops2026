# Challenge 02 — Cloud Shell: Code Your Azure Resources

**Time:** 30–40 minutes  
**You will learn:** Use Azure Cloud Shell (Bash or PowerShell) to query and manage resources without installing tools locally.

## Why Cloud Shell?

- Already authenticated to your subscription  
- Azure CLI and PowerShell Az modules preinstalled  
- Good for demos, labs, and quick automation  

---

## Step 1 — Open Cloud Shell

1. In the portal, click the **Cloud Shell** icon (`>_`) near the top right.
2. Choose **Bash** (recommended for these steps) or **PowerShell**.
3. First time only: create Cloud Shell storage when prompted (advanced settings optional).

✅ **Checkpoint:** A terminal panel opens at the bottom of the portal.

---

## Step 2 — Who am I? What do I have?

**Bash:**

```bash
az account show -o table
az group list -o table
az resource list -g rg-d1-<yourname> -o table
```

**PowerShell:**

```powershell
Get-AzContext
Get-AzResourceGroup | Format-Table
Get-AzResource -ResourceGroupName rg-d1-<yourname> | Format-Table
```

✅ **Checkpoint:** Your Day 1 RG and VM/VNet appear in the list.

---

## Step 3 — Explore useful commands

```bash
# VM sizes in your region (Bash)
az vm list-sizes --location <region> -o table | head

# Show your VM
az vm show -g rg-d1-<yourname> -n vm-d1-<yourname>-01 -o table

# Public IP
az network public-ip show -g rg-d1-<yourname> -n pip-d1-<yourname>-vm --query "{ip:ipAddress,dns:dnsSettings.fqdn}" -o table
```

PowerShell equivalents:

```powershell
Get-AzVMSize -Location '<region>' | Select-Object -First 15
Get-AzVM -ResourceGroupName rg-d1-<yourname> -Name vm-d1-<yourname>-01
```

---

## Step 4 — Make a small change from the shell

Add a tag to the VM:

```bash
az vm update -g rg-d1-<yourname> -n vm-d1-<yourname>-01 --set tags.ManagedBy=CloudShell
az vm show -g rg-d1-<yourname> -n vm-d1-<yourname>-01 --query tags
```

Confirm in the portal: VM → **Tags**.

✅ **Checkpoint:** Tag `ManagedBy=CloudShell` visible in portal.

---

## Step 5 — Optional: create a tiny resource with CLI

```bash
az network nsg rule list -g rg-d1-<yourname> --nsg-name <your-nsg-name> -o table
```

Find NSG name from:

```bash
az network nsg list -g rg-d1-<yourname> -o table
```

---

## Step 6 — Optional stretch: create a second small VM with defaults

> Creates extra cost. Skip unless instructor asks.

```powershell
# PowerShell example — uses many defaults; prefer explicit networking in real work
$cred = Get-Credential   # not admin/administrator
New-AzVM -Name "vm-d1-temp" -Credential $cred -Location "<region>"
# Then delete:
Remove-AzResourceGroup -Name "vm-d1-temp" -Force -AsJob
```

Better practice is always specifying VNet/NIC/size (see Challenge 04 templates).

---

## Deliverables

- [ ] Cloud Shell opened successfully  
- [ ] Listed account, RGs, and Day 1 resources  
- [ ] Updated a tag from the CLI  
- [ ] Can switch between portal and shell confidently  

## Tip

Cloud Shell times out when idle — reopen and re-run `az account show` if commands fail oddly.

➡️ Next: [Challenge 03 — Storage](./challenge-03-storage.md)
