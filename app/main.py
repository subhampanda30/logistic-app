from fastapi import FastAPI
from app.api.v1.api_v1 import api_v1
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

app.include_router(api_v1, prefix="/api/v1", tags=["v1"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Logistic Application API!"}