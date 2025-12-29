from sqlalchemy.orm import Session
from . import models, schemas

def create_company(db: Session, company: schemas.CompanyCreate):
    obj = models.Company(**company.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def create_project(db: Session, project: schemas.ProjectCreate):
    obj = models.Project(**project.dict())
    db.add(obj)
    db.commit()
    return obj

def create_worker(db: Session, worker: schemas.WorkerCreate):
    obj = models.Worker(**worker.dict())
    db.add(obj)
    db.commit()
    return obj
