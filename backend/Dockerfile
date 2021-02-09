FROM python:3.8.6-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /backend

COPY pyproject.toml poetry.lock /backend/

RUN pip install -U pip \
    && pip install --no-cache poetry

RUN poetry config virtualenvs.create false \
    && poetry install --no-root
