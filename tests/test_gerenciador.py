from fastapi import status
from fastapi.testclient import TestClient

from gerenciador_tarefas.gerenciador import TAREFAS, app


def test_list_task_status_200():
    client = TestClient(app)
    response = client.get("/tarefas")

    assert response.status_code == status.HTTP_200_OK


def test_list_taks_format_json():
    client = TestClient(app)
    response = client.get("/tarefas")
    assert response.headers["Content-Type"] == "application/json"


def test_list_task_list():
    client = TestClient(app)
    response = client.get("/tarefas")
    assert isinstance(response.json(), list)


def test_when_task_return_id():
    TAREFAS.append(
        {
            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "titulo": "titulo 1",
            "descricao": "descricao 1",
            "estado": "finalizado",
        }
    )
    client = TestClient(app)
    response = client.get("/tarefas")
    assert "id" in response.json().pop()
    TAREFAS.clear()


def test_when_task_return_title():
    TAREFAS.append(
        {
            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "titulo": "titulo 1",
            "descricao": "descricao 1",
            "estado": "finalizado",
        }
    )
    client = TestClient(app)
    response = client.get("/tarefas")
    assert "titulo" in response.json().pop()
    TAREFAS.clear()


def test_when_task_return_description():
    TAREFAS.append(
        {
            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "titulo": "titulo 1",
            "descricao": "descricao 1",
            "estado": "finalizado",
        }
    )

    client = TestClient(app)
    response = client.get("/tarefas")
    assert "descricao" in response.json().pop()
    TAREFAS.clear()


def test_when_task_return_state():
    TAREFAS.append(
        {
            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "titulo": "titulo 1",
            "descricao": "descricao 1",
            "estado": "finalizado",
        }
    )

    client = TestClient(app)
    response = client.get("/tarefas")
    assert "estado" in response.json().pop()
    TAREFAS.clear()


def test_resource_task_accept_post():

    client = TestClient(app)
    response = client.get("/tarefas")
    assert response.status_code != status.HTTP_405_METHOD_NOT_ALLOWED


def test_when_task_is_title():
    client = TestClient(app)
    response = client.post("tarefas", json={})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_title_caracters_content():
    client = TestClient(app)
    response = client.post("/tarefas", json={"title": 2 * "*"})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    response = client.post("/tarefas", json={"title": 51 * "*"})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def teste_title_content_description():
    client = TestClient(app)
    response = client.post("/tarefas", json={"title": "title"})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_description_max_140_caracters():
    client = TestClient(app)
    response = client.post(
        "/tarefas", json={"title": "title", "description": "*" * 141}
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_when_create_task_return_task():
    client = TestClient(app)
    task_esperada = {"title": "title", "description": "description"}
    response = client.post("/tarefas", json=task_esperada)
    task_created = response.json()
    assert task_created["title"] == task_esperada["title"]
    assert task_created["description"] == task_esperada["description"]
    TAREFAS.clear()


def test_when_create_new_task_state_finished_or_not():
    client = TestClient(app)
    task = {"title": "title", "description": "description"}
    response = client.post("/tarefas", json=task)
    assert response.json()["state"] == "not finished"
    TAREFAS.clear()


def test_whe_create_return_state_201():
    client = TestClient(app)
    task = {"title": "title", "description": "description"}
    response = client.post("/tarefas", json=task)
    assert response.status_code == status.HTTP_201_CREATED
    TAREFAS.clear()


def test_when_create_task_existing():
    client = TestClient(app)
    task = {"title": "title", "description": "description"}
    client.post("/tarefas", json=task)
    assert len(TAREFAS) == 1
    TAREFAS.clear()
