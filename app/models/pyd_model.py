from pydantic import Field, BaseModel


class AdBase(BaseModel):
    title: str
    description: str
    category: str
    price: float
    location: str

class AdOut(BaseModel):
    id: int

    class Config:
        orm_mode = True