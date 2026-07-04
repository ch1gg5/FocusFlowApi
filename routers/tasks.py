from fastapi import APIRouter, Depends
from security.dependencies import get_current_user

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)

@router.get("/")
def get_tasks(user_id: str = Depends(get_current_user)):
    return {"message" : "You are Authenticated", "user_id": user_id}