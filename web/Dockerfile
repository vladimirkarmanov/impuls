FROM python:3.8.3-alpine

WORKDIR /home/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APP_HOME=/home/app/src

RUN apk update \
    && apk add --virtual .build-deps gcc g++ python3-dev musl-dev \
    && apk add --no-cache mariadb-dev libpq zlib-dev jpeg-dev

RUN pip install --upgrade pip setuptools
RUN pip install mysqlclient

COPY ./requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

RUN apk del .build-deps

WORKDIR $APP_HOME

COPY ./src $APP_HOME
