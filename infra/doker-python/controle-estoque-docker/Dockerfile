FROM python:3.7-slim-buster
MAINTAINER Jonatas Oliveira

ENV PYTHONUNBUFFERED 1

RUN apt update && \
    apt install -y libjpeg-dev zlib1g-dev python3-dev build-essential

RUN mkdir /src
WORKDIR /src
COPY ./requirements.txt /requirements.txt

RUN pip install pip --upgrade && pip install -r /requirements.txt

