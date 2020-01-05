
FROM python:alpine

COPY requirements.txt /tmp/pip-tmp/

RUN pip --disable-pip-version-check --no-cache-dir install pylint \
    && pip --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt