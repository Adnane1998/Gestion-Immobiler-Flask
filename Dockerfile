FROM python:3.9.10-alpine
WORKDIR /app
ADD . /app
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev



RUN pip install -r requirements.txt
RUN apk del build-deps
EXPOSE 5000
CMD ["python","app.py"]