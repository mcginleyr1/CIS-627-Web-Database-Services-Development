FROM python:latest
ADD . /code
WORKDIR /code
RUN apt-get install libmysqlclient-dev
RUN pip install -r requirements.txt
CMD ["python", "app.py"]