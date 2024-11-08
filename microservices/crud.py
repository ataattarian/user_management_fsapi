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


def update_user(db: Session, data):
    user = db.query(User).filter(User.id ==data.id).first()

    if not user:
        return None

    user.username = data.username or user.username
    user.first_name = data.first_name or user.first_name
    user.last_name = data.last_name or user.last_name
    user.password = data.password or user.password

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
