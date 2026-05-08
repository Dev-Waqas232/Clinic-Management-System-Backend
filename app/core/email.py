from fastapi_mail import (
    FastMail,
    ConnectionConfig,
    MessageSchema,
    MessageType,
    NameEmail,
)
from typing import List

from .config import settings

config = ConnectionConfig(
    MAIL_USERNAME=settings.EMAIL_USERNAME,
    MAIL_PASSWORD=settings.EMAIL_PASSWORD,
    MAIL_FROM=settings.EMAIL_USERNAME,
    MAIL_PORT=int(settings.EMAIL_PORT),
    MAIL_SERVER=settings.EMAIL_HOST,
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
)

fm = FastMail(config)


async def send_email(subject: str, body: str, recepient: List[NameEmail]):
    message = MessageSchema(
        subject=subject, recipients=recepient, body=body, subtype=MessageType.html
    )

    try:
        await fm.send_message(message)
    except Exception as e:
        print(f"Email sending failed: {e}")
