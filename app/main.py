from fastapi import FastAPI
from app.database import Base, engine
from app import models
from app.routers import companies, projects, workers

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Construction REST API")

app.include_router(companies.router, prefix="/companies", tags=["Companies"])
app.include_router(projects.router, prefix="/projects", tags=["Projects"])
app.include_router(workers.router, prefix="/workers", tags=["Workers"])
