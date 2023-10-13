FROM python:3.11.1

RUN mkdir -p /user/src/app/
WORKDIR /user/src/app/

ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN pip install -r requirements.txt
