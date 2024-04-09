from fastapi import APIRouter

auth_service = APIRouter()

@auth_service.get("/")
def root():
    return {"message":"Service is on"}