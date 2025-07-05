from fastapi import FastAPI, Query, Depends
from pydantic import BaseModel, Field
from typing import List, Optional
from sqlalchemy import create_engine, Column, Integer, String, Float, select, and_
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from .database import Base
app = FastAPI()



class Ad(Base):
    __tablename__ = "advertising"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    category = Column(String, index=True)
    price = Column(Float, index=True)
    location = Column(String, index=True)



def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
@app.get("/ads/", response_model=List[AdOut])
def read_ads(
    category: Optional[str] = Query(None),
    min_price: Optional[float] = Query(None, ge=0),
    max_price: Optional[float] = Query(None, ge=0),
    location: Optional[str] = Query(None),
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    filters = []
    if category:
        filters.append(Ad.category == category)
    if min_price is not None:
        filters.append(Ad.price >= min_price)
    if max_price is not None:
        filters.append(Ad.price <= max_price)
    if location:
        filters.append(Ad.location == location)

    query = select(Ad).where(and_(*filters)) if filters else select(Ad)
    query = query.offset(skip).limit(limit)
    result = db.execute(query).scalars().all()
    return result



