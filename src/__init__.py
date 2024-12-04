from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.auth.routes import auth_router
from src.db.main import init_db

@asynccontextmanager
async def life_span(app : FastAPI):
    print("Server is starting...")
    await init_db()
    yield
    print("Server has been stopped")

version = "v1"

app = FastAPI(
    title="Musicapp",
    description="A REST API for a music app web service",
    version=version,
    lifespan=life_span,
)


app.include_router(auth_router ,prefix=f"/api/{version}/auth", tags=['auth'])




