from fastapi import FastAPI
from router import public_router, protected_router

app = FastAPI()
app.include_router(public_router, prefix="/api/v1")
app.include_router(protected_router, prefix="/api/v1")
