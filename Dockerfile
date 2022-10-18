FROM python:slim-buster
WORKDIR /code

COPY ./docker-requirements.txt /code/requirements.txt
RUN apt update
RUN apt install whois

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

