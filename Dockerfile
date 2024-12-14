FROM python:3.13.1-alpine3.21

COPY requirements.txt ./

RUN apk update && apk add bash
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p workspace
WORKDIR ~/workspace