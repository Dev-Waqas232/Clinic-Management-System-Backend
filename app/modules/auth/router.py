from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.auth.service import register_user, login_user
from .schemas import LoginBody, LoginResponse, RegisterBody, RegisterResponse
from app.db.database import get_db

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=RegisterResponse)
async def register(data: RegisterBody, db: AsyncSession = Depends(get_db)):
    return await register_user(data, db)


@router.post("/login", response_model=LoginResponse)
async def login(
    data: LoginBody, response: Response, db: AsyncSession = Depends(get_db)
):
    return await login_user(data, db, response)
