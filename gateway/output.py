from pydantic import BaseModel
from uuid import UUID

class UserInfoOutput(BaseModel):
    id: UUID
    username: str
    first_name: str
    last_name: str

