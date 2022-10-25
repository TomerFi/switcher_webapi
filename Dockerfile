FROM python:3.11.0-slim

ARG TIMEZONE="Asia/Jerusalem"

RUN ln -fs /usr/share/zoneinfo/$TIMEZONE /etc/localtime

WORKDIR /usr/switcher_webapi

COPY LICENSE app/webapp.py requirements.txt ./

RUN pip install -U pip

RUN AIOHTTP_NO_EXTENSIONS=1 \
    FROZENLIST_NO_EXTENSIONS=1 \
    MULTIDICT_NO_EXTENSIONS=1 \
    YARL_NO_EXTENSIONS=1 \
    pip install -r requirements.txt

EXPOSE 8000

ENV LOG_LEVEL=INFO

CMD ["/bin/sh", "-c", "python webapp.py -p 8000 -l $LOG_LEVEL"]

ARG BUILD_DATE
ARG VCS_REF
ARG VERSION

LABEL org.opencontainers.image.created=$BUILD_DATE \
org.opencontainers.image.authors="Tomer Figenblat <mailto:tomer.figenblat@gmail.com>" \
org.opencontainers.image.url="https://hub.docker.com/r/tomerfi/switcher_webapi" \
org.opencontainers.image.documentation="https://switcher-webapi.tomfi.info" \
org.opencontainers.image.source="https://github.com/TomerFi/switcher_webapi" \
org.opencontainers.image.version=$VERSION \
org.opencontainers.image.revision=$VCS_REF \
org.opencontainers.image.vendor="https://switcher.co.il/" \
org.opencontainers.image.licenses="Apache-2.0" \
org.opencontainers.image.ref.name=$VERSION \
org.opencontainers.image.title="tomerfi/switcher_webapi" \
org.opencontainers.image.description="Containerized web service integrating with Switcher devices"
