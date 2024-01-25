FROM python:3.12.1

RUN pip install mysqlclient && \
    mkdir /project

WORKDIR /project

CMD [ "/usr/local/bin/python", "/project/main.py" ]
