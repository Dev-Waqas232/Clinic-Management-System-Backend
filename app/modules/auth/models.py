from datetime import datetime, timezone
import uuid
from sqlalchemy import UUID, Boolean, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base


class Auth(Base):
    __tablename__ = "auth"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    password: Mapped[str] = mapped_column(String())
    is_email_verified: Mapped[bool] = mapped_column(Boolean(), default=False)
    password_hash: Mapped[str] = mapped_column(String())
    created_at: Mapped[datetime] = mapped_column(DateTime(),default=lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(DateTime(),default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

