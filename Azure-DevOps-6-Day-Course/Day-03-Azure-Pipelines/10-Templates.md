# 10 - Templates

## Overview

**Templates** let you define reusable pipeline content once and reference it from many pipelines. They are the key to keeping pipelines DRY (don't repeat yourself), enforcing standards, and managing complexity across teams.

## Why Templates?

- **Reuse** common steps/jobs/stages across many pipelines.
- **Standardize** — enforce a consistent build/test/deploy pattern.
- **Maintainability** — fix or improve logic in one place.
- **Parameterize** — customize behavior per use with inputs.

## Types of Templates

You can templatize at any level:

| Template type | Reuses |
| ------------- | ------ |
| **Steps template** | A set of steps |
| **Jobs template** | One or more jobs |
| **Stages template** | One or more stages |
| **Variables template** | A block of variables |

## A Steps Template Example

Create `templates/build-steps.yml`:

```yaml
# templates/build-steps.yml
parameters:
  - name: buildConfiguration
    type: string
    default: 'Release'

steps:
  - script: echo "Restoring..."
    displayName: 'Restore'
  - script: echo "Building in ${{ parameters.buildConfiguration }}"
    displayName: 'Build'
  - script: echo "Testing..."
    displayName: 'Test'
```

Use it in the main pipeline:

```yaml
# azure-pipelines.yml
trigger:
  - main

pool:
  vmImage: 'ubuntu-latest'

steps:
  - template: templates/build-steps.yml
    parameters:
      buildConfiguration: 'Debug'
```

## Parameters

Parameters make templates flexible. They support types and defaults:

```yaml
parameters:
  - name: vmImage
    type: string
    default: 'ubuntu-latest'
  - name: runTests
    type: boolean
    default: true
  - name: regions
    type: object
    default: [ 'eastus', 'westus' ]
```

Parameters are resolved at **compile time** (use `${{ parameters.x }}`), which means you can use them in conditionals to include/exclude content:

```yaml
steps:
  - ${{ if eq(parameters.runTests, true) }}:
      - script: echo "Running tests"
```

## A Jobs Template Example

```yaml
# templates/build-job.yml
parameters:
  - name: name
    type: string
  - name: vmImage
    type: string
    default: 'ubuntu-latest'

jobs:
  - job: ${{ parameters.name }}
    pool:
      vmImage: ${{ parameters.vmImage }}
    steps:
      - script: echo "Building ${{ parameters.name }}"
```

```yaml
# azure-pipelines.yml
jobs:
  - template: templates/build-job.yml
    parameters:
      name: LinuxBuild
      vmImage: 'ubuntu-latest'
  - template: templates/build-job.yml
    parameters:
      name: WindowsBuild
      vmImage: 'windows-latest'
```

## Templates from Another Repository

Share templates across projects by referencing an external repo:

```yaml
resources:
  repositories:
    - repository: templates
      type: git
      name: SharedProject/pipeline-templates
      ref: refs/heads/main

stages:
  - template: build-stage.yml@templates
```

## Template Security: `extends`

For governance, a pipeline can be required to **extend** an approved template, which can restrict what steps run (used with protected resources). This enforces organizational policy.

```yaml
extends:
  template: secure-pipeline.yml@templates
  parameters:
    project: myapp
```

## Best Practices

- Keep templates in a `templates/` folder or a dedicated repo.
- Parameterize thoughtfully — enough flexibility, not too much.
- Version shared template repos (use `ref:` to pin).
- Document each template's parameters.

## Summary

- Templates reuse steps, jobs, stages, or variables across pipelines.
- Reference with `template:` and pass `parameters:`.
- Parameters resolve at compile time (`${{ }}`) and enable conditionals.
- Share templates across projects via `resources.repositories`.

## Knowledge Check

1. What are the four kinds of templates by reuse level?
2. When are template parameters resolved — compile time or runtime?
3. How do you reference a template stored in another repository?

➡️ Next: [11 - Artifacts](./11-Artifacts.md)
