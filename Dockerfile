FROM python:latest

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN mkdir /var/djangoproject

WORKDIR /var/djangoproject

