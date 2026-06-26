# 08 - Variables

## Overview

**Variables** let you store and reuse values in a pipeline — configuration, paths, flags, secrets — instead of hard-coding them. They make pipelines flexible and DRY (don't repeat yourself).

## Defining Variables

### Inline (pipeline-level)
```yaml
variables:
  buildConfiguration: 'Release'
  appName: 'myapp'

steps:
  - script: echo "Building $(appName) in $(buildConfiguration)"
```

### Name/value list with more scope
```yaml
variables:
  - name: buildConfiguration
    value: 'Release'
  - group: 'shared-settings'        # a variable group (next lesson)
```

### Stage- or job-scoped
```yaml
stages:
  - stage: Build
    variables:
      stageVar: 'only-in-build'
    jobs:
      - job: A
        variables:
          jobVar: 'only-in-job-A'
```

## Referencing Variables — Three Syntaxes

| Syntax | Name | When it's expanded | Use for |
| ------ | ---- | ------------------ | ------- |
| `$(var)` | Macro | At runtime, before the step runs | Most cases |
| `${{ var }}` | Template expression | At **compile** time (before run) | Conditionals, templates |
| `$[ var ]` | Runtime expression | At runtime (whole expression) | `condition`, dependency results |

```yaml
steps:
  - script: echo "$(buildConfiguration)"          # macro
  - ${{ if eq(parameters.debug, true) }}:          # template expression
      - script: echo "debug mode"
  - script: echo "ran"
    condition: eq(variables['Build.Reason'], 'PullRequest')   # runtime
```

## Secret Variables

Mark sensitive values as **secret** so they're masked in logs and not exposed.

- **In the UI:** Pipeline → Edit → **Variables** → add variable → check **Keep this value secret**.
- Secrets are **not** decrypted into `$(var)` automatically for scripts; map them explicitly via `env`:

```yaml
steps:
  - script: echo "Using the secret"
    env:
      MY_SECRET: $(mySecretVar)     # mapped into an environment variable
```

> Never `echo` a secret directly or store secrets in YAML in plain text. Use secret variables, variable groups linked to Key Vault, or secure files.

## Setting Variables at Runtime (Output Variables)

A step can set a variable for later steps/jobs using a logging command:

```yaml
steps:
  - bash: echo "##vso[task.setvariable variable=version]1.2.3"
    name: setVarStep
  - script: echo "Version is $(version)"
```

To pass between jobs, mark it `isOutput=true` and reference via dependencies:

```yaml
- bash: echo "##vso[task.setvariable variable=ver;isOutput=true]1.2.3"
  name: produce
# in another job:
# variables:
#   v: $[ dependencies.JobA.outputs['produce.ver'] ]
```

## Predefined (System) Variables

Azure provides many built-in variables:

| Variable | Description |
| -------- | ----------- |
| `Build.BuildId` | Unique build ID |
| `Build.SourceBranch` | Triggering branch ref |
| `Build.SourceVersion` | Commit SHA |
| `Build.Reason` | Why the build ran (Manual, IndividualCI, PullRequest...) |
| `Agent.OS` | Agent operating system |
| `System.DefaultWorkingDirectory` | Working directory |

## Variable Precedence (highest wins)

1. Variables set at queue time (UI, when running).
2. Variables in the YAML at job/stage/pipeline scope.
3. Variable group / Key Vault variables.

## Summary

- Variables store reusable values; define them at pipeline/stage/job scope.
- Reference with `$(macro)`, `${{ template }}`, or `$[ runtime ]` depending on timing.
- Use **secret** variables for sensitive data and map them via `env`.
- Many **predefined** variables are available automatically.

## Knowledge Check

1. What's the difference between `$(var)` and `${{ var }}`?
2. How do you keep a variable's value out of the logs?
3. Which predefined variable holds the commit SHA?

➡️ Next: [09 - Variable Groups](./09-Variable-Groups.md)
