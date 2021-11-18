FROM python:slim-buster

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt