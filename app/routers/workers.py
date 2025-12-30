from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas, database

router = APIRouter(prefix="/workers", tags=["workers"])
get_db = database.get_db

@router.post("/", response_model=schemas.WorkerRead)
def create_worker(worker: schemas.WorkerCreate, db: Session = Depends(get_db)):
    return crud.create_worker(db, worker)

@router.get("/", response_model=list[schemas.WorkerRead])
def get_workers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_workers(db, skip, limit)
