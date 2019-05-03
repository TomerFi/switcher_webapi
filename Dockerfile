FROM python:3.7.3-stretch

ARG timezone='Asia/Jerusalem'

RUN ln -fs /usr/share/zoneinfo/$timezone /etc/localtime

WORKDIR /srv/switcher_webapi

COPY pyscripts/*.py requirements.txt ./

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["/bin/sh", "-c", "python -u start_server.py -p 8000"]
