FROM python:alpine as test

RUN echo -e "http://mirrors.aliyun.com/alpine/v3.8/main/\nhttp://mirrors.aliyun.com/alpine/v3.8/community/" > /etc/apk/repositories \
    && apk update \
    && apk add git \
    && pip --disable-pip-version-check --no-cache-dir install pylint -i https://mirrors.aliyun.com/pypi/simple/
