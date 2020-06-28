FROM python:3-alpine

RUN mkdir -p /usr/src/app

RUN apk add build-base libffi-dev openssl-dev

WORKDIR /usr/src/app
COPY . /usr/src/app

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["/bin/sh", "start.sh"]
