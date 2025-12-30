from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas, database

router = APIRouter(prefix="/companies", tags=["companies"])
get_db = database.get_db

@router.post("/", response_model=schemas.CompanyRead)
def create_company(company: schemas.CompanyCreate, db: Session = Depends(get_db)):
    return crud.create_company(db, company)

@router.get("/", response_model=list[schemas.CompanyRead])
def get_companies(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_companies(db, skip, limit)

@router.put("/{company_id}", response_model=schemas.CompanyRead)
def update_company(company_id: int, company: schemas.CompanyCreate, db: Session = Depends(get_db)):
    return crud.update_company(db, company_id, company)

@router.delete("/{company_id}")
def delete_company(company_id: int, db: Session = Depends(get_db)):
    return crud.delete_company(db, company_id)

@router.get("/with-projects")
def companies_with_projects(db: Session = Depends(get_db)):
    return crud.join_companies_projects(db)

@router.get("/projects-count")
def projects_count(db: Session = Depends(get_db)):
    return crud.group_projects(db)
