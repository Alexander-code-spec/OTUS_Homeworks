# Запуск контейнера: docker run -p 8002:8000 my-app
FROM python:3.9-buster

WORKDIR /var/app

COPY app/requirement.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY app .

CMD uvicorn app:app --host=0.0.0.0 --port=8000