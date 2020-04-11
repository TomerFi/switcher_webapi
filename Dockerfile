FROM python:3.8.2

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
org.opencontainers.image.ref.name=v$VERSION \
org.opencontainers.image.title="tomerfi/switcher_webapi" \
org.opencontainers.image.description="Unofficial WebAPI integration with the switcher water heater."

RUN ln -fs /usr/share/zoneinfo/$TIMEZONE /etc/localtime

WORKDIR /srv/switcher_webapi

COPY LICENSE \
pyscripts/consts.py \
pyscripts/helpers.py \
pyscripts/mappings.py \
pyscripts/request_handlers.py \
pyscripts/start_server.py \
requirements.txt ./

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["/bin/sh", "-c", "python -u start_server.py -p 8000"]
