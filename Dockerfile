FROM frolvlad/alpine-python3
MAINTAINER Henrique Lopes

ENV PYTHONUNBUFFERED 1
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN mkdir /small_gateway
WORKDIR /small_gateway

ADD . /small_gateway/

# Installing project dependencies.
RUN pip install -U pip
RUN pip install -r requirements.txt
RUN pip install -r requirements_dev.txt
