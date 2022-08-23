import time

from random import randint


# Generaetes a list and prints to screen
def generate_sequence(difficulty):
    random_num_list = []
    clear_terminal = lambda: print('\n' * 15)
    for num in range(1, difficulty + 1):
        rand_num = randint(1, 101)
        print(rand_num)
        time.sleep(0.7)
        clear_terminal()
        random_num_list.append(rand_num)
    return random_num_list


# get input from user and puts in a list
def get_list_from_user(difficulty):
    user_list = []
    for num in range(1, difficulty + 1):
        user_nums = int(input("Insert number: "))
        user_list.append(user_nums)
    return user_list


# compares both lists
def is_list_equal(random_num_list, user_list):
    if random_num_list == user_list:
        return True
    else:
        return False


# plays above functions
def play(difficulty):
    computer_generated_list = generate_sequence(difficulty)
    user_list = get_list_from_user(difficulty)
    result = is_list_equal(computer_generated_list, user_list)
    return print(
        f'Won: {result}, numbers you gave: {user_list}, numbers that were displayed: {computer_generated_list}')
