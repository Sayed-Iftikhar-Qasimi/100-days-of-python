import random
from game_data import data
import os
from art import logo, vs


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(user_guess, a_follower, b_followers):

    if a_follower > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"


print(logo)

score = 0
should_game_continue = True
account_b = random.choice(data)

while should_game_continue:
    account_a = account_b
    account_b = random.choice(data)

    while account_a==account_b:
        b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'a' or 'b': ")
    clear_screen()
    print(logo)

    a_follower_account = account_a["follower_count"]
    b_follower_account = account_b["follower_count"]

    result = check_answer(guess, a_follower_account, b_follower_account)

    if result:
        score += 1
        print(f"Your right, current score: {score}")
        
    else:
        print(f"Sorry, that's wrong. Final score {score}")
        should_game_continue = False
