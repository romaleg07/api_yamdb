# https://docs.docker.com/engine/reference/builder/#from documentation

FROM python:3.7-slim

LABEL author="Romaleg" version=1 descrtiption="Trying new stuff. Docker is awesome"

RUN mkdir app/

COPY requirements.txt app/

RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY . /app

WORKDIR /app

CMD [ "gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]