from fastapi import FastAPI
from crud_operation_service.crud_service import crud_service
from auth_service.auth_service import auth_service
from dotenv import load_dotenv
from db.database import engine
from db import models
from os.path import join, dirname
models.Base.metadata.create_all(bind=engine)

dotenv_path = join(dirname(__file__), './.env')
load_dotenv(dotenv_path)

app = FastAPI()

app.include_router(crud_service, prefix='/api/v1/crud_service')
app.include_router(auth_service, prefix='/api/v1/auth_service')


@app.get("/")
async def root():
    return {"message": "Server is on"}
