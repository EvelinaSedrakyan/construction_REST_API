from pydantic import BaseModel

class CompanyCreate(BaseModel):
    name: str
    country: str

class CompanyRead(CompanyCreate):
    id: int
    class Config:
        orm_mode = True   

class ProjectCreate(BaseModel):
    name: str
    budget: int
    company_id: int

class ProjectRead(ProjectCreate):
    id: int
    class Config:
        orm_mode = True    

class WorkerCreate(BaseModel):
    name: str
    role: str
    project_id: int

class WorkerRead(WorkerCreate):
    id: int
    class Config:
        orm_mode = True    
