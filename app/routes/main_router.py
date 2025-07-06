from fastapi import APIRouter, Query, Depends
from typing import Optional, List
from app.models.database import Base, SessionLocal
from app.models.models import Ad
from sqlalchemy import select, and_
from app.shemas.pyd_model import AdOut

main_router = APIRouter(prefix="/main", tags=["main"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@main_router.get("/ads/", response_model=List[AdOut])
def read_ads(
    category: Optional[str] = Query(None),
    min_price: Optional[float] = Query(None, ge=0),
    max_price: Optional[float] = Query(None, ge=0),
    location: Optional[str] = Query(None),
    skip: int = 0,
    limit: int = 10,
    db: SessionLocal = Depends(get_db)
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
