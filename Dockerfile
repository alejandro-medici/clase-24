FROM python:3.11.0a6-slim-buster

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt