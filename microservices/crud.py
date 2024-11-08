from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_users(db: Session):
    return db.query(User).all()


def create_user(db: Session, user: UserCreate):
    db_user = User(username=user.username, first_name=user.first_name, last_name=user.last_name, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, username: str, first_name: str, last_name: str, password: str):
    user = get_user(db, user_id)
    if user:
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.password = password
        db.commit()
        db.refresh(user)
    return user


def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
        return db_user
    return None
