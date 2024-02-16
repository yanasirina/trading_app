from fastapi_users import FastAPIUsers
from fastapi import Depends, APIRouter
from auth.backend import auth_backend
from auth.models import User
from auth.manager import get_user_manager
from auth.schemas import UserRead, UserCreate, UserUpdate


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

fastapi_users = FastAPIUsers[User, int](get_user_manager,[auth_backend])
current_user = fastapi_users.current_user()

router.include_router(fastapi_users.get_auth_router(auth_backend), prefix="/jwt")
router.include_router(fastapi_users.get_register_router(UserRead, UserCreate), prefix="/auth")
router.include_router(fastapi_users.get_users_router(UserRead, UserUpdate), prefix="/users", tags=["Users"])


@router.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"


@router.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonym"
