FROM python:3.10

ENV APP_HOME=/app

WORKDIR $APP_HOME

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT ["python", "main.py"]
