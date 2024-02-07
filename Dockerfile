FROM python:3.10-alpine

WORKDIR /code

RUN apk add --no-cache tzdata \
    && cp /usr/share/zoneinfo/Asia/Seoul /etc/localtime \
    && echo "Asia/Seoul" > /etc/timezone \
    && apk del tzdata

RUN pip install --no-cache-dir celery redis

# COPY ./app .