FROM python:3.12-slim

ENV PATH "${PATH}:/github/workspace"

WORKDIR /github/workspace

COPY . .

RUN pip install -U pip -r requirements.txt

RUN ls -al

CMD [ "entrypoint.sh" ]
