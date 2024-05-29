
from pydantic import BaseModel


class AlunoResponse(BaseModel):
    id: int
    nome: str
    cpf: str
    rg: str

    class Config:
        from_attributes = True


class AlunoRequest(BaseModel):
    nome: str
    cpf: str
    rg: str