

from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from escola.models.aluno import Aluno
from escola.schemas.aluno_schema import AlunoRequest, AlunoResponse
from shared.dependencies import get_db


router = APIRouter(prefix="/escola")

@router.get("/", response_model=List[AlunoResponse], status_code=200)
async def get_alunos(db: Session=Depends(get_db)) -> List[AlunoResponse]:
    return db.query(Aluno).all()

@router.get("/{id_aluno}", response_model=AlunoResponse, status_code=200)
async def get_aluno(id_aluno:int, db:Session=Depends(get_db)) -> AlunoResponse:
    aluno = buscar_aluno_por_id(id_aluno, db)
    return aluno

@router.post("", response_model=AlunoResponse, status_code=201)
async def criar_aluno(aluno_request:AlunoRequest, db:Session=Depends(get_db)) -> AlunoResponse:
    aluno = Aluno(**aluno_request.model_dump())
    db.add(aluno)
    db.commit()
    db.refresh(aluno)
    return aluno


def buscar_aluno_por_id(id:int, db:Session) -> Aluno:
    aluno = db.query(Aluno).get(id)
    if aluno is None:
        raise "Aluno não encontrado"
    return aluno