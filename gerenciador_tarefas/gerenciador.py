import fastapi
from uuid import uuid4
from fastapi import status
from core.gerenciador_tarefas.models import TarefaEntrada, Tarefa

app = fastapi.FastAPI()

TAREFAS = [
    {
        "id": "1",
        "titulo": "fazer compras",
        "descrição": "comprar leite e ovos",
        "estado": "não finalizado",
    },
    {
        "id": "2",
        "titulo": "levar o cachorro para tosar",
        "descrição": "está muito peludo",
        "estado": "não finalizado",
    },
    {
        "id": "3",
        "titulo": "lavar roupas",
        "descrição": "estão sujas",
        "estado": "não finalizado",
    },
]


@app.get("/tarefas")
def listar():
    return TAREFAS


@app.post("/tarefas", response_model=Tarefa, status_code=status.HTTP_201_CREATED)
def criar(tarefa: TarefaEntrada):
    new_task = tarefa.dict()
    new_task.update({"id": uuid4()})
    TAREFAS.append(new_task)
    return new_task
