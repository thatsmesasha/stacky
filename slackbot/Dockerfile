FROM    python:3.7.0

ARG     SLACK_SIGNING_SECRET
ARG     SLACK_BOT_TOKEN

ENV     SLACK_APP_PORT=3000
ENV     SLACK_SIGNING_SECRET=$SLACK_SIGNING_SECRET
ENV     SLACK_BOT_TOKEN=$SLACK_BOT_TOKEN

COPY    app.py /
COPY    requirements.txt /

RUN     pip install -r requirements.txt

EXPOSE  3000

CMD     [ "python", "app.py" ]
