from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db import get_db
from services.task_service import *
from schemas.task import *
from security.dependencies import get_current_user

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)

@router.post("/")
def create_task_endpoint(data: TaskCreate, db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    return create_task(db, user_id, data)

@router.get("/")
def list_tasks(
        completed: bool = None,
        priority: str = None,
        category_id: int = None,
        db: Session = Depends(get_db),
        user_id: int = Depends(get_current_user)
):
    return get_tasks(db, user_id, completed, priority, category_id)

@router.put("/{task_id}")
def update_task_endpoint(task_id: int, data: TaskUpdate, db: Session = Depends(get_db),
                         user_id: int = Depends(get_current_user)):
    result = update_task(db, user_id, task_id, data)
    if not result:
        raise HTTPException(status_code=404, detail="Task not found")
    return result

@router.delete("/{task_id}")
def delete(task_id: int, db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    result = delete_task(db, user_id, task_id)
    if not result:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted"}