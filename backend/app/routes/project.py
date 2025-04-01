from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(prefix="/projects", tags=["projects"])

@router.get("/")
async def get_projects():
    return {"message": "project one"}

