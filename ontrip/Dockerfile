FROM python:3.9

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH="${PYTHONPATH}:/code/"

RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/

RUN pip install --no-cache-dir -r requirements.txt

ADD . /code/

RUN apt-get update && apt-get install vim -y

RUN chmod +x ./start.sh

EXPOSE 8080

CMD ["./start.sh"]