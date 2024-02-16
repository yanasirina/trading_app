import uvicorn
from fastapi import FastAPI

from auth.router import router as auth_router
from operations.router import router as operation_router


app = FastAPI(title="Trading App")

app.include_router(auth_router)
app.include_router(operation_router)


if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", log_level="info", reload=True)
