from art import logo
import os

print(logo)
auction_data = {}


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


is_continue = True
while is_continue:
    name = input("What is Your name?: ")
    bid = int(input("What is your bid?: "))

    auction_data[name] = bid

    next_bid = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if next_bid == "no":
        is_continue = False
    else:
        clear_screen()


highest_bidder = max(auction_data, key=auction_data.get)

print(f"The winner is {highest_bidder} with a bid of ${auction_data[highest_bidder]}")