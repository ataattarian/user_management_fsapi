import os
from http.client import responses

import grpc
from proto_generated import user_pb2, user_pb2_grpc
from schemas import LoginInput, UserProfileInput

# Get the CRUD service host and port from environment variables
micro_service_host = os.getenv("MICRO_SERVICE_HOST", "localhost")
micro_service_port = os.getenv("MICRO_SERVICE_PORT", "50051")
channel = grpc.insecure_channel(f"{micro_service_host}:{micro_service_port}")
client = user_pb2_grpc.UserServiceStub(channel)


def get_user(user_id: int):
    response = client.GetUser(user_pb2.UserRequest(id=user_id))
    if not response.id:
        user_data = {}
    else:
        user_data = {
            "id": response.id,
            "username": response.username,
            "first_name": response.first_name,
            "last_name": response.last_name,
        }
    return user_data


def get_users():
    response = client.GetUsers(user_pb2.EmptyRequest())
    return {
        "users": [
            {
                "id": user.id,
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name
            }
            for user in response.users
        ]
    }


def register_user(data: UserProfileInput):
    return client.RegisterUser(user_pb2.RegisterUserRequest(
        username=data.username,
        first_name=data.first_name,
        last_name=data.last_name,
        password=data.password
    ))


def update_user(user_id: int, data: UserProfileInput):
    response = client.UpdateUser(user_pb2.UpdateUserRequest(
        id=user_id,
        username=data.username,
        first_name=data.first_name,
        last_name=data.last_name,
        password=data.password
    ))
    user_data = {
        "id": response.id,
        "username": response.username,
        "first_name": response.first_name,
        "last_name": response.last_name,
    }
    return user_data
