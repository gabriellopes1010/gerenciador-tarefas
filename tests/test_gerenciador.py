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
