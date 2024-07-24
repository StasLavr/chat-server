import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
subfolder_path = os.path.join(current_dir, '..')
sys.path.append(subfolder_path)
from conf import token
import uuid
from typing import Optional, Annotated, Union

from fastapi import Depends, Request, Query
from fastapi_users import BaseUserManager, IntegerIDMixin, InvalidPasswordException

from .db import User, get_user_db

SECRET = token


class UserManager(IntegerIDMixin, BaseUserManager[User, uuid.   UUID]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: Annotated[User, Query(min_length=3)], request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")
    async def validate_password(
        self,
        password: str,
        user: Union[User: User],
    ) -> None:
        if len(password) < 8:
            raise InvalidPasswordException(
                reason="Password should be at least 8 characters"
            )
        if len(user.email) < 4:
            raise InvalidPasswordException(
                reason="Email should be at least 4 characters"
            )
        if len(user.username) < 3:
            raise InvalidPasswordException(
                reason="Username should be at least 3 characters"
            )
        if len(user.fullname) < 3:
            raise InvalidPasswordException(
                reason="Fullname should be at least 4 characters"
            )


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)