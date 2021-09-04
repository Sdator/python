FROM python:alpine
RUN echo -e "http://mirrors.aliyun.com/alpine/v3.8/main/\nhttp://mirrors.aliyun.com/alpine/v3.8/community/" > /etc/apk/repositories

RUN echo "========123==========="
RUN env
RUN echo "=======456============"
