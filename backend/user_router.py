from fastapi import APIRouter
import schemas, models
from database import Session, engine


user_router = APIRouter(
    prefix = '/user',
    tags = ['user']
)


session = Session(bind=engine)

@user_router.get('/ID')
def get_user_by_id(user_id: int):
    return session.query(models.User).filter(models.User.id == user_id).first()


@user_router.get('/Username')
def get_user_by_username(username: str):
    return session.query(models.User).filter(models.User.username == username).first()


@user_router.post('/Signup')
def create_user(user: schemas.UserCreate):
    db_user = models.User(username=user.username, password=user.password)
    session.add(db_user)
    session.commit()
    return db_user


# @user_router.post('/Login')
# def login()