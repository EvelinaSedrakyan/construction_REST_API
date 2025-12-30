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
def create_project(
    project: schemas.ProjectCreate,
    db: Session = Depends(get_db)
):
    return crud.create_project(db, project)

@router.get("/")
def get_projects(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return db.query(crud.models.Project).offset(skip).limit(limit).all()

#where
@router.get("/filter")
def filter_projects(
    min_budget: int,
    name_part: str,
    db: Session = Depends(get_db)
):
    return crud.filter_projects(db, min_budget, name_part)

#update
@router.put("/increase-budget")
def increase_budget(
    limit: int,
    increase: int,
    db: Session = Depends(get_db)
):
    return crud.update_budget(db, limit, increase)

#sort
@router.get("/sorted")
def sorted_projects(
    desc: bool = False,
    db: Session = Depends(get_db)
):
    return crud.sorted_projects(db, desc)
