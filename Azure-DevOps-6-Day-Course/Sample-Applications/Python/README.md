# Contoso Tasks — Python Sample

A minimal Flask API used by the Azure DevOps 6-Day Course.

## Requirements

- Python 3.10+ (3.12 recommended).

## Run Locally

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py                       # starts on http://localhost:5000
```

Try the endpoints:

```bash
curl http://localhost:5000/
curl http://localhost:5000/health
curl http://localhost:5000/tasks
curl -X POST http://localhost:5000/tasks -H "Content-Type: application/json" -d '{"title":"My task"}'
```

## Run Tests

```bash
pip install pytest
pytest
```

## Project Structure

```
Python/
├── app.py               # Flask app factory (create_app)
├── test_app.py          # pytest tests
├── requirements.txt
├── .gitignore
└── azure-pipelines.yml  # CI pipeline (publishes test results)
```

## CI Pipeline

`azure-pipelines.yml` installs dependencies, runs `pytest` with coverage, and publishes test results. See [Day 3](../../Day-03-Azure-Pipelines/) and the [Day 6 project](../../Day-06-Real-Time-Project/).

## Endpoints

| Method | Path | Description |
| ------ | ---- | ----------- |
| GET | `/` | Welcome message |
| GET | `/health` | `{ "status": "ok" }` |
| GET | `/tasks` | List tasks |
| POST | `/tasks` | Add a task (`{ "title": "..." }`) |
