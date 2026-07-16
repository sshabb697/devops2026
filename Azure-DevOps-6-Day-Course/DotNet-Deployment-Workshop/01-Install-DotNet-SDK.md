# 01 - Install .NET SDK

## Overview

Before you can build a web app or run a pipeline, you need the **.NET SDK** on your machine. The SDK includes the compiler, runtime, and CLI tools (`dotnet`).

> **Analogy:** The .NET SDK is like having Node.js + npm, or Python + pip — it is everything you need to create, build, and run .NET applications locally.

## What You Are Installing

| Component | Purpose |
| --------- | ------- |
| **.NET SDK** | Build and run apps; includes CLI (`dotnet`) |
| **.NET Runtime** | Runs compiled apps (included with SDK) |

This workshop uses **.NET 8** (LTS — long-term support).

---

## Step 1 — Download

1. Go to [https://dotnet.microsoft.com/download](https://dotnet.microsoft.com/download).
2. Download **.NET 8 SDK** for your operating system (Windows, macOS, or Linux).
3. Run the installer and accept the defaults.

### Windows (alternative — winget)

```powershell
winget install Microsoft.DotNet.SDK.8
```

### macOS (alternative — Homebrew)

```bash
brew install dotnet@8
```

---

## Step 2 — Verify Installation

Open a **new** terminal (important — restart so `PATH` updates) and run:

```powershell
dotnet --version
```

You should see something like `8.0.xxx`.

```powershell
dotnet --info
```

This prints installed SDKs and runtimes. Look for `.NET SDK 8.x` in the output.

✅ **Checkpoint:** `dotnet --version` returns `8.0.x` without errors.

---

## Step 3 — Understand the CLI

| Command | What it does |
| ------- | ------------ |
| `dotnet --version` | Show SDK version |
| `dotnet --info` | Show all installed SDKs and runtimes |
| `dotnet new list` | List project templates you can scaffold |
| `dotnet new webapi -n MyApp` | Create a new Web API project |
| `dotnet build` | Compile the project |
| `dotnet run` | Build and run (development) |
| `dotnet test` | Run unit tests |
| `dotnet publish` | Create a deployable output (artifact) |

You will use all of these in the next lessons.

---

## Step 4 — (Optional) Install VS Code Extensions

If you use Visual Studio Code:

1. Install the [C# Dev Kit](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csdevkit) extension (or **C#** by Microsoft).
2. Open the Command Palette (`Ctrl+Shift+P`) → **.NET: New Project** to scaffold from the IDE.

---

## Troubleshooting

| Problem | Fix |
| ------- | --- |
| `'dotnet' is not recognized` | Close and reopen the terminal; reinstall SDK; check PATH |
| Wrong version shown | Multiple SDKs installed — `dotnet --list-sdks` shows all; 8.x should be used for this course |
| Permission errors on Linux | Do not use `sudo` with `dotnet new` — install SDK for your user |

---

## Summary

- Install the **.NET 8 SDK** from [dotnet.microsoft.com](https://dotnet.microsoft.com/download).
- Verify with `dotnet --version`.
- The `dotnet` CLI is how you create, build, run, test, and publish apps — locally and in pipelines.

## Knowledge Check

1. What is the difference between the SDK and the Runtime?
2. Which command shows all installed SDK versions?
3. Why do you need to open a new terminal after installing?

➡️ Next: [02 - Create Web App & Run Locally](./02-Create-WebApp-and-Run-Locally.md)
