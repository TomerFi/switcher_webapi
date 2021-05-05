FROM python:3.9.5

ARG BUILD_DATE
ARG VCS_REF
ARG VERSION

ARG TIMEZONE="Asia/Jerusalem"

LABEL org.opencontainers.image.created=$BUILD_DATE \
org.opencontainers.image.authors="Tomer Figenblat <mailto:tomer.figenblat@gmail.com>" \
org.opencontainers.image.url="https://hub.docker.com/r/tomerfi/switcher_webapi" \
org.opencontainers.image.documentation="https://switcher-webapi.tomfi.info" \
org.opencontainers.image.source="https://github.com/TomerFi/switcher_webapi" \
org.opencontainers.image.version=$VERSION \
org.opencontainers.image.revision=$VCS_REF \
org.opencontainers.image.vendor="https://switcher.co.il/" \
org.opencontainers.image.licenses="MIT" \
org.opencontainers.image.ref.name=$VERSION \
org.opencontainers.image.title="tomerfi/switcher_webapi" \
org.opencontainers.image.description="Switcher Water Heater Unofficial REST API"

RUN ln -fs /usr/share/zoneinfo/$TIMEZONE /etc/localtime

WORKDIR /usr/switcher_webapi

COPY LICENSE requirements.txt ./

COPY switcher_webapi switcher_webapi

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["/bin/sh", "-c", "python -m switcher_webapi.start_server -p 8000"]
