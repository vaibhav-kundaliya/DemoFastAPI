from fastapi import APIRouter

crud_service = APIRouter()

@crud_service.get("/")
def root():
    return {"message":"Service is on"}