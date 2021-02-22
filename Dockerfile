FROM python:slim

RUN apt-get update && apt-get install -y --no-install-recommends gcc build-essential

WORKDIR /src
COPY . .
RUN pip install -r requirements.txt

CMD ["gunicorn"," rockument.asgi:application", "-k", "uvicorn.workers.UvicornWorker"]