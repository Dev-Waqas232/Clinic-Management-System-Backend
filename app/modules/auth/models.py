from datetime import datetime, timezone
import uuid
from sqlalchemy import UUID, Boolean, DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base


class Auth(Base):
    __tablename__ = "auth"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), default=uuid.uuid4, primary_key=True
    )
    is_email_verified: Mapped[bool] = mapped_column(Boolean(), default=False)
    password_hash: Mapped[str] = mapped_column(String())
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id")
    )

    otp: Mapped[int | None] = mapped_column(default=None)
    otp_expires_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), default=None
    )
