FROM python:3.8.12-slim-buster

RUN mkdir /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

EXPOSE 8000

COPY . /app

CMD ["python", "manage.py", "run", "--host", "0.0.0.0", "--port", "8000"]
