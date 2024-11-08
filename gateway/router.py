import grpc
from fastapi import Body, APIRouter, HTTPException, Depends
from schemas import LoginInput, UserProfileInput
from grpc_client import get_user, get_users, update_user, register_user, delete_user, login_req
from auth import create_access_token, get_current_user

public_router = APIRouter()
protected_router = APIRouter(dependencies=[Depends(get_current_user)])

@protected_router.get("/users/")
async def get_users_list(current_user: dict = Depends(get_current_user)):
    try:
        return get_users()
    except grpc.RpcError as e:
        raise HTTPException(status_code=500, detail=e.details())


@protected_router.get("/user_info/{user_id}")
async def get_user_info(user_id: int):
    try:
        return get_user(user_id)
    except grpc.RpcError as e:
        raise HTTPException(status_code=404, detail=e.details())


@public_router.post("/register")
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


@public_router.post("/login")
async def login(data: LoginInput = Body()):
    resp = login_req(data)

    if resp.valid:
        access_token = create_access_token(data={"username": data.username})
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=401, detail="username or password incorrect")


@protected_router.put("/user_info/{user_id}")
async def update_profile(user_id: int, data: UserProfileInput = Body()):
    try:
        return update_user(user_id, data)
    except grpc.RpcError as e:
        if e.code() == grpc.StatusCode.NOT_FOUND:
            raise HTTPException(status_code=404, detail="User not found.")
        elif e.code() == grpc.StatusCode.ALREADY_EXISTS:
            raise HTTPException(status_code=409, detail="Username already exists.")
        raise HTTPException(status_code=500, detail="Internal server error.")


@protected_router.delete("/user_info/{user_id}")
async def delete_profile(user_id: int):
    try:
        response = delete_user(user_id)

        if not response.success:
            raise HTTPException(status_code=404, detail="User not found.")

        return {"detail": "User deleted successfully."}

    except grpc.RpcError as e:
        if e.code() == grpc.StatusCode.NOT_FOUND:
            raise HTTPException(status_code=404, detail="User not found.")
        raise HTTPException(status_code=500, detail="Internal server error.")
