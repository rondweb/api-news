FROM python:3.10-alpine as base
FROM base as builder
# RUN apk --update add --no-cache g++
# RUN pip install numpy

RUN mkdir /install

WORKDIR /install

COPY requirements.txt /requirements.txt

RUN pip install --prefix=/install -r /requirements.txt --upgrade

FROM base

COPY --from=builder /install /usr/local

RUN mkdir /app
COPY *.py /app

WORKDIR /app

EXPOSE 80

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]