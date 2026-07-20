# Challenge 04 — ARM / Bicep Templates (Infrastructure as Code)

**Time:** 45–60 minutes  
**You will learn:** What ARM is, deploy a template from the portal, then create and deploy a small Public IP template with parameters via Cloud Shell.

## Concepts (read first)

| Term | Meaning |
| ---- | ------- |
| **Resource** | A manageable Azure object (VM, storage, PIP, …) |
| **Resource group** | Lifecycle container; deployments target an RG |
| **Resource provider** | API that creates a type (e.g. `Microsoft.Storage`) |
| **ARM template** | JSON that describes resources to deploy |
| **Bicep** | Cleaner language that compiles to ARM |

Portal, CLI, PowerShell, and REST all go through **Azure Resource Manager**.

---

## Part A — See resource providers (5 min)

Cloud Shell (Bash):

```bash
az provider list -o table | head -n 30
```

Portal: **Subscriptions → your subscription → Resource providers** — note `Microsoft.Storage`, `Microsoft.Network`, `Microsoft.Compute`.

---

## Part B — Deploy a storage account template from the portal (15 min)

1. Portal → **+ Create a resource** → search **Template deployment** → **Create**.
2. **Build your own template in the editor**.
3. Paste this template:

```json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "storageAccountName": {
      "type": "string",
      "metadata": { "description": "Globally unique storage account name" }
    },
    "location": {
      "type": "string",
      "defaultValue": "[resourceGroup().location]"
    }
  },
  "resources": [
    {
      "type": "Microsoft.Storage/storageAccounts",
      "apiVersion": "2022-05-01",
      "name": "[parameters('storageAccountName')]",
      "location": "[parameters('location')]",
      "sku": { "name": "Standard_LRS" },
      "kind": "StorageV2",
      "properties": {}
    }
  ]
}
```

4. **Save**.
5. Select resource group `rg-d1-<yourname>` (or create `rg-d1-<yourname>-arm`).
6. Parameter `storageAccountName`: e.g. `std1arm<yourname>01`.
7. **Review + create → Create**.

✅ **Checkpoint:** New storage account appears from the template (not the portal storage wizard).

---

## Part C — Build a Public IP template yourself (20 min)

### 1. Create files locally or in Cloud Shell editor

`pip.json`:

```json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "IPName": {
      "type": "string",
      "metadata": { "description": "Public IP resource name" }
    }
  },
  "resources": [
    {
      "type": "Microsoft.Network/publicIPAddresses",
      "apiVersion": "2020-06-01",
      "name": "[parameters('IPName')]",
      "location": "[resourceGroup().location]",
      "sku": { "name": "Standard" },
      "properties": {
        "publicIPAllocationMethod": "Static",
        "publicIPAddressVersion": "IPv4"
      }
    }
  ]
}
```

`pip.parameters.json`:

```json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentParameters.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "IPName": { "value": "pip-d1-arm-<yourname>" }
  }
}
```

### 2. Upload to Cloud Shell (upload button) or create with `code pip.json` / `cat > pip.json`.

### 3. Deploy

```bash
az group create -n rg-d1-<yourname>-arm -l <region> --tags Owner=<yourname> Env=Lab Day=Day1

az deployment group create \
  -g rg-d1-<yourname>-arm \
  --template-file pip.json \
  --parameters @pip.parameters.json
```

✅ **Checkpoint:** `pip-d1-arm-<yourname>` exists in the ARM resource group.

---

## Part D — Incremental vs Complete (read)

| Mode | Behavior |
| ---- | -------- |
| **Incremental** (default) | Adds/updates resources in the template; leaves others alone |
| **Complete** | Resources **not** in the template can be **deleted** from the RG |

Use Complete only when you understand the blast radius.

---

## Optional — same idea in Bicep

```bicep
param IPName string

resource pip 'Microsoft.Network/publicIPAddresses@2020-06-01' = {
  name: IPName
  location: resourceGroup().location
  sku: { name: 'Standard' }
  properties: {
    publicIPAllocationMethod: 'Static'
    publicIPAddressVersion: 'IPv4'
  }
}
```

```bash
az deployment group create -g rg-d1-<yourname>-arm --template-file pip.bicep --parameters IPName=pip-d1-bicep-<yourname>
```

---

## Deliverables

- [ ] Deployed storage via Template deployment in portal  
- [ ] Created `pip.json` + parameters file  
- [ ] Deployed with `az deployment group create`  
- [ ] Can explain parameter file purpose (Dev/Test/Prod)  

## Cleanup

```bash
az group delete -n rg-d1-<yourname>-arm --yes --no-wait
# optional: delete template-created storage in rg-d1-<yourname>
```

➡️ Next: [Challenge 05 — VNet Peering](./challenge-05-vnet-peering.md)
