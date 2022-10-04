FROM python:3.8.3-alpine

WORKDIR /app

COPY ./MainScores.py ./Utils.py ./Scores.txt /app/

RUN pip install flask
RUN pip install selenium
RUN pip install install webdriver-manager

EXPOSE 80
EXPOSE 8777

CMD ["python", "/app/MainScores.py"]
