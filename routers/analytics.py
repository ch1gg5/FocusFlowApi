from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.db import get_db
from security.dependencies import get_current_user
from services.analytics_service import *

router = APIRouter(prefix="/analytics", tags=["Analytics"])

@router.get("/study-hours")
def total_hours(db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    return get_total_study_hours(db, user_id)

@router.get("/categories")
def category_stats(db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    return get_category_breakdown(db, user_id)

@router.get("/weekly")
def weekly(db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    return get_weekly_productivity(db, user_id)

@router.get("/streak")
def streak(db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    return get_streak(db, user_id)