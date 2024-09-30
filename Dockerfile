FROM python:3.12-slim-bullseye

WORKDIR /app
COPY . /app

RUN pip3 install -r requirements.txt

EXPOSE 8080
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
