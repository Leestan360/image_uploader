from pydantic import BaseModel
from typing import Optional, Union


# class SignUpModel(BaseModel):
#     id: Optional[int]
#     username: str
#     password: str


#     class Config:
#         orm_mode = True
#         schema_extra = {
#             'example':{
#                 'username': 'stanleymay',
#                 'password': 'password'
#             }
#         }


# class ItemModel(BaseModel):
#     title: str
#     description: Union[str, None] = None


class ImageBase(BaseModel):
    title: str
    description: Union[str, None] = None


class ImageCreate(ImageBase):
    pass


class Image(ImageBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    items: list[Image] = []

    class Config:
        orm_mode = True
