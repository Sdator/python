FROM python:alpine as test1
RUN echo -e "http://mirrors.aliyun.com/alpine/v3.8/main/\nhttp://mirrors.aliyun.com/alpine/v3.8/community/" > /etc/apk/repositories
RUN echo "========11111111111111==========="
RUN env


FROM python:alpine as test2
RUN echo "=======2222222222222222============"



FROM python:alpine as test3
RUN echo "========333333333333333==========="

