FROM python:3.7
RUN pip install --upgrade pip

EXPOSE 8000

WORKDIR /app

ADD requirements.txt /app/
RUN pip install -r requirements.txt

ADD . /app

CMD [ "uvicorn", "app:app", "--port", "8000", "--host", "0.0.0.0" ]