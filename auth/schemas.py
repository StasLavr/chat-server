import uuid

from fastapi_users import schemas


class UserRead(schemas.BaseUser[uuid.UUID]):
    username: str
    fullname: str
    email: str
    id: int


class UserCreate(schemas.BaseUserCreate):
    username: str                                       
    fullname: str
    email: str
    password: str


class UserUpdate(schemas.BaseUserUpdate):
    pass
