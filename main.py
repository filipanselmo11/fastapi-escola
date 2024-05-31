from fastapi import FastAPI

from escola.routers import aluno_router, professor_router, turma_router
from shared.exceptions import NotFound
from shared.exceptions_handle import not_found_handler

app = FastAPI()

@app.get("/")
async def root():
    return "Olá Mundo"

app.include_router(aluno_router.router)
app.include_router(professor_router.router)
app.include_router(turma_router.router)
app.add_exception_handler(NotFound, not_found_handler)