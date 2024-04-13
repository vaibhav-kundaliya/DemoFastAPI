from fastapi import FastAPI
from auth_service.auth_service import auth_service
from dotenv import load_dotenv
from db.database import engine
from db import models
from os.path import join, dirname
dotenv_path = join(dirname(__file__), './.env')
load_dotenv(dotenv_path)
models.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(auth_service, prefix='/api/v1/auth_service')


@app.get("/")
async def root():
    return {"message": "Server is on"}
