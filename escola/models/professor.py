from sqlalchemy import Column, Integer, String
from shared.database import Base


class Professor(Base):
    __tablename__ = "professores"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50))
    cpf = Column(String(30))
    rg = Column(String(30))
    # Campo de turmas