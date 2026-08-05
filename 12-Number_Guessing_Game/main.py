import os
import random
from art import logo

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def generateRandomNumber():
    number = random.randint(1,100)
    return number

def determineDifficulty():
    """ASk the user for a difficulty, and keeping asking until it's valid"""

    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

        if difficulty == "easy":
            print(f"Easy Mode Activated! You have 10 attempts. Use them wisely and try to win!\n")
            return 10
        elif difficulty == "hard":
            print(f"Hard Mode Activated! You have 5 attempts. Use them wisely and try to win!\n")
            return 5
        else:
            print("Please type 'easy' or 'hard' \n")


def get_guess():

    while True:
        try:
            return int(input("Guess a number: "))
        except ValueError:
            print("That's not a valid. Try again.\n")



def play_game():

    print(logo)

    random_number = generateRandomNumber()
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    attempts = determineDifficulty()

    guess = int(input("Make a guess: "))

    while True:

        if guess == random_number:
            print(f"You got it! The answer was {random_number}.")
            return

        attempts -= 1

        if attempts == 0:
            print("You've run out of guesses. Refresh the page to run again.")
            return

        print("Too high" if guess > random_number else "Too low")
        print(f"You have {attempts} guesses remaining\n")
        guess = get_guess()

   

while True: 
    play_game()
    replay = input("\nDo you want to play again. Type 'y' or 'n': ").lower()
    if replay == "y":
        clear_screen()
    else:
        print("Thanks for playing! Goodbye!")
        break




