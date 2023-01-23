FROM python:3.9-slim-buster

WORKDIR /usr/src/app
COPY . ./
EXPOSE 5000


RUN pip install --no-cache-dir -r requirements.txt
RUN flask db init
RUN flask db migrate
RUN flask db upgrade
CMD ["sh", "-c", "sleep 5 && flask run --host=0.0.0.0"]