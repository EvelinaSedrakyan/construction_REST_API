from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas, database, models

router = APIRouter(prefix="/projects", tags=["projects"])
get_db = database.get_db

@router.post("/", response_model=schemas.ProjectRead)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    return crud.create_project(db, project)

@router.get("/", response_model=list[schemas.ProjectRead])
def get_projects(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_projects(db, skip, limit)

@router.get("/filter", response_model=list[schemas.ProjectRead])
def filter_projects(min_budget: int, name_part: str, db: Session = Depends(get_db)):
    return crud.filter_projects(db, min_budget, name_part)

@router.put("/increase-budget", response_model=list[schemas.ProjectRead])
def increase_budget(limit: int, increase: int, db: Session = Depends(get_db)):
    return crud.update_budget(db, limit, increase)

@router.get("/sorted", response_model=list[schemas.ProjectRead])
def sorted_projects(desc: bool = False, db: Session = Depends(get_db)):
    return crud.sorted_projects(db, desc)

@router.get("/search-json", response_model=list[schemas.ProjectRead])
def search_projects(pattern: str, db: Session = Depends(get_db)):
    return db.query(models.Project)\
             .filter(models.Project.metadata_json.cast(sa.Text).op("~")(pattern))\
             .all()
