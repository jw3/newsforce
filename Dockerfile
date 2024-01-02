FROM python:3.12-slim

COPY . /action

RUN pip install -U pip -r /action/requirements.txt

CMD [ "/action/entrypoint.sh" ]
