import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    return app.test_client()


def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.get_json()["status"] == "ok"


def test_list_tasks(client):
    res = client.get("/tasks")
    assert res.status_code == 200
    data = res.get_json()
    assert isinstance(data, list)
    assert len(data) >= 1


def test_add_task(client):
    res = client.post("/tasks", json={"title": "Write tests"})
    assert res.status_code == 201
    data = res.get_json()
    assert data["title"] == "Write tests"
    assert data["done"] is False


def test_add_task_rejects_empty_title(client):
    res = client.post("/tasks", json={"title": ""})
    assert res.status_code == 400
