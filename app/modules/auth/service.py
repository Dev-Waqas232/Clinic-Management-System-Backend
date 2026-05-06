from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from passlib.hash import bcrypt

from .schemas import RegisterBody, RegisterResponse
from app.modules.users.models import User
from .models import Auth


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
