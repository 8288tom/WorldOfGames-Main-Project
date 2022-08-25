import requests as r
from random import randint

# Sends an API call to receieve USD and ILS currency and returns random number, get response and an interval
def get_money_interval(difficulty):
    to = 'ILS'
    base = 'USD'
    random_num = randint(1, 101)
    header = {"apikey": "bBDWsGC7Z2EOuWCUW7DqWwpD74M06acp"}
    endpoint = f"https://api.apilayer.com/fixer/convert?to={to}&from={base}&amount={random_num}"
    request_json = r.get(endpoint, headers=header).json()
    t = request_json['result']
    d = difficulty
    interval = (t - (5 - d), t + (5 - d))
    return interval, request_json, random_num,t

# inputs the user for a number
def get_guess_from_user():
    guess = int(input("How much is it in ILS? "))
    return guess

# receives difficulty from Live.py and compares the input vs result
def play(difficulty):
    api_response = get_money_interval(difficulty)
    print(f"It's time to guess how many Shekels are: {api_response[2]}$, "
          f"the range of error depends on the difficulty level chosen ")
    guess = get_guess_from_user()
    if api_response[0][0] < guess < api_response[0][1]:
        print(f"You're right, {api_response[2]}$ are {api_response[3]}₪ in ILS")
        return 1
    else:
        print(f"Wrong!, the amount in ILS is: {api_response[3]}")
        return 0




