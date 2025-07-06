from fastapi import FastAPI, Query, Depends
from pydantic import BaseModel, Field
from typing import List, Optional
from sqlalchemy import create_engine, Column, Integer, String, Float, select, and_
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from app.models.database import Base
app = FastAPI()



class Ad(Base):
    __tablename__ = "advertising"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    category = Column(String, index=True)
    price = Column(Float, index=True)
    location = Column(String, index=True)






