web: uvicorn app.main:app --host 0.0.0.0 --port $PORT
worker: celery -A app.core.celery:app worker --loglevel=info
