import GuessGame
import MemoryGame
import CurrencyRouletteGame
from pyfiglet import Figlet
import termcolor

def welcome(name):
    f= Figlet(font='starwars', width=250)
    name = str(name)
    greeting =f.renderText(f"Hello {name} and welcome\nto the World of Games\nHere you will find many cool games to play.")
    colored_greeting=termcolor.colored(greeting, "yellow")
    return colored_greeting


def print_games():
    game_selection = {
        "1": "1.Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back",
        "2": "2.Guess Game - guess a number and see if you chose like the computer",
        "3": "3.Currency  - try and guess the value of a random amount of USD in ILS "}
    print(game_selection['1'] + '\n' + game_selection['2'] + '\n' + game_selection['3'])


def check_difficulty(difficulty):
    if 0 < difficulty <= 5:

        return True
    else:
        print("That is not a valid number, don't play games with me!")
        return False


def load_game():
    print_games()
    x = 0
    while x == 0:
        try:
            user_input = int(input("Select a game to play: "))
            difficulty = int(input("Choose game difficulty between 1 to 5: "))
            check = check_difficulty(difficulty)
            if check:
                if user_input == 1 or user_input == "memory game":
                    MemoryGame.play(difficulty)
                    break
                elif user_input == 2 or user_input == "guess game":
                    GuessGame.play(difficulty)
                    break
                elif user_input == 3 or user_input == "currency":
                    CurrencyRouletteGame.play(difficulty)
                    break
                else:
                    print("That wasn't a valid choice, try again")
                    print_games()
            else:
                print_games()
        except:
            print("Please use a number next time")
