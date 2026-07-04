from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db import get_db
from services.category_service import *
from schemas.category import *
from security.dependencies import get_current_user

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.post("/")
def create(data: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db, data)

@router.get("/")
def list_all(db: Session = Depends(get_db)):
    return get_categories(db)

@router.put("/{category_id}")
def update(category_id: int, data: CategoryUpdate, db: Session = Depends(get_db)):
    result = update_category(db, category_id, data)
    if not result:
        raise HTTPException(status_code=404, detail="Category not found")
    return result

@router.delete("/{category_id}")
def delete(category_id: int, db: Session = Depends(get_db)):
    result = delete_category(db, category_id)
    if not result:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"message": "Category deleted"}