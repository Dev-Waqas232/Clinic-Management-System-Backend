from datetime import datetime, timedelta, timezone
from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from passlib.hash import bcrypt
import jwt

from .schemas import LoginBody, LoginResponse, RegisterBody, RegisterResponse
from app.modules.users.models import User
from .models import Auth
from app.core.config import settings


async def register_user(body: RegisterBody, db: AsyncSession):
    result = await db.execute(select(User).where(User.email == body.email))
    user = result.scalar_one_or_none()

    if user is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="This email is already associated with an account",
        )

    password_hash = bcrypt.hash(body.password)

    new_user = User(
        first_name=body.first_name,
        last_name=body.last_name,
        email=body.email,
        role=body.role,
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    user_auth = Auth(password_hash=password_hash, user_id=new_user.id)
    db.add(user_auth)
    await db.commit()

    return RegisterResponse(
        first_name=new_user.first_name,
        last_name=new_user.last_name,
        email=new_user.email,
        role=new_user.role,
        is_email_verified=user_auth.is_email_verified,
    )


async def login_user(body: LoginBody, db: AsyncSession):
    result = await db.execute(select(User).where(User.email == body.email))
    user = result.scalar_one_or_none()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials"
        )

    result = await db.execute(select(Auth).where(Auth.user_id == user.id))
    auth = result.scalar_one()

    has_password_match = bcrypt.verify(body.password, auth.password_hash)
    if not has_password_match:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials"
        )

    if not auth.is_email_verified:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Please confirm your email first to login to the system",
        )

    access_exp = datetime.now(timezone.utc) + timedelta(days=1)
    refresh_exp = datetime.now(timezone.utc) + timedelta(days=7)

    access_token = generate_token(
        {
            "user_id": str(user.id),
            "role": user.role.value,
            "email": user.email,
            "exp": access_exp,
        },
        settings.JWT_ACCESS_SECRET,
    )
    refresh_token = generate_token(
        {
            "user_id": str(user.id),
            "role": user.role.value,
            "email": user.email,
            "exp": refresh_exp,
        },
        settings.JWT_REFRESH_SECRET,
    )

    return LoginResponse(access_token=access_token, refresh_token=refresh_token)


def generate_token(payload: dict, secret: str) -> str:
    token = jwt.encode(payload, secret, algorithm="HS256")
    return token
