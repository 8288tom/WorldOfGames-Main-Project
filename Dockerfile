FROM python:3-alpine

WORKDIR /app

COPY ./MainScores.py ./Utils.py /app/
COPY ./Scores.txt /Scores.txt 

RUN pip install flask
RUN pip install selenium
RUN pip install chromedriver-autoinstaller

EXPOSE 80
EXPOSE 8777

CMD ["python", "/app/MainScores.py"]
