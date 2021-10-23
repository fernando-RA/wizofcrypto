FROM python:3.7

ARG DEBIAN_FRONTEND=noninteractive

# Allow SECRET_KEY to be passed via arg so collectstatic can run during build time
ARG SECRET_KEY
RUN echo "deb https://deb.debian.org/debian buster main" > /etc/apt/sources.list
RUN apt-get update && apt-get -y dist-upgrade
RUN apt install -y curl git gcc libpq-dev vim

WORKDIR /opt/webapp
COPY . .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt