FROM python:3.9
MAINTAINER soodabe@localhost

WORKDIR /app

COPY ./app/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app

EXPOSE 8000

CMD ["gunicorn", "TextClassification.wsgi", "-b 0.0.0.0:8000"]