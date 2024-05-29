from sqlalchemy import Column, Integer, Numeric, String

from shared.database import Base

class Aluno(Base):
    __tablename__ = "alunos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(30))
    cpf = Column(String(50))
    rg = Column(String(50))