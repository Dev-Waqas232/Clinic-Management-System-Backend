import asyncio
from fastapi_mail import NameEmail

from app.core.celery import app
from app.core.email import send_email


@app.task
def email_tasks(subject: str, body: str, email: str, name: str):
    recepient = [NameEmail(email=email, name=name)]
    asyncio.run(send_email(subject, body, recepient))
