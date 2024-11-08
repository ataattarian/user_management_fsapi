import grpc
from concurrent import futures
from proto_generated import user_pb2, user_pb2_grpc
from crud import get_user, get_users, create_user, delete_user
from database import engine, Base, SessionLocal
from sqlalchemy.exc import IntegrityError


Base.metadata.create_all(bind=engine)


class UserService(user_pb2_grpc.UserServiceServicer):
    def GetUser(self, request, context):
        db = SessionLocal()
        user = get_user(db, user_id=request.id)
        db.close()
        if user:
            return user_pb2.UserResponse(id=user.id, username=user.username, first_name=user.first_name,
                                         last_name=user.last_name)
        return user_pb2.UserResponse()

    def GetUsers(self, request, context):
        db = SessionLocal()
        users = get_users(db)
        db.close()
        return user_pb2.UserListResponse(users=[
            user_pb2.UserResponse(id=u.id, username=u.username, first_name=u.first_name, last_name=u.last_name) for u in
            users
        ])

    def RegisterUser(self, request, context):
        db = SessionLocal()
        try:
            new_user = create_user(
                db=db,
                user=request
            )
            return user_pb2.UserResponse(
                id=new_user.id,
                username=new_user.username,
                first_name=new_user.first_name,
                last_name=new_user.last_name
            )
        except IntegrityError:
            db.rollback()
            context.set_code(grpc.StatusCode.ALREADY_EXISTS)
            context.set_details("Username already exists.")
            return user_pb2.UserResponse()
        finally:
            db.close()

    def DeleteUser(self, request, context):
        db = SessionLocal()
        success = delete_user(db, user_id=request.id) is not None
        db.close()
        return user_pb2.DeleteUserResponse(success=success)


# Start gRPC server
grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
user_pb2_grpc.add_UserServiceServicer_to_server(UserService(), grpc_server)
grpc_server.add_insecure_port('[::]:50051')
grpc_server.start()
print("gRPC server is running on port 50051")
grpc_server.wait_for_termination()
