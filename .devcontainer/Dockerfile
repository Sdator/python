FROM python:alpine

# COPY requirements.txt /tmp/pip-tmp/
RUN echo -e "http://mirrors.aliyun.com/alpine/v3.8/main/\nhttp://mirrors.aliyun.com/alpine/v3.8/community/" > /etc/apk/repositories \
    apk update \
    && apk install git \
    && pip --disable-pip-version-check --no-cache-dir install pylint

    # && pip --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt