from datetime import datetime, timedelta
from jose import jwt
from config.settings import settings

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
    return encoded_jwt

def decode_token(token: str):
    return jwt.decode(
        token,
        settings.secret_key,
        algorithms=[settings.algorithm]
    )