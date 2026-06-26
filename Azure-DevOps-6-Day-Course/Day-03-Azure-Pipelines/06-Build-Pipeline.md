# 06 - Build Pipeline

## Overview

A **build pipeline** (the CI part of CI/CD) compiles your source, runs tests, and produces **artifacts** ready for deployment. This lesson shows complete, real build pipelines for several languages so you can adapt one to your project.

## Anatomy of a Build Pipeline

A typical CI build does:

1. **Trigger** on push/PR.
2. **Checkout** the code (automatic).
3. **Restore** dependencies.
4. **Build/compile**.
5. **Test** (unit tests, optionally with coverage).
6. **Publish** test results.
7. **Package** and **publish artifacts**.

## .NET Build Pipeline

```yaml
trigger:
  - main

pool:
  vmImage: 'ubuntu-latest'

variables:
  buildConfiguration: 'Release'

steps:
  - task: UseDotNet@2
    inputs:
      packageType: 'sdk'
      version: '8.x'

  - task: DotNetCoreCLI@2
    displayName: 'Restore'
    inputs:
      command: 'restore'
      projects: '**/*.csproj'

  - task: DotNetCoreCLI@2
    displayName: 'Build'
    inputs:
      command: 'build'
      projects: '**/*.csproj'
      arguments: '--configuration $(buildConfiguration) --no-restore'

  - task: DotNetCoreCLI@2
    displayName: 'Test'
    inputs:
      command: 'test'
      projects: '**/*Tests.csproj'
      arguments: '--configuration $(buildConfiguration) --collect "Code coverage"'

  - task: DotNetCoreCLI@2
    displayName: 'Publish'
    inputs:
      command: 'publish'
      publishWebProjects: true
      arguments: '--configuration $(buildConfiguration) --output $(Build.ArtifactStagingDirectory)'

  - task: PublishBuildArtifacts@1
    displayName: 'Publish artifact'
    inputs:
      PathtoPublish: '$(Build.ArtifactStagingDirectory)'
      ArtifactName: 'drop'
```

## Node.js Build Pipeline

```yaml
trigger:
  - main

pool:
  vmImage: 'ubuntu-latest'

steps:
  - task: NodeTool@0
    inputs:
      versionSpec: '20.x'
    displayName: 'Install Node.js'

  - script: npm ci
    displayName: 'Install dependencies'

  - script: npm test
    displayName: 'Run tests'

  - script: npm run build
    displayName: 'Build'

  - task: PublishBuildArtifacts@1
    inputs:
      PathtoPublish: 'dist'
      ArtifactName: 'drop'
```

## Python Build Pipeline

```yaml
trigger:
  - main

pool:
  vmImage: 'ubuntu-latest'

steps:
  - task: UsePythonVersion@0
    inputs:
      versionSpec: '3.12'

  - script: |
      python -m pip install --upgrade pip
      pip install -r requirements.txt
    displayName: 'Install dependencies'

  - script: |
      pip install pytest pytest-cov
      pytest --junitxml=test-results.xml --cov=. --cov-report=xml
    displayName: 'Run tests'

  - task: PublishTestResults@2
    inputs:
      testResultsFiles: 'test-results.xml'
      testRunTitle: 'Python tests'
```

## Java (Maven) Build Pipeline

```yaml
trigger:
  - main

pool:
  vmImage: 'ubuntu-latest'

steps:
  - task: Maven@4
    inputs:
      mavenPomFile: 'pom.xml'
      goals: 'package'
      publishJUnitResults: true
      testResultsFiles: '**/surefire-reports/TEST-*.xml'
      javaHomeOption: 'JDKVersion'
      jdkVersionOption: '17'

  - task: CopyFiles@2
    inputs:
      contents: '**/target/*.jar'
      targetFolder: '$(Build.ArtifactStagingDirectory)'

  - task: PublishBuildArtifacts@1
    inputs:
      PathtoPublish: '$(Build.ArtifactStagingDirectory)'
      ArtifactName: 'drop'
```

## Publishing Test Results & Coverage

Use `PublishTestResults@2` and `PublishCodeCoverageResults@2` so results appear in the run summary's **Tests** and **Code Coverage** tabs. This powers quality gates and dashboards.

## Useful Predefined Variables in Builds

| Variable | Use |
| -------- | --- |
| `$(Build.ArtifactStagingDirectory)` | Where to stage files to publish |
| `$(Build.SourcesDirectory)` | Where the repo is checked out |
| `$(Build.BuildId)` | Unique build number |
| `$(Build.SourceBranch)` | Triggering branch |

## Summary

- A build pipeline restores, builds, tests, and publishes artifacts.
- Use the language-appropriate tasks (`DotNetCoreCLI@2`, `NodeTool@0`, `Maven@4`, `UsePythonVersion@0`).
- Publish artifacts with `PublishBuildArtifacts@1` (or `PublishPipelineArtifact@1`).
- Publish test results/coverage to enable quality reporting.

## Knowledge Check

1. What are the typical phases of a build pipeline?
2. Which task publishes build outputs as an artifact?
3. Where should you stage files you intend to publish?

➡️ Next: [07 - Release Pipeline Concept](./07-Release-Pipeline-Concept.md)
