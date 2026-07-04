from sqlalchemy.orm import Session
from models.user import User
from schemas.auth import UserCreate
from security.password import hash_password, verify_password
from security.jwt_handler import create_access_token

def register_user(db: Session, user: UserCreate):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        return None

    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.hashed_password):
        return None

    token = create_access_token({"sub": str(user.id)})

    return token