from shared.database import Base
from sqlalchemy import Column, Integer, String


class Turma(Base):
    __tablename__ = "turmas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    serie = Column(String(30))
    codigo = Column(String(30))