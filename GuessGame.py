from random import randint


# Difficulty is given on Live.py>load_game()

# Generates a number
def generate_number(difficulty):
    return randint(1, difficulty + 1), difficulty + 1


# Input from user between 1 to Difficulty
def get_guess_from_user(difficulty):
    return int(input(f'Choose a number from 1 to {str(difficulty)}:'))


# Compares reuslts between get_guess_from_user and generate_number
def compare_result(user_guess, secret_number):
    x = 0
    while x != 1:
        if user_guess == secret_number:
            x = 1
            print(f'Secret number was: {secret_number}, Your guess: {user_guess}')
            return True
        else:
            return False


# Runs above functions
def play(difficulty):
    secret_number = generate_number(difficulty)
    difficulty = secret_number[1]
    user_guess = get_guess_from_user(difficulty)
    result = compare_result(user_guess, secret_number[0])
    if result:
        return 1
    else:
        return 0