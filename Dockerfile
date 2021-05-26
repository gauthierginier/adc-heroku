FROM python:3.6-buster
WORKDIR /adc-heroku
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install uwsgi-plugin-python -y
COPY . .
CMD ["uwsgi","app.ini"]