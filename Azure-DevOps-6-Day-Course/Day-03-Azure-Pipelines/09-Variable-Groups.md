# 09 - Variable Groups

## Overview

A **variable group** is a set of variables stored in the **Library** that can be shared across **multiple pipelines**. Instead of defining the same values (or secrets) in every pipeline, you define them once and link them where needed.

## Why Variable Groups?

- **Reuse** — share config across many pipelines.
- **Central management** — change a value in one place.
- **Secrets** — store sensitive values securely, optionally backed by **Azure Key Vault**.
- **Environment separation** — e.g., `settings-dev`, `settings-prod`.

## Creating a Variable Group

1. **Pipelines → Library → + Variable group**.
2. Name it (e.g., `web-app-settings`).
3. Add variables as name/value pairs.
4. Toggle the **lock icon** to mark a value as a **secret** (masked, encrypted).
5. (Optional) Toggle **Link secrets from an Azure key vault** to pull secrets from Key Vault.
6. **Save**.

## Using a Variable Group in YAML

```yaml
variables:
  - group: 'web-app-settings'          # link the group
  - name: localVar                      # plus inline variables
    value: 'hello'

steps:
  - script: echo "Connection: $(connectionString)"   # from the group
```

You can link multiple groups:

```yaml
variables:
  - group: 'common-settings'
  - group: 'prod-settings'
```

## Linking to Azure Key Vault

For secrets managed centrally in Azure:

1. Create the variable group and enable **Link secrets from an Azure key vault as variables**.
2. Select the **Azure subscription** (via a service connection) and the **Key Vault**.
3. Choose which secrets to expose as variables.
4. Reference them like any other variable: `$(MySecretFromKeyVault)`.

Benefits: secrets never live in Azure DevOps; rotation happens in Key Vault; access is audited.

## Scoping Variable Groups to Stages

Link a group only where needed, e.g., production secrets only in the prod stage:

```yaml
stages:
  - stage: DeployProd
    variables:
      - group: 'prod-settings'
    jobs:
      - deployment: Prod
        environment: 'production'
        strategy:
          runOnce:
            deploy:
              steps:
                - script: echo "Deploying with $(prodApiKey)"
```

## Securing Variable Groups

- Set **permissions** on each group (who can read/use/manage it).
- Restrict which **pipelines** can access a group (pipeline permissions / "Authorize").
- Mark sensitive values as **secrets** (or use Key Vault).

## Variable Group vs Inline Variables

| | Inline variables | Variable group |
| --- | ---------------- | -------------- |
| Scope | One pipeline | Many pipelines |
| Stored in | The YAML file | Library (portal) |
| Secrets | Per-pipeline secret vars | Group secrets / Key Vault |
| Best for | Pipeline-specific values | Shared config & secrets |

## Summary

- Variable groups store reusable variables/secrets in the **Library**.
- Link them in YAML with `variables: - group: <name>`.
- Back secrets with **Azure Key Vault** for centralized, audited secret management.
- Control access with group permissions and pipeline authorization.

## Knowledge Check

1. Where are variable groups stored and managed?
2. How do you reference a variable group in a YAML pipeline?
3. What's the advantage of linking a group to Azure Key Vault?

➡️ Next: [10 - Templates](./10-Templates.md)
