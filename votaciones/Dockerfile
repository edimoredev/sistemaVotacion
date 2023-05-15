FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1


RUN apk update \
  && apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev \
  && pip install --upgrade pip

RUN mkdir /votaciones

WORKDIR /votaciones


COPY requirements.txt /votaciones/
RUN pip install -r requirements.txt


COPY . /votaciones/
