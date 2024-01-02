FROM python:3.12-slim

COPY . /action

WORKDIR /action

RUN pip install -U pip -r requirements.txt

CMD [ "entrypoint.sh" ]
