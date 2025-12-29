from pydantic import BaseModel
from typing import Optional, Dict

class CompanyCreate(BaseModel):
    name: str
    info: Dict

class ProjectCreate(BaseModel):
    title: str
    budget: int
    company_id: int

class WorkerCreate(BaseModel):
    name: str
    salary: int
    project_id: int
