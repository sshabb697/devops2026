# Sample Applications

Small, self-contained demo applications used by the course labs (especially Days 3 and 6). Each implements the same tiny **Tasks API** — a few HTTP endpoints plus a `/health` check and unit tests — so you can practice building and deploying in your language of choice.

| App | Stack | Build/Test | Pipeline |
| --- | ----- | ---------- | -------- |
| [DotNet](./DotNet/) | ASP.NET Core (.NET 8) | `dotnet build` / `dotnet test` | `azure-pipelines.yml` |
| [Java](./Java/) | Spring Boot (Maven, JDK 17) | `mvn package` | `azure-pipelines.yml` |
| [NodeJS](./NodeJS/) | Express (Node 20) | `npm test` | `azure-pipelines.yml` |
| [Python](./Python/) | Flask (Python 3.12) | `pytest` | `azure-pipelines.yml` |

## Common Endpoints

Every app exposes:

| Method | Path | Description |
| ------ | ---- | ----------- |
| `GET` | `/` | Welcome message |
| `GET` | `/health` | Health check → `{ "status": "ok" }` |
| `GET` | `/tasks` | List tasks |
| `POST` | `/tasks` | Add a task |

## How to Use

1. Pick an app and read its `README.md` for run instructions.
2. For **.NET**, follow the [.NET Deployment Workshop](../DotNet-Deployment-Workshop/) — local build → artifact → Azure Repos → CI/CD → App Service.
3. Push the app to an Azure Repos repository.
4. Use its `azure-pipelines.yml` (or the samples in [Day 3 YAML](../Day-03-Azure-Pipelines/YAML/)) to build it.
5. Follow the [Day 6 Real-Time Project](../Day-06-Real-Time-Project/) to deploy it.

> These apps are intentionally minimal — the focus is the **DevOps workflow**, not the application code.
