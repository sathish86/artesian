FROM python:3.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD /requirements/base.txt /code/
ADD /requirements/requirements_dev.txt /code/
RUN pip install -r requirements_dev.txt
ADD . /code/
