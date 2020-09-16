FROM python:3.8.5-alpine

WORKDIR /home/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APP_HOME=/home/app/src

RUN apk update \
    && apk add --virtual .build-deps gcc g++ python3-dev \
    && apk add --no-cache --update postgresql-dev libpq zlib-dev jpeg-dev

RUN pip install --upgrade pip setuptools

COPY ./requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

RUN apk del .build-deps

WORKDIR $APP_HOME

COPY . $APP_HOME
