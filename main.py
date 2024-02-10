import uvicorn
from fastapi_users import FastAPIUsers
from fastapi import FastAPI, Depends

from auth.backend import auth_backend
from auth.models import User
from auth.manager import get_user_manager
from auth.schemas import UserRead, UserCreate, UserUpdate


app = FastAPI(title="Trading App")

fastapi_users = FastAPIUsers[User, int](get_user_manager,[auth_backend])
current_user = fastapi_users.current_user()

app.include_router(fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"])
app.include_router(fastapi_users.get_register_router(UserRead, UserCreate), prefix="/auth", tags=["auth"])
app.include_router(fastapi_users.get_users_router(UserRead, UserUpdate), prefix="/users", tags=["users"])


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"


@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonym"


if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", log_level="info", reload=True)
