FROM python:3.6-buster
WORKDIR /poc-desktop
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uwsgi","app.ini"]