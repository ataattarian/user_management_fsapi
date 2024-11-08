import grpc
from fastapi import Body, APIRouter, HTTPException
from schemas import LoginInput, UserProfileInput
from grpc_client import get_user, get_users, update_user, register_user

router = APIRouter()


@router.get("/users/")
async def get_users_list():
    try:
        return get_users()
    except grpc.RpcError as e:
        raise HTTPException(status_code=500, detail=e.details())


@router.get("/user_info/{user_id}")
async def get_user_info(user_id: int):
    try:
        return get_user(user_id)
    except grpc.RpcError as e:
        raise HTTPException(status_code=404, detail=e.details())


@router.post("/register")
async def register(data: UserProfileInput = Body()):
    try:
        user = register_user(data)
        return {
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name
        }
    except grpc.RpcError as e:
        if e.code() == grpc.StatusCode.ALREADY_EXISTS:
            raise HTTPException(status_code=409, detail="Username already exists.")
        else:
            raise HTTPException(status_code=500, detail="Internal server error.")


@router.post("/login")
async def login(data: LoginInput = Body()):
    return {"data": data}


@router.put("/user_info/{user_id}")
async def update_profile(user_id: int, data: UserProfileInput = Body()):
    user = update_user(user_id, data)
    if not user.id:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.delete("/user_info/{user_id}")
async def delete_profile(user_id: int):
    return {"user_id": user_id}
