# FROM alpine
FROM python:alpine

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# RUN echo -e "http://mirrors.aliyun.com/alpine/v3.8/main/\nhttp://mirrors.aliyun.com/alpine/v3.8/community/" > /etc/apk/repositories \
# /etc/apk/repositories
# http://dl-cdn.alpinelinux.org/alpine/v3.11/main
# http://dl-cdn.alpinelinux.org/alpine/v3.11/community
# 直接替换镜像地址 因为根据内核版本是会改变的
RUN sed -i -e 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/' /etc/apk/repositories \
    && apk --update add --no-cache \
        # libuuid \
        # gcc \
        # libc-dev \
        # linux-headers \
        # make  \
        # automake   \
        # g++  \
        # python3-dev \
        sudo \
        # bash \
        git \
        openssh \
        # curl \
        # python3 \
    # && curl https://bootstrap.pypa.io/get-pip.py| python3 - \
    # 安装pylint 代码检测
    && pip --disable-pip-version-check --no-cache-dir install pylint -i https://mirrors.aliyun.com/pypi/simple/ \
    # 添加用户组
    && addgroup -g $USER_GID $USERNAME \
    # 添加用户
    && adduser -s /bin/sh -u $USER_UID -G $USERNAME -D $USERNAME \
    # 设置用户权限
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME
