FROM lambci/lambda:python3.8

USER root

COPY ./requirements.txt /tmp/requirements.txt

RUN pip3 install -r /tmp/requirements.txt
