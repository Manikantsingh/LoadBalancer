#FROM python:3-alpine
FROM ubuntu:latest

MAINTAINER Manikant

COPY app /app

WORKDIR /app

RUN apt-get update \
    && apt-get install -y python3 \
    && apt-get install -y python3-pip

RUN pip3 install -r requirements.txt

CMD ["python3", "app.py" , "&"]