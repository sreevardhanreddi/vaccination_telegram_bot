# pull official base image
FROM python:3.8-alpine

# set work directory
RUN mkdir /app
WORKDIR /app

RUN apk update && apk add gcc python3-dev musl-dev

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy entire code
COPY . .

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT [ "python" , "main.py" ]