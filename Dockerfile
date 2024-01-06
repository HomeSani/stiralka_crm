FROM python:3.11.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

ADD pyproject.toml /code/

RUN pip install poetry
RUN poetry install

ADD . /code
