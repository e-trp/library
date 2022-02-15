
FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /webapp

RUN pip install --upgrade pip
RUN apt-get update \
    && apt-get -y install libpq-dev gcc

COPY requirements.txt /webapp/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /webapp