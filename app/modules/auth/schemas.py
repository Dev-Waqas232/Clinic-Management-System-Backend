from pydantic import BaseModel, Field, EmailStr

from app.modules.users.models import Role


class RegisterBody(BaseModel):
    first_name: str = Field(examples=["Usman"], max_length=30)
    last_name: str = Field(examples=["Ghani"], max_length=30)
    email: EmailStr
    password: str = Field(min_length=8)
    role: Role


class RegisterResponse(BaseModel):
    first_name: str
    last_name: str
    email: str
    role: Role
    is_email_verified: bool
