
from pydantic import BaseModel

class ProfessorResponse(BaseModel):
    id: int
    nome: str
    cpf: str
    rg: str

    class Config:
        from_attributes = True

class ProfessorRequest(BaseModel):
    nome: str
    cpf: str
    rg: str