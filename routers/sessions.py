from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.db import get_db
from security.dependencies import get_current_user

from schemas.session import SessionCreate
from services.session_service import create_session, get_sessions

router = APIRouter(
    prefix="/sessions",
    tags=["sessions"]
)

@router.post("/")
def create(
        data: SessionCreate,
        db: Session = Depends(get_db),
        user_id: int = Depends(get_current_user)
):
    result = create_session(db, user_id, data)
    if not result:
        raise HTTPException(status_code=400, detail="Session creation failed")
    return result

@router.get("/")
def list_sessions(
        db: Session = Depends(get_db),
        user_id: int = Depends(get_current_user)
):
    return get_sessions(db, user_id)