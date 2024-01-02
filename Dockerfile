FROM python:3.12-slim

WORKDIR /github/workspace

COPY . .

RUN pip install -U pip -r requirements.txt

CMD [ "entrypoint.sh" ]
