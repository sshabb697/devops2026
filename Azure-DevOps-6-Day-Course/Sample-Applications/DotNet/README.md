# Contoso Tasks — .NET Sample

A minimal ASP.NET Core (.NET 8) minimal-API used by the Azure DevOps 6-Day Course.

## Requirements

- [.NET SDK 8.0+](https://dotnet.microsoft.com/download).

## Run Locally

```bash
cd src/ContosoTasks
dotnet run
# Listens on http://localhost:5000 (or the URL printed in the console)
```

Try the endpoints:

```bash
curl http://localhost:5000/
curl http://localhost:5000/health
curl http://localhost:5000/tasks
curl -X POST http://localhost:5000/tasks -H "Content-Type: application/json" -d '{"title":"My task"}'
```

## Build & Test

```bash
# from the DotNet/ folder
dotnet restore
dotnet build --configuration Release
dotnet test
```

## Project Structure

```
DotNet/
├── src/ContosoTasks/
│   ├── ContosoTasks.csproj
│   └── Program.cs              # minimal API + records
├── tests/ContosoTasks.Tests/
│   ├── ContosoTasks.Tests.csproj
│   └── ApiTests.cs             # xUnit + WebApplicationFactory
├── .gitignore
├── azure-pipelines.yml         # CI only: restore → build → test → publish artifact
└── azure-pipelines-full.yml    # CI + CD: deploy to Azure App Service
```

## CI Pipeline

`azure-pipelines.yml` restores, builds, tests, publishes the web app, and uploads an artifact. See [Day 3](../../Day-03-Azure-Pipelines/) and the [Day 6 project](../../Day-06-Real-Time-Project/).

## Full CI/CD (Azure App Service)

`azure-pipelines-full.yml` adds a **Deploy** stage that publishes to **Azure App Service** via `AzureWebApp@1`. Follow the step-by-step [.NET Deployment Workshop](../../DotNet-Deployment-Workshop/).

## Endpoints

| Method | Path | Description |
| ------ | ---- | ----------- |
| GET | `/` | Welcome message |
| GET | `/health` | `{ "status": "ok" }` |
| GET | `/tasks` | List tasks |
| POST | `/tasks` | Add a task (`{ "title": "..." }`) |
