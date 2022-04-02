FROM python:3.8-slim

COPY requirements.txt /
RUN pip install -r requirements.txt

COPY . /app

ENV PORT 5050

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app