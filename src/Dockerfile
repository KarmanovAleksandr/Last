FROM python:3.11

# set working directory
WORKDIR /usr/src/src

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements .
RUN pip install --upgrade pip
RUN pip install -r requirements

# copy project
COPY . .

# set working directory
WORKDIR /usr/src