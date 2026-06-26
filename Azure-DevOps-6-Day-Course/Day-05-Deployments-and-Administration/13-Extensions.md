# 13 - Extensions

## Overview

**Extensions** add new capabilities to Azure DevOps — pipeline **tasks**, dashboard **widgets**, **boards** enhancements, code tools, and integrations. They come from the **Visual Studio Marketplace** (free and paid), or you can build your own.

## Where Extensions Come From

- **[Visual Studio Marketplace → Azure DevOps](https://marketplace.visualstudio.com/azuredevops)** — thousands of published extensions.
- **Custom/private** — your org can build and share internal extensions.

## What Extensions Can Add

| Contribution | Example |
| ------------ | ------- |
| **Pipeline tasks** | SonarQube analysis, Terraform, Slack notify, OWASP scan |
| **Dashboard widgets** | Custom charts, velocity, build monitors |
| **Boards features** | Delivery Plans, extra work item controls |
| **Repos features** | Code search, PR enhancements |
| **Hubs/menus** | New pages in the navigation |
| **Service hooks** | Integrations with external systems |

## Installing an Extension

1. Browse the **Marketplace** and pick an extension.
2. Click **Get it free** (or buy) → select your **organization**.
3. An **organization admin** approves/installs it.
4. The extension's tasks/widgets become available across the org.

Manage installed extensions at **Organization settings → Extensions**.

## Popular Extensions

- **SonarQube / SonarCloud** — code quality & security analysis.
- **Terraform / Azure DevOps Terraform tasks** — IaC.
- **Replace Tokens** — substitute config tokens at deploy time.
- **Slack / Microsoft Teams** — notifications.
- **WhiteSource/Mend, OWASP Dependency-Check** — security scanning.
- **Delivery Plans** — cross-team roadmap (now often built-in).
- **Code Coverage / Build widgets** — reporting.

## Using an Extension's Pipeline Task

Once installed, an extension task is referenced like any other task:

```yaml
steps:
  - task: SonarQubePrepare@5
    inputs:
      SonarQube: 'sonar-connection'
      scannerMode: 'MSBuild'
      projectKey: 'myapp'
```

## Security Considerations

Extensions run **inside your org/pipelines**, so treat them like dependencies:
- Install only from **trusted publishers**.
- Review the **permissions/scopes** an extension requests.
- Prefer widely used, well-maintained extensions.
- Periodically **audit** installed extensions and remove unused ones.
- Pin task **versions** for reproducibility.

## Building Custom Extensions (Overview)

You can author extensions with the **Azure DevOps Extension SDK**:
- Package contributions (tasks/widgets/hubs) into a `.vsix`.
- Publish privately to your org or publicly to the Marketplace.
- Useful for org-specific tasks, widgets, or integrations.

## Best Practices

- Only install **trusted, necessary** extensions.
- Review requested **scopes/permissions**.
- **Audit** and prune installed extensions regularly.
- Pin task versions; test extension updates before broad use.

## Summary

- Extensions add tasks, widgets, and integrations from the Marketplace (or custom).
- Install via the Marketplace; manage at **Organization settings → Extensions**.
- Treat them as trusted dependencies — vet publishers, scopes, and keep them maintained.

## Knowledge Check

1. Where do most Azure DevOps extensions come from?
2. Name two things an extension can contribute.
3. Why should you review an extension's requested scopes before installing?

➡️ Next: [14 - Audit Logs](./14-Audit-Logs.md)
