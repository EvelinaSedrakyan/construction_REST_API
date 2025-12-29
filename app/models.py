from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import relationship
from .database import Base

class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    info = Column(JSON)
    projects = relationship("Project", back_populates="company")


class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    budget = Column(Integer)
    company_id = Column(Integer, ForeignKey("companies.id"))
    company = relationship("Company", back_populates="projects")
    workers = relationship("Worker", back_populates="project")


class Worker(Base):
    __tablename__ = "workers"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    salary = Column(Integer)
    project_id = Column(Integer, ForeignKey("projects.id"))
    project = relationship("Project", back_populates="workers")
