from fastapi import Depends, HTTPException
from jose import jwt
from fastapi.security import OAuth2PasswordBearer
import os

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def require_role(required_role: str):
    def role_dependency(token: str = Depends(oauth2_scheme)):
        payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=["HS256"])
        if payload.get("role") != required_role:
            raise HTTPException(status_code=403, detail="Forbidden")
        return payload
    return role_dependency