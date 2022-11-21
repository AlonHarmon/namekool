FROM python:buster

RUN pip install -r requirements.txt

CMD main.py
