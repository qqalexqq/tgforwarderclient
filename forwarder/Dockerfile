FROM python:latest

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade -r requirements.txt

COPY . /app

CMD [ "python3", "/app/main.py" ]
