from fastapi import FastAPI
import uuid
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends
from fastapi_users import FastAPIUsers, fastapi_users
from auth.manager import get_user_manager
from auth.auth import auth_backend
from auth.db import User
from auth.schemas import UserCreate, UserRead
fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


app = FastAPI() 

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

current_user = fastapi_users.current_user()

@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"
