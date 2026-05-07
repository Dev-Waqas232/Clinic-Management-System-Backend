from pydantic import BaseModel, Field, EmailStr

from app.modules.users.models import Role


class AuthBaseModel(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)


class RegisterBody(AuthBaseModel):
    first_name: str = Field(examples=["Usman"], max_length=30)
    last_name: str = Field(examples=["Ghani"], max_length=30)
    role: Role


class LoginBody(AuthBaseModel):
    pass


class RegisterResponse(BaseModel):
    first_name: str
    last_name: str
    email: str
    role: Role
    is_email_verified: bool


class LoginResponse(BaseModel):
    access_token: str
    refresh_token: str
