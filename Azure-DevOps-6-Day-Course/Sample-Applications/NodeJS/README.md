# Contoso Tasks — Node.js Sample

A minimal Express API used by the Azure DevOps 6-Day Course.

## Requirements

- Node.js 20+ (uses the built-in test runner and global `fetch`).

## Run Locally

```bash
npm install      # or: npm ci
npm start        # starts on http://localhost:3000
```

Try the endpoints:

```bash
curl http://localhost:3000/
curl http://localhost:3000/health
curl http://localhost:3000/tasks
curl -X POST http://localhost:3000/tasks -H "Content-Type: application/json" -d '{"title":"My task"}'
```

## Run Tests

```bash
npm test
```

The tests use Node's built-in `node:test` runner (no extra dependencies) and exercise the `/health`, `/tasks` (GET/POST) endpoints.

## Project Structure

```
NodeJS/
├── app.js               # builds and exports the Express app
├── server.js            # starts the server (npm start)
├── app.test.js          # tests (npm test)
├── package.json
├── .gitignore
└── azure-pipelines.yml  # CI pipeline
```

## CI Pipeline

`azure-pipelines.yml` installs dependencies, runs tests, and publishes an artifact. See [Day 3](../../Day-03-Azure-Pipelines/) and the [Day 6 project](../../Day-06-Real-Time-Project/) for how to build and deploy it.

## Endpoints

| Method | Path | Description |
| ------ | ---- | ----------- |
| GET | `/` | Welcome message |
| GET | `/health` | `{ "status": "ok" }` |
| GET | `/tasks` | List tasks |
| POST | `/tasks` | Add a task (`{ "title": "..." }`) |
