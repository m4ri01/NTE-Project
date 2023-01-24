FROM python:3.9-buster

WORKDIR /usr/src/app
COPY . ./
EXPOSE 5000
RUN apt-get install libmariadb-dev

RUN pip install --no-cache-dir -r requirements.txt
RUN chmod u+x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
# CMD ["sh", "-c", "sleep 5 &&flask run --host=0.0.0.0"]