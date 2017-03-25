FROM python:latest

COPY requirements.txt requirements.txt

EXPOSE 8000

RUN pip install -r requirements.txt

RUN mkdir /var/djangoproject

WORKDIR /var/djangoproject

