FROM    python:3.7.0

ENV     STACKY_API_PORT=5000

COPY    app.py /
COPY    engine.py /
COPY    requirements.txt /

RUN     pip install -r requirements.txt

EXPOSE  5000

CMD     [ "python", "app.py" ]
