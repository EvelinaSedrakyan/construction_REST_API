from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#crud
@router.post("/")
def create_worker(
    worker: schemas.WorkerCreate,
    db: Session = Depends(get_db)
):
    return crud.create_worker(db, worker)

@router.get("/")
def get_workers(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return db.query(crud.models.Worker).offset(skip).limit(limit).all()
