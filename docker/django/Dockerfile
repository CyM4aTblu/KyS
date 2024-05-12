FROM python:3.10.14-slim-bookworm

WORKDIR /app

COPY pyproject.toml .

RUN pip install .

COPY manage.py rights_verification_system access ./

CMD gunicorn --workers=4 -b=0.0.0.0:$PORT rights_verification_system.wsgi:application