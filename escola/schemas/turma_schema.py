from pydantic import BaseModel

class TurmaResponse(BaseModel):
    id: int
    serie: str
    codigo: str

    class Config:
        from_attributes = True


class TurmaRequest(BaseModel):
    serie: str
    codigo: str