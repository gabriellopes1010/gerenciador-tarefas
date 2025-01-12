from enum import Enum
from uuid import UUID
from pydantic import BaseModel, Field


class StatesPossibles(str, Enum):
    finished = "finished"
    not_finished = "not finished"


class TarefaEntrada(BaseModel):
    title: str = Field(min_length=3, max_length=50)
    description: str = Field(max_length=140)
    state: StatesPossibles = StatesPossibles.not_finished


class Tarefa(TarefaEntrada):
    id: UUID
