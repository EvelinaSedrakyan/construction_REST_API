from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import relationship
from app.database import Base

class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    projects = relationship("Project", back_populates="company", cascade="all, delete")
    workers = relationship("Worker", back_populates="company", cascade="all, delete")

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    budget = Column(Integer, nullable=False)
    description = Column(String)
    metadata_json = Column(JSON)
    company_id = Column(Integer, ForeignKey("companies.id"))
    company = relationship("Company", back_populates="projects")
    workers = relationship("Worker", back_populates="project", cascade="all, delete")


class Worker(Base):
    __tablename__ = "workers"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, index=True)
    role = Column(String, nullable=False)
    email = Column(String)
    company_id = Column(Integer, ForeignKey("companies.id"))
    company = relationship("Company", back_populates="workers")
    project_id = Column(Integer, ForeignKey("projects.id"))
    project = relationship("Project", back_populates="workers")
