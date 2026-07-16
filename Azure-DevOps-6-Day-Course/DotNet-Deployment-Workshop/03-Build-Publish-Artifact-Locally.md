# 03 - Build & Publish Artifact Locally

## Overview

Running with `dotnet run` is for **development**. To deploy an app, you need a **build artifact** — a self-contained folder (or ZIP) that Azure App Service can run without your source code or SDK.

> **Key concept:** An **artifact** is the output of a build that you **deploy**. In .NET, that is the `publish` folder (often zipped).

This lesson mirrors what the CI pipeline will do automatically in lesson 05.

---

## Development vs Production Output

```
  dotnet run                    dotnet publish
  ──────────                    ────────────────
  Runs from source              Produces deployable files
  Needs SDK installed           Runtime on server is enough
  Fast iteration                Optimized, release build
  localhost only                Ready for App Service / IIS / containers
```

---

## Step 1 — Build (Compile)

From the solution root:

```powershell
cd C:\devops-labs\ContosoTasks
dotnet restore
dotnet build --configuration Release
```

✅ **Checkpoint:** Build succeeds with `0 Error(s)`.

---

## Step 2 — Run Tests (Optional but Recommended)

```powershell
dotnet test --configuration Release
```

If you skipped tests in lesson 02, you can skip this step — but add tests before lesson 05 so the CI pipeline has something to run.

---

## Step 3 — Publish (Generate the Artifact)

```powershell
dotnet publish src/ContosoTasks/ContosoTasks.csproj `
  --configuration Release `
  --output ./publish
```

On macOS/Linux (single line):

```bash
dotnet publish src/ContosoTasks/ContosoTasks.csproj \
  --configuration Release \
  --output ./publish
```

This creates a `publish/` folder with everything needed to run the app.

### Inspect the output

```powershell
dir .\publish
```

You should see:

```
publish/
├── ContosoTasks.dll          # Compiled application
├── ContosoTasks.exe          # (Windows) entry executable
├── appsettings.json
├── web.config                # (Windows/IIS hosting)
├── *.dll                     # Dependencies
└── ...
```

| File | Purpose |
| ---- | ------- |
| `ContosoTasks.dll` | Your compiled app |
| `*.dll` | .NET and NuGet dependencies |
| `appsettings.json` | Configuration |
| `web.config` | IIS/App Service hosting hints |

---

## Step 4 — Run the Published App Locally

Prove the artifact works **without** `dotnet run` from source:

```powershell
cd publish
dotnet ContosoTasks.dll
```

Open [http://localhost:5000/health](http://localhost:5000/health) again.

✅ **Checkpoint:** The published artifact runs and `/health` still returns `ok`.

Press `Ctrl+C`, then `cd ..` back to the solution root.

---

## Step 5 — Create a ZIP (What Pipelines Ship)

Azure App Service deploys often use a **ZIP package**. Create one manually to see what the pipeline produces:

**PowerShell:**

```powershell
Compress-Archive -Path .\publish\* -DestinationPath .\ContosoTasks.zip -Force
dir ContosoTasks.zip
```

**macOS/Linux:**

```bash
cd publish && zip -r ../ContosoTasks.zip . && cd ..
ls -la ContosoTasks.zip
```

✅ **Checkpoint:** `ContosoTasks.zip` exists and is several MB (not empty).

---

## Visual — From Source to Artifact

```
  SOURCE                          BUILD ARTIFACT
  ──────                          ──────────────

  Program.cs                      publish/
  ContosoTasks.csproj    ──────►   ├── ContosoTasks.dll
  appsettings.json       dotnet    ├── appsettings.json
                         publish   ├── web.config
                                   └── (all dependencies)

                                           │
                                           ▼
                                   ContosoTasks.zip  ──►  Deploy to Azure App Service
```

---

## What the CI Pipeline Will Do (Preview)

In lesson 05, Azure Pipelines runs the same commands on a **Microsoft-hosted agent**:

| Local (you) | Pipeline (agent) |
| ----------- | ---------------- |
| `dotnet restore` | `DotNetCoreCLI@2` restore |
| `dotnet build -c Release` | `DotNetCoreCLI@2` build |
| `dotnet test` | `DotNetCoreCLI@2` test |
| `dotnet publish -o ./publish` | `DotNetCoreCLI@2` publish + `zipAfterPublish: true` |
| `ContosoTasks.zip` on disk | `PublishPipelineArtifact@1` → artifact named `drop` |

---

## Add to `.gitignore`

Do **not** commit build output. Create or update `.gitignore` in the solution root:

```gitignore
bin/
obj/
publish/
*.zip
.vs/
```

You will push only **source code** to Git; the pipeline generates artifacts in the cloud.

---

## Summary

- `dotnet build` compiles; `dotnet publish` creates a **deployable artifact**.
- The `publish/` folder contains DLLs and config — that is what App Service runs.
- ZIP the publish folder — that is what the pipeline uploads as the `drop` artifact.

## Knowledge Check

1. Why is `dotnet publish` needed instead of copying `.cs` source files?
2. What files would you expect inside the `publish` folder?
3. Why should `publish/` and `*.zip` be in `.gitignore`?

➡️ Next: [04 - Push to Azure Repos](./04-Push-to-Azure-Repos.md)
