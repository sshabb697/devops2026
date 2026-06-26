# 09 - Pipeline Security

## Overview

Pipelines are powerful — they can access secrets, deploy to production, and run arbitrary code on agents. **Pipeline security** ensures that power is used safely: protecting secrets, controlling access to resources, and preventing malicious or accidental misuse.

## Key Threats to Mitigate

- **Secret leakage** — secrets printed to logs or exfiltrated by malicious code.
- **Unauthorized resource use** — a pipeline using a production connection it shouldn't.
- **Malicious PRs** — forked/PR code stealing secrets or abusing agents.
- **Privilege escalation** — over-permissive service connections/agents.

## Protecting Secrets

- Use **secret variables**, **variable groups (Key Vault)**, and **secure files** — never plaintext in YAML.
- Secrets are **masked** in logs, but don't `echo` them or write them to files.
- **Don't pass secrets** to forked-PR builds. Settings under **Pipelines → Settings**:
  - "Limit variables that can be set at queue time."
  - "Make secrets available to builds of forks" → keep **off** for public projects.
- Map secrets explicitly via `env:` so they're only available where needed.

## Protected Resources & Checks

Treat environments, service connections, variable groups, secure files, and agent pools as **protected resources**:
- Require **approvals/checks** before a pipeline can use them (lesson 07).
- Set **pipeline permissions** so only specific pipelines may use a resource.

## Pipeline Permissions & Authorization

- The first time a pipeline uses a resource, you must **authorize** it.
- Manage under each resource's **Security / Pipeline permissions**.
- Avoid "grant access to all pipelines" for production resources.

## Securing the Pipeline Definition

- YAML lives in the repo → protect it with **branch policies** (changes reviewed).
- Use **required template** checks (`extends`) to force pipelines through an approved, restricted template.
- Restrict who can **edit pipelines** and **create new pipelines** (Pipelines → Settings, and permissions).

## Agent Considerations

- **Microsoft-hosted** agents are isolated and fresh — safer for untrusted code.
- **Self-hosted** agents persist and can access internal networks — be cautious:
  - Don't run **public/fork PR** builds on self-hosted agents.
  - Isolate and harden self-hosted machines.
  - Clean workspaces between runs.

## Settable-at-Queue-Time Variables

Restrict which variables can be overridden when manually running a pipeline. Otherwise, a user could inject a malicious value. Mark only intended variables as settable at queue time.

## Task & Extension Trust

- Only install **trusted Marketplace extensions** (they run in your pipelines).
- Pin task versions; review what third-party tasks do.

## Best Practices Checklist

- [ ] Store all secrets in **variable groups (Key Vault)** / **secure files**.
- [ ] Keep "secrets to forks" **disabled**.
- [ ] Require **approvals/checks** on production resources.
- [ ] Use **pipeline permissions** — no blanket access to prod connections.
- [ ] Enforce **required template** (`extends`) for governance.
- [ ] Don't run untrusted PRs on **self-hosted** agents.
- [ ] Limit who can edit/create pipelines.
- [ ] Vet **extensions** and pin task versions.

## Summary

- Pipeline security protects secrets and controls access to powerful resources.
- Keep secrets in Key Vault-backed groups/secure files; never expose them to forks.
- Gate **protected resources** with checks and pipeline permissions.
- Be especially careful with **self-hosted agents** and **untrusted PRs**.

## Knowledge Check

1. Why should "make secrets available to builds of forks" stay off for public projects?
2. What does a **required template** (`extends`) check enforce?
3. Why are self-hosted agents riskier for untrusted PR builds?

➡️ Next: [10 - Agent Pool Administration](./10-Agent-Pool-Administration.md)
