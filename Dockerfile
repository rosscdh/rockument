FROM python:slim

WORKDIR /src
COPY . .
RUN pip install -r requirements.txt

CMD ["gunicorn"," rockument.asgi:application", "-k", "uvicorn.workers.UvicornWorker"]