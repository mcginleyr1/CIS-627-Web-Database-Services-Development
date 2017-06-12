FROM python:latest
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt

EXPOSE 8000

RUN pip install -r requirements.txt
RUN apt-get install libmysqlclient-dev

RUN mkdir /var/djangoproject/tango_with_django_project

WORKDIR /var/djangoproject/tango_with_django_project

