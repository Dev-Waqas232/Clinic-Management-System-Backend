from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.auth.service import register_user
from .schemas import RegisterBody, RegisterResponse
from app.db.database import get_db

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=RegisterResponse)
async def register(data: RegisterBody, db: AsyncSession = Depends(get_db)):
    return await register_user(data, db)
