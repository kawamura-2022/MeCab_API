# Base Image
FROM ubuntu:18.04

# Python pipenv
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

COPY ./webapp/requirements.txt /projects/
WORKDIR /projects

RUN apt-get -y update && apt-get install -y --no-install-recommends \
         wget \
         swig \
         python3 \
         python3-dev \
         nginx \
         git \
         make \
         curl \
         sudo \
         gcc \
         g++ \
    && rm -rf /var/lib/apt/lists/*

RUN wget --no-check-certificate https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py  && python3 get-pip.py  && pip install -U pip


#mecab
RUN apt-get update \
  && apt-get install -y mecab \
  && apt-get install -y mecab-ipadic \
  && apt-get install -y libmecab-dev \
  && apt-get install -y mecab-ipadic-utf8

RUN pip install -r ./requirements.txt
