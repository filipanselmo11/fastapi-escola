from typing import List
from fastapi import APIRouter, Depends
from escola.models.turma import Turma
from escola.schemas.turma_schema import TurmaRequest, TurmaResponse
from sqlalchemy.orm import Session
from shared.exceptions import NotFound
from shared.dependencies import get_db


router = APIRouter(prefix="/escola")

@router.get("/", response_model=List[TurmaResponse], status_code=200)
async def get_turmas(db: Session=Depends(get_db)) -> List[TurmaResponse]:
    return db.query(Turma).all()


@router.get("/{id_turma}", response_model=TurmaResponse, status_code=200)
async def get_turma(id_turma:int, db:Session=Depends(get_db)) -> TurmaResponse:
    turma = buscar_turmar_por_id(id_turma, db)
    return turma

@router.post("", response_model=TurmaResponse, status_code=201)
async def criar_turma(turma_request:TurmaRequest, db:Session=Depends(get_db)) -> TurmaResponse:
    turma = Turma(**turma_request.model_dump())
    db.add(turma)
    db.commit()
    db.refresh(turma)
    return turma

def buscar_turmar_por_id(id:int, db:Session) -> Turma:
    turma = db.query(Turma).get(id)
    if turma is None:
        raise NotFound("Turma não encotrada")
    return turma