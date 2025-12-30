from pydantic import BaseModel
from typing import List, Optional

class ProjectRead(BaseModel):
    id: int
    name: str
    budget: int
    description: Optional[str] = None
    metadata_json: Optional[dict] = None
    class Config:
        orm_mode = True

class WorkerRead(BaseModel):
    id: int
    name: str
    role: str
    email: Optional[str] = None
    project_id: int
    company_id: int
    class Config:
        orm_mode = True

class CompanyCreate(BaseModel):
    name: str
    country: str

class CompanyRead(CompanyCreate):
    id: int
    projects: List[ProjectRead] = []
    workers: List[WorkerRead] = []
    class Config:
        orm_mode = True

class ProjectCreate(BaseModel):
    name: str
    budget: int
    description: Optional[str] = None
    metadata_json: Optional[dict] = None
    company_id: int

class ProjectReadFull(ProjectRead):
    workers: List[WorkerRead] = []
    class Config:
        orm_mode = True


class WorkerCreate(BaseModel):
    name: str
    role: str
    email: Optional[str] = None
    project_id: int
    company_id: int

class WorkerReadFull(WorkerRead):
    class Config:
        orm_mode = True
