import os
from art import logo

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print("+\n-\n*\n/")
    return 0

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

print(logo)


operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

is_continue = True
is_continue_with_previous = False
result = 0

while is_continue:

    if is_continue_with_previous:
        num1 = result
    else:
        num1 = float(input("What's your first number? "))

    operation = input("+ \n- \n* \n/\nPick an operation: ")

    num2 = float(input("What's the next number? "))

    result = operations[operation](num1, num2)
    print(f"{num1} {operation} {num2} = {result}")

    choice = input(f"Type 'y' to  continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

    if choice == "y":
        is_continue_with_previous = True
    else:
        clear_screen()
        print(logo)

