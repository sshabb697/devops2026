# 05 - Secure Files

## Overview

**Secure files** let you store sensitive **binary files** — certificates, signing keys, keystores, provisioning profiles, `.env` files — in the Library so pipelines can use them **without committing them to source control**. They are encrypted at rest and only downloaded to the agent at runtime.

## Why Secure Files?

- Keep **secrets out of the repo** (a leaked repo shouldn't leak your signing cert).
- Reuse the same file across pipelines.
- Control **who and which pipelines** can use each file.
- Files are **deleted from the agent** after the job (on Microsoft-hosted agents the VM is destroyed anyway).

## Common Uses

| File | Used for |
| ---- | -------- |
| **Code signing certificate** (`.pfx`, `.p12`) | Signing apps/installers |
| **Android keystore** (`.jks`) | Signing Android APKs/AABs |
| **Apple provisioning profile / certificate** | iOS builds |
| **SSH private key** | Deploying to servers |
| **`.env` / config file** | Runtime configuration |

## Uploading a Secure File

1. **Pipelines → Library → Secure files → + Secure file**.
2. Upload the file.
3. Set **permissions** and **pipeline authorization**.

## Using a Secure File in YAML

Use the **DownloadSecureFile** task; it downloads the file to a temp path and exposes it via an output variable:

```yaml
steps:
  - task: DownloadSecureFile@1
    name: signingCert            # name to reference its output
    inputs:
      secureFile: 'signing.pfx'

  - script: |
      echo "Cert is at $(signingCert.secureFilePath)"
      # use the file, e.g., import the certificate
    displayName: 'Use the certificate'
```

The path is available as `$(<taskName>.secureFilePath)`.

## Example: Android Signing

```yaml
steps:
  - task: DownloadSecureFile@1
    name: keystore
    inputs:
      secureFile: 'release.jks'

  - task: AndroidSigning@3
    inputs:
      apkFiles: '**/*.apk'
      apksign: true
      apksignerKeystoreFile: '$(keystore.secureFilePath)'
      apksignerKeystorePassword: '$(keystorePassword)'   # a secret variable
```

## Security & Permissions

- **Roles:** Administrator / User on each secure file.
- **Pipeline permissions:** authorize specific pipelines (prompted on first use).
- Combine with **approvals/checks** on the resource for production-sensitive files.
- The file is only ever materialized on the agent during the job, then removed.

## Secure Files vs Secret Variables

| | Secret variable | Secure file |
| --- | --------------- | ----------- |
| Stores | A string value | A binary file |
| Example | API key, password | Certificate, keystore |
| Access in pipeline | `$(secret)` (mapped) | DownloadSecureFile task → path |

## Best Practices

- Store **certs/keys/profiles** as secure files, never in the repo.
- Pair a secure file (the cert) with a **secret variable** (its password).
- **Restrict** which pipelines can use each file.
- Rotate files periodically and re-upload.

## Summary

- Secure files keep sensitive **binaries** out of source control, encrypted in the Library.
- Download them at runtime with **DownloadSecureFile@1** and reference `secureFilePath`.
- Control access via roles and pipeline permissions; combine with secret variables for passwords.

## Knowledge Check

1. When would you use a secure file instead of a secret variable?
2. Which task downloads a secure file, and how do you get its path?
3. What happens to the file after the job completes?

➡️ Next: [06 - Approvals](./06-Approvals.md)
