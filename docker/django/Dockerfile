FROM python:3.10.14-slim-bookworm

WORKDIR /app

COPY app/pyproject.toml .

RUN pip install .

COPY app .

CMD gunicorn --workers=4 -b=0.0.0.0:$PORT rights_verification_system.wsgi:application