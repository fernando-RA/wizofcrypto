FROM python:3.7
RUN echo "PRINT "

ARG DEBIAN_FRONTEND=noninteractive
# Allow SECRET_KEY to be passed via arg so collectstatic can run during build time
ARG SECRET_KEY
RUN echo "deb https://deb.debian.org/debian buster main" > /etc/apt/sources.list
RUN apt-get update && apt-get -y dist-upgrade
RUN apt install -y curl git gcc libpq-dev vim

WORKDIR /code
COPY . .
RUN python -m pip install --upgrade pip
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
RUN pip install -r requirements.txt

CMD waitress-serve --port=8000 backend.wsgi:application