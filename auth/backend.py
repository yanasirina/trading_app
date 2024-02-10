from fastapi_users.authentication import CookieTransport, JWTStrategy, AuthenticationBackend

from config import JWT_SECRET


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=JWT_SECRET, lifetime_seconds=60*60)


cookie_transport = CookieTransport(cookie_name='token', cookie_max_age=60*60)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)
