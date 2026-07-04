from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.db import get_db
from schemas.auth import UserCreate, UserLogin, TokenResponse
from services.auth_service import register_user, authenticate_user

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    result = register_user(db, user)

    if not result:
        raise HTTPException(status_code=400, detail="User already exists")

    return {"message": "User registered successfully"}

@router.post("/login", response_model=TokenResponse)
def login(user: UserLogin, db: Session = Depends(get_db)):
    token = authenticate_user(db, user.email, user.password)

    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"access_token": token, "token_type": "bearer"}
