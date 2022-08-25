from flask import Flask, request
from Utils import SCORES_FILE_NAME

app = Flask("something")


@app.route('/')
def score_server():
    with open(SCORES_FILE_NAME, 'r') as f:
        SCORE = f.readline()

    if SCORE == '':
        error = '<html><head><title>Scores Game</title></head>' \
                '<body>' \
                '<body>' \
                '<h1>' \
                '<div id="score" style="color:red">{ERROR}</div>' \
                '</h1>' \
                '</body>' \
                '</html>'
        return error
    elif SCORE:
        body = f'<html><head><title>Scores Game</title></head>' \
               f'<body style="background-color:ivory ;padding-top:330px;">' \
               f'<h1 style="text-align:center;margin:auto;font-size:700%;background-color:#6EA1DB;color:#F0494A;border-radius:50px;font-family:Arial; width:1000px">' \
               f'The Score is: <div id="score" style="color:#000000";>{SCORE}</div><' \
               f'/h1>' \
               f'</body>' \
               f'</html>'
        return body



app.run(host="0.0.0.0", port=5001, debug=True)
