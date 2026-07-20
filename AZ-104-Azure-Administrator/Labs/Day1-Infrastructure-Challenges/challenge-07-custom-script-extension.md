# Challenge 07 (Optional) — Custom Script Extension

**Time:** 40–50 minutes  
**You will learn:** Run a script inside a VM **after** deployment using the Custom Script Extension (CSE) — the start of “zero-touch” VM setup.

## Prerequisites

- A **Windows** VM (easiest for this lab) in your subscription — reuse Day 1 VM if Windows, or create `vm-d1-<yourname>-cse` (Windows Server 2022, B2s)
- Storage account (Challenge 03) for hosting the script

---

## Part A — Create the script

1. On your PC, create `HelloWorld.ps1`:

```powershell
$folderPath = Join-Path 'C:' 'temp'
$filePath = Join-Path $folderPath 'CSEwasRunAt.txt'

if (-not (Test-Path -Path $folderPath)) {
  New-Item -Path $folderPath -ItemType 'Directory'
}

Get-Date | Out-File $filePath -Append
```

---

## Part B — Upload script to storage

1. Storage account → **Containers → + Container** → name `csescripts` · Public access: **Blob** (anonymous read) *for lab simplicity*  
   - Prod: keep private + SAS/identity for the extension.
2. Upload `HelloWorld.ps1`.
3. Open the blob → copy URL. Test in browser — file should download.

✅ **Checkpoint:** Script URL is reachable over HTTPS.

---

## Part C — Attach Custom Script Extension

1. Virtual machines → your Windows VM → **Extensions + applications → + Add**.
2. Select **Custom Script Extension** → Next.
3. **Browse** to the blob `HelloWorld.ps1` in `csescripts` (or paste URI).
4. Create / OK. Wait until extension status is **Provisioning succeeded**.

✅ **Checkpoint:** Extension shows success on the VM blade.

---

## Part D — Verify inside the VM

1. RDP to the VM.
2. Open `C:\temp\CSEwasRunAt.txt` — should contain a timestamp.
3. Troubleshooting folders (if it failed):
   - `C:\Packages\Plugins\Microsoft.Compute.CustomScriptExtension\...\Downloads`
   - `C:\WindowsAzure\Logs\Plugins\Microsoft.Compute.CustomScriptExtension\...`

---

## Part E — Stretch: install IIS via CSE

1. Create `Install-IIS.ps1`:

```powershell
Install-WindowsFeature -name Web-Server -IncludeManagementTools
"<h1>IIS from CSE on $env:COMPUTERNAME</h1>" | Out-File C:\inetpub\wwwroot\index.html -Encoding utf8
```

2. Upload to `csescripts`.
3. **Uninstall** the previous Custom Script Extension (only one CSE at a time via portal).
4. Add CSE again with `Install-IIS.ps1`.
5. Open NSG for port **80** from your IP.
6. Browse `http://<vm-public-ip>/`.

✅ **Checkpoint:** Default site shows your HTML from CSE.

---

## Why this matters

| Manual RDP install | CSE / ARM+CSE |
| ------------------ | ------------- |
| Slow, inconsistent | Repeatable |
| Hard to audit | Script in storage/Git |
| Easy to forget steps | “Zero-touch” after VM create |

---

## Deliverables

- [ ] Script uploaded to storage  
- [ ] CSE succeeded on VM  
- [ ] Evidence file or IIS page verified  
- [ ] Know where CSE logs live  

## Cleanup

Uninstall extension; delete VM/RG if created only for this lab.

➡️ Next (optional): [Challenge 08 — Traffic Manager](./challenge-08-traffic-manager.md)
