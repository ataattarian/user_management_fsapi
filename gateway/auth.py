import jwt
from datetime import datetime, timedelta
from typing import Optional
from fastapi import HTTPException, Security
from fastapi.security import OAuth2PasswordBearer, HTTPBearer, HTTPAuthorizationCredentials
from dotenv import load_dotenv
import os
from jwt.exceptions import ExpiredSignatureError

load_dotenv()

# JWT Configuration
SECRET_KEY = os.getenv("SECRET_KEY", "mysecretkey")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Use HTTPBearer for extracting Bearer token from Authorization header
security = HTTPBearer()


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode = data.copy()
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("username")

        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        return username

    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")

    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


async def get_current_user(credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials
    username = verify_access_token(token)
    return username
