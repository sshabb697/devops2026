# 02 - Create Web App & Run Locally

## Overview

Now you will create a small **ASP.NET Core Web API** and run it on your machine. This is the same app the CI/CD pipeline will later build and deploy to Azure.

> **Goal:** Open a browser, hit `http://localhost:5000/health`, and see `{ "status": "ok" }`.

---

## Choose Your Path

| Path | Best for |
| ---- | -------- |
| **A — Build from scratch** | Students new to .NET who want to see how the app is created |
| **B — Use the course sample** | Faster start; copy the ready-made [Contoso Tasks](../Sample-Applications/DotNet/) app |

---

## Path A — Build from Scratch

### Step 1 — Create a workspace folder

```powershell
mkdir C:\devops-labs\ContosoTasks
cd C:\devops-labs\ContosoTasks
```

> On macOS/Linux use `~/devops-labs/ContosoTasks` instead.

### Step 2 — Scaffold the solution

```powershell
dotnet new sln -n ContosoTasks
dotnet new webapi -n ContosoTasks -o src/ContosoTasks --use-minimal-apis
dotnet sln add src/ContosoTasks/ContosoTasks.csproj
```

### Step 3 — Replace `Program.cs` with the course API

Open `src/ContosoTasks/Program.cs` and replace its contents with:

```csharp
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

var tasks = new List<TaskItem> { new(1, "Learn Azure DevOps", false) };
var nextId = 2;

app.MapGet("/", () => Results.Ok(new { message = "Welcome to the Contoso Tasks API" }));
app.MapGet("/health", () => Results.Ok(new { status = "ok" }));
app.MapGet("/tasks", () => Results.Ok(tasks));

app.MapPost("/tasks", (NewTask input) =>
{
    var title = (input.Title ?? string.Empty).Trim();
    if (string.IsNullOrEmpty(title))
        return Results.BadRequest(new { error = "title is required" });

    var task = new TaskItem(nextId++, title, false);
    tasks.Add(task);
    return Results.Created($"/tasks/{task.Id}", task);
});

app.Run();

public record TaskItem(int Id, string Title, bool Done);
public record NewTask(string? Title);
public partial class Program { }
```

### Step 4 — (Optional) Add unit tests

```powershell
dotnet new xunit -n ContosoTasks.Tests -o tests/ContosoTasks.Tests
dotnet add tests/ContosoTasks.Tests/ContosoTasks.Tests.csproj reference src/ContosoTasks/ContosoTasks.csproj
dotnet add tests/ContosoTasks.Tests package Microsoft.AspNetCore.Mvc.Testing
dotnet sln add tests/ContosoTasks.Tests/ContosoTasks.Tests.csproj
```

Add a simple test in `tests/ContosoTasks.Tests/ApiTests.cs` (or skip tests for now and add them before lesson 05).

---

## Path B — Use the Course Sample

```powershell
# Copy the sample from this repo into your workspace
mkdir C:\devops-labs
xcopy /E /I "path\to\repo\Azure-DevOps-6-Day-Course\Sample-Applications\DotNet" C:\devops-labs\ContosoTasks
cd C:\devops-labs\ContosoTasks
```

On macOS/Linux:

```bash
cp -r Azure-DevOps-6-Day-Course/Sample-Applications/DotNet ~/devops-labs/ContosoTasks
cd ~/devops-labs/ContosoTasks
```

---

## Run the App Locally

### Step 1 — Restore and run

From the solution root (`ContosoTasks/` folder containing `ContosoTasks.sln`):

```powershell
dotnet restore
cd src/ContosoTasks
dotnet run
```

The console prints URLs like:

```
info: Microsoft.Hosting.Lifetime[14]
      Now listening on: http://localhost:5000
```

### Step 2 — Test in the browser or terminal

**Browser:** open [http://localhost:5000/health](http://localhost:5000/health)

**PowerShell:**

```powershell
Invoke-RestMethod http://localhost:5000/health
# status
# ------
# ok
```

**curl (macOS/Linux/Git Bash):**

```bash
curl http://localhost:5000/
curl http://localhost:5000/health
curl http://localhost:5000/tasks
curl -X POST http://localhost:5000/tasks -H "Content-Type: application/json" -d "{\"title\":\"My first task\"}"
```

✅ **Checkpoint:** `/health` returns `{ "status": "ok" }`.

Press `Ctrl+C` in the terminal to stop the app.

---

## What Just Happened? (Visual)

```
  YOUR LAPTOP
  ┌─────────────────────────────────────────────────────────┐
  │  Source code (Program.cs, .csproj)                    │
  │         │                                               │
  │         ▼  dotnet run                                   │
  │  ┌──────────────┐      HTTP       ┌─────────────────┐  │
  │  │ Kestrel web  │ ◄────────────── │ Browser / curl  │  │
  │  │ server       │   localhost:5000│                 │  │
  │  │ :5000        │                 └─────────────────┘  │
  │  └──────────────┘                                       │
  └─────────────────────────────────────────────────────────┘

  Development mode: code runs from source, hot reload available.
  NOT what you ship to production — that is a published artifact (lesson 03).
```

---

## Project Structure

```
ContosoTasks/
├── ContosoTasks.sln              # Solution file (groups projects)
├── src/
│   └── ContosoTasks/
│       ├── ContosoTasks.csproj   # Project file (dependencies, target framework)
│       └── Program.cs            # App entry point + API routes
└── tests/                        # (optional) unit tests
    └── ContosoTasks.Tests/
```

| File | Role |
| ---- | ---- |
| `.sln` | Groups one or more `.csproj` files |
| `.csproj` | Defines target framework (`net8.0`), packages |
| `Program.cs` | Application code — routes, logic |

---

## Summary

- You created (or copied) a minimal ASP.NET Core Web API.
- `dotnet run` starts a local web server on `localhost`.
- The same endpoints (`/`, `/health`, `/tasks`) will run in Azure after deployment.

## Knowledge Check

1. Which command starts the app in development mode?
2. What URL would you use to check if the app is healthy?
3. What is the difference between `dotnet build` and `dotnet run`?

➡️ Next: [03 - Build & Publish Artifact Locally](./03-Build-Publish-Artifact-Locally.md)
