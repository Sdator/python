FROM alpine:3.10

ENV DEBIAN_FRONTEND=noninteractive

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN sed -i -e 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/' /etc/apk/repositories\
    && apk --update add --no-cache \
        libuuid \
        gcc \
        libc-dev \
        linux-headers \
        make  \
        automake   \
        g++  \
        python3-dev \
        sudo \
        bash \
        git \
        curl \
        python3 \
    && curl https://bootstrap.pypa.io/get-pip.py| python3 - \
    && pip --disable-pip-version-check --no-cache-dir install pylint -i https://mirrors.aliyun.com/pypi/simple/ \
    && addgroup -g $USER_GID $USERNAME \
    && adduser -s /bin/bash -u $USER_UID -G $USERNAME -D $USERNAME \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# VOLUME [ "/workspace" ]

ENV DEBIAN_FRONTEND=