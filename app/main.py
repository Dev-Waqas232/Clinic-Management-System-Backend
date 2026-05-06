import uvicorn
from fastapi import FastAPI

from app.modules.auth.router import router as auth_router

app = FastAPI()

app.include_router(auth_router)


@app.get("/")
async def root():
    return {"message": "Hello World!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
