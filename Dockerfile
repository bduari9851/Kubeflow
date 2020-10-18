FROM python:3.7
RUN python3 -m pip install keras
COPY ./test.py /src/test.py