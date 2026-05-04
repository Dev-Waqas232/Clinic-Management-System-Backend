from datetime import datetime, timezone
import enum
import uuid
from sqlalchemy import UUID, Boolean, Enum,  String
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base 


class Role(enum.Enum):
    ADMIN = "admin"
    CLINIC = "clinic"
    DOCTOR = "doctor"
    PATIENT = "patient"

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True),primary_key=True, default=uuid.uuid4)
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(),unique=True, index=True)
    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(onupdate=lambda: datetime.now(timezone.utc), default=lambda: datetime.now(timezone.utc))
    is_active: Mapped[bool] = mapped_column(Boolean(), default=False)
    role: Mapped[Role] = mapped_column(Enum(Role), default=Role.PATIENT)

