from fastapi import FastAPI, Query, Depends
import uvicorn
from app.models.database import *
from app.models.models import *
from app.routes.main_router import *
create_all()
app = FastAPI()

app.include_router(main_router)


if __name__ == "__main__":
    uvicorn.run(app)

