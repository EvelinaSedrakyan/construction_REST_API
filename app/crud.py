from sqlalchemy.orm import Session
from sqlalchemy import func
from app import models, schemas

def create_company(db: Session, company: schemas.CompanyCreate):
    obj = models.Company(**company.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def create_project(db: Session, project: schemas.ProjectCreate):
    obj = models.Project(**project.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def create_worker(db: Session, worker: schemas.WorkerCreate):
    obj = models.Worker(**worker.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

#read and filter
def get_companies(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Company).offset(skip).limit(limit).all()

def get_projects(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Project).offset(skip).limit(limit).all()

def get_workers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Worker).offset(skip).limit(limit).all()

def filter_projects(db: Session, min_budget: int, name_part: str):
    return db.query(models.Project)\
        .filter(
            models.Project.budget >= min_budget,
            models.Project.name.ilike(f"%{name_part}%")
        ).all()

#join,group by
def join_companies_projects(db: Session):
    return db.query(models.Company.name, models.Project.name)\
        .join(models.Project).all()

def group_projects(db: Session):
    return db.query(
        models.Company.name,
        func.count(models.Project.id)
    ).join(models.Project).group_by(models.Company.name).all()

#update, sort
def update_budget(db: Session, limit: int, inc: int):
    projects = db.query(models.Project)\
        .filter(models.Project.budget < limit).all()
    for p in projects:
        p.budget += inc
    db.commit()
    return projects

def sorted_projects(db: Session, desc: bool):
    q = db.query(models.Project)
    return q.order_by(models.Project.budget.desc() if desc else models.Project.budget).all()
