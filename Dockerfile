FROM python:3

WORKDIR /app

ADD api.py .

RUN python -m pip install --upgrade pip
RUN pip install wheel
RUN pip install flask
EXPOSE 5000

CMD ["python", "api.py"]
