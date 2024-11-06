from fastapi import Body, APIRouter
from _input import LoginInput, UserProfileInput
from output import UserInfoOutput

router = APIRouter()


@router.get("/users/")
async def get_users():
    # users = get_users()
    # return {"users": users.users}
    return {"users": "ata"}


@router.get("/user_info/{user_id}")
async def get_user_info(user_id: int):
    return {"user_id": user_id}


@router.post("/register")
async def register(data: UserProfileInput = Body()):
    return {"data": data}


@router.post("/login")
async def login(data: LoginInput = Body()):
    return {"data": data}


@router.put("/user_info/{user_id}")
async def update_profile(user_id: int, data: UserProfileInput = Body()):
    return {"user_id": user_id, "data": data}


@router.delete("/user_info/{user_id}")
async def delete_profile(user_id: int):
    return {"user_id": user_id}
