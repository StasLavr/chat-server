import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
subfolder_path = os.path.join(current_dir, '..')
sys.path.append(subfolder_path)
from conf import token

from fastapi_users.authentication import CookieTransport, JWTStrategy,  AuthenticationBackend, BearerTransport
cookie_transport = CookieTransport(cookie_name="auth", cookie_max_age=3600)
SECRET=token
def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)