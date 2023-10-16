FROM python:3.9.6

RUN mkdir -p /user/src/app/
WORKDIR /user/src/app/

ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN pip install install fastapi uvicorn redis aiohttp fastapi_utils

COPY . /user/src/app/
