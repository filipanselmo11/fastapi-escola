from fastapi import FastAPI

from escola.routers import aluno_router

app = FastAPI()

@app.get("/")
async def root():
    return "Olá Mundo"

app.include_router(aluno_router.router)