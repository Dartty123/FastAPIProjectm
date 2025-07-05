from fastapi import FastAPI, Query, Depends
import uvicorn
from app.models.database import *
from app.models.models import *
create_all()
app = FastAPI()


if __name__ == "__main__":
    uvicorn.run(app)