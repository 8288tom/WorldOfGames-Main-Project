from flask import Flask, request
from Utils import SCORES_FILE_NAME

app = Flask("something")
with open(SCORES_FILE_NAME, 'r') as f:
    SCORE = f.readline()


@app.route('')
def my_func():
    body = f'<html><head><title>Scores Game</title></head><body><h1>The score is <div id="score">{SCORE}</div></h1></body></html>'
    return body


app.run(host="0.0.0.0", port=5001, debug=False)
