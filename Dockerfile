FROM python:3.6.10-stretch

LABEL maintainer="radzikowskikacper@gmail.com"
LABEL VERSION="0.1"

ADD . /server
ADD manage.py /server
WORKDIR /server

RUN apt-get update && apt-get install -y postgresql-client

RUN groupadd -g 999 appuser && \
    useradd -r -u 999 -g appuser appuser && \
    chmod -R 777 /server

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

USER appuser

ARG BACKEND_PORT=8000
ENV BACKEND_PORT ${BACKEND_PORT}
EXPOSE $BACKEND_PORT

# CMD python manage.py runserver 0.0.0.0:${BACKEND_PORT}
CMD ./init.sh ${BACKEND_PORT}