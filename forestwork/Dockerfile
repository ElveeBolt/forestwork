# syntax=docker/dockerfile:1

FROM python

WORKDIR /forestwork

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .