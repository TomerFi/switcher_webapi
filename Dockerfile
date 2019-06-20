FROM python:3.7.3-stretch

ARG BUILD_DATE
ARG VCS_REF
ARG VERSION

ARG TIMEZONE="Asia/Jerusalem"

LABEL org.label-schema.build-date=$BUILD_DATE \
org.label-schema.name="tomerfi/switcher_webapi" \
org.label-schema.description="Unofficial WebAPI integration with the switcher water heater." \
org.label-schema.url="https://hub.docker.com/r/tomerfi/switcher_webapi" \
org.label-schema.vcs-url="https://github.com/TomerFi/switcher_webapi" \
org.label-schema.vcs-ref=$VCS_REF \
org.label-schema.version=$VERSION \
org.label-schema.schema-version="1.0" \
org.label-schema.docker.cmd="\
docker run -d -p 8000:8000 \
-e CONF_DEVICE_IP_ADDR=192.168.100.157 \
-e CONF_PHONE_ID=1234 \
-e CONF_DEVICE_ID=ab1c2d \
-e CONF_DEVICE_PASSWORD=12345678 \
-e CONF_THROTTLE=5.0 \
--name switcher_webapi tomerfi/switcher_webapi:latest" \
org.label-schema.docker.params="\
CONF_DEVICE_IP_ADDR=string static ip address of the device \
CONF_PHONE_ID=string phone id from your device \
CONF_DEVICE_ID=string device's id \
CONF_DEVICE_PASSWORD=string device's password \
CONF_THROTTLE=float throttle time between consecutive requests - default is 5.0" \
license="MIT" \
maintainer="Tomer Figenblat <tomer.figenblat@gmail.com>" \
manufacturer-url="https://switcher.co.il/" \
community-url="https://www.dockeril.net/"

RUN ln -fs /usr/share/zoneinfo/$TIMEZONE /etc/localtime

WORKDIR /srv/switcher_webapi

COPY LICENSE \
pyscripts/conftest.py \
pyscripts/consts.py \
pyscripts/helpers.py \
pyscripts/mappings.py \
pyscripts/request_handlers.py \
pyscripts/start_server.py \
requirements_prod.txt \
requirements.txt ./

RUN pip install -r requirements_prod.txt -c requirements.txt

EXPOSE 8000

CMD ["/bin/sh", "-c", "python -u start_server.py -p 8000"]
