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
def create_company(
    company: schemas.CompanyCreate,
    db: Session = Depends(get_db)
):
    return crud.create_company(db, company)

@router.get("/")
def get_companies(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return db.query(crud.models.Company).offset(skip).limit(limit).all()

@router.put("/{company_id}")
def update_company(
    company_id: int,
    company: schemas.CompanyCreate,
    db: Session = Depends(get_db)
):
    return crud.update_company(db, company_id, company)

@router.delete("/{company_id}")
def delete_company(
    company_id: int,
    db: Session = Depends(get_db)
):
    return crud.delete_company(db, company_id)

#join
@router.get("/with-projects")
def companies_with_projects(db: Session = Depends(get_db)):
    return crud.join_companies_projects(db)

#group by
@router.get("/projects-count")
def projects_count(db: Session = Depends(get_db)):
    return crud.group_projects(db)
