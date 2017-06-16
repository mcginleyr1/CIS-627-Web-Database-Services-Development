FROM python:latest
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt

EXPOSE 8000

RUN pip install -r requirements.txt

RUN mkdir /var/djangoproject

WORKDIR /var/djangoproject

