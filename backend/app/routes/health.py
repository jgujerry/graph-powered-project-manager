from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["health"])


@router.get("/", response_model=dict)
async def health():
    return {"status": "ok"}
