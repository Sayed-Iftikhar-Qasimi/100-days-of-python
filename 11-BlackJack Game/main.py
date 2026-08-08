import random
import os
from art import logo

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    score = sum(cards)
    length = len(cards)

    if length == 2 and score == 21:
        return 0

    elif 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)

    return score

def compare(computer_score, user_score):

    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, Opponent has Blackjack."
    elif user_score == 0:
        return "Win with a Blackjack."
    elif user_score > 21:
        return "You went over, you lose."
    elif computer_score > 21:
        return "Opponent went over, you win."
    else:
        if computer_score > user_score:
            return "You lose"
        elif user_score > computer_score:
            return "You Won"


def play():
    user_cards = []
    computer_cards = []

    for _ in range(0,2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    user_score = -1
    computer_score = -1

    is_game_over = False
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        if computer_score == 0  or user_score == 0 or user_score > 21:
            is_game_over = True
        else:
            print(f"\tYour Cards: {user_cards}, current score: {calculate_score(user_cards)}")
            print(f"\tComputer first card: {computer_cards[0]}")

            draw_another_card = input("Would you like to draw another card? (Y/N): ").lower()
            if draw_another_card == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score: {calculate_score(computer_cards)} ")

    print(compare(computer_score, user_score))



while True:
        user_choice = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if user_choice == 'y':
            clear_screen()
            print(logo)
            play()
        else:
            break
