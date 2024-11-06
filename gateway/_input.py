from pydantic import BaseModel
from uuid import UUID


class LoginInput(BaseModel):
    username: str
    password: str


class UserProfileInput(BaseModel):
    username: str
    first_name: str
    last_name: str
    password: str
