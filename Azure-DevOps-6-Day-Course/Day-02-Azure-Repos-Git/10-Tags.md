# 10 - Tags

## Overview

A **tag** is a named pointer to a specific commit. Unlike branches, tags don't move — they permanently mark a point in history. Their most common use is to mark **releases** (e.g., `v1.0.0`).

## Branch vs Tag

| | Branch | Tag |
| --- | ------ | --- |
| Moves with new commits? | Yes | No (fixed) |
| Purpose | Ongoing development | Mark a specific point (release) |
| Example | `feature/login` | `v2.1.0` |

## Types of Tags

### Lightweight tag
Just a name pointing to a commit — no extra metadata.

```bash
git tag v1.0.0
```

### Annotated tag (recommended for releases)
A full object storing the tagger, date, and a message (and can be GPG-signed).

```bash
git tag -a v1.0.0 -m "Release version 1.0.0"
```

## Common Tag Commands

```bash
git tag                          # list all tags
git tag -l "v1.*"                # filter tags by pattern
git show v1.0.0                  # show tag + commit details

# Tag a specific past commit
git tag -a v0.9.0 <commit-sha> -m "Beta release"

# Push tags to Azure Repos (tags are NOT pushed by default)
git push origin v1.0.0           # push a single tag
git push origin --tags           # push all tags

# Delete tags
git tag -d v1.0.0                # delete local tag
git push origin --delete v1.0.0  # delete remote tag
```

> **Important:** `git push` does **not** push tags automatically. You must push them explicitly.

## Semantic Versioning (SemVer)

A widely used scheme for naming version tags: `MAJOR.MINOR.PATCH`.

| Part | Increment when... | Example |
| ---- | ----------------- | ------- |
| **MAJOR** | You make breaking changes | `1.0.0 → 2.0.0` |
| **MINOR** | You add backward-compatible features | `1.0.0 → 1.1.0` |
| **PATCH** | You make backward-compatible fixes | `1.0.0 → 1.0.1` |

Pre-release/build suffixes: `2.0.0-beta.1`, `1.4.0+build.456`.

## Tags in Azure Repos

- View tags under **Repos → Tags**.
- Create a tag from the web UI on any commit.
- Manage **tag permissions** (who can create/delete tags) under repo security.
- Pipelines can be **triggered by tags** (e.g., deploy when a `v*` tag is pushed) — useful for release automation.

## Using Tags in Pipelines

```yaml
trigger:
  tags:
    include:
      - v*
```

This runs the pipeline only when a tag like `v1.2.0` is pushed — a clean way to trigger production deployments.

## Best Practices

- Use **annotated** tags for releases (they carry metadata).
- Follow **Semantic Versioning**.
- Tag the exact commit that was built/released for traceability.
- Remember to **push** your tags.

## Summary

- A tag is a fixed, named pointer to a commit, mainly used to mark releases.
- Prefer **annotated** tags; follow **SemVer** (`MAJOR.MINOR.PATCH`).
- Tags aren't pushed automatically — use `git push origin --tags`.
- Tags can trigger release pipelines.

## Knowledge Check

1. What is the key difference between a branch and a tag?
2. When would you increment the MAJOR version in SemVer?
3. How do you push all local tags to Azure Repos?

➡️ Next: [11 - .gitignore](./11-GitIgnore.md)
