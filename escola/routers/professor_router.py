from sqlalchemy.orm import Session
from typing import List
from fastapi import APIRouter, Depends
from escola.schemas.professor_schema import ProfessorRequest, ProfessorResponse
from shared.dependencies import get_db
from shared.exceptions import NotFound
from escola.models.professor import Professor

router = APIRouter(prefix="/professor")

@router.get("/", response_model=List[ProfessorResponse], status_code=200)
async def get_professores(db: Session=Depends(get_db)) -> List[ProfessorResponse]:
    return db.query(Professor).all()

@router.get("/{id_professor}", response_model=ProfessorResponse, status_code=200)
async def get_professor(id_professor:int, db:Session=Depends(get_db)) -> ProfessorResponse:
    professor = buscar_professor_id(id_professor, db)
    return professor

@router.post("", response_model=ProfessorResponse, status_code=201)
async def criar_professor(professor_request:ProfessorRequest, db:Session=Depends(get_db)) -> ProfessorRequest:
    professor = Professor(**professor_request.model_dump())
    db.add(professor)
    db.commit()
    db.refresh(professor)
    return professor

@router.delete("/{id_professor}", status_code=204)
async def deletar_professor(id_professor:int, db:Session=Depends(get_db)) -> None:
    professor = buscar_professor_id(id_professor, db)
    db.delete(professor)
    db.commit()


def buscar_professor_id(int:int, db:Session) -> Professor:
    professor = db.query(Professor).get(id)
    if professor is None:
        raise NotFound("Professor(a) não encotrado(a)")
    return professor