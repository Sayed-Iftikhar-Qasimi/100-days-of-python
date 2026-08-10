def report(available_resources,money):
    print(f"Water: {available_resources["water"]}")
    print(f"Milk: {available_resources["milk"]}")
    print(f"Coffee: {available_resources["coffee"]}")
    print(f"Money: {money}")

def process_coins(cost, order_drink):

    print("Please Insert coins.")
    quarters = int(input("how many quarters? "))
    dimes = int(input("how many dimes? "))
    nickles = int(input("how many nickles? "))
    pennies = int(input("how many pennies? "))

    total_money = ((quarters*0.25) + (dimes*0.10) + (nickles*0.05) + (pennies*0.01))
    change = total_money - cost
    return change

def check_resources(available_resources,menu, drink):

    for item in available_resources:
        if MENU[drink]["ingredients"][item] > available_resources[item]:
            print(f"Sorry there is not enough {item}")
            return 0
    return 1

def deduct_resources(avilable_resources, menu, drink):
    for item in avilable_resources:
        avilable_resources[item] -= menu[drink]["ingredients"][item]


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk" : 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}




profit = 0
while True:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "report":
        report(resources, profit)
    elif user_choice == "off":
        print("The coffee machine is now off. Thank you for using the coffee machine! ☕")
        break
    else:
        is_sufficient_resources = check_resources(resources,MENU,user_choice)
        if is_sufficient_resources:
            drink_cost = MENU[user_choice]["cost"]
            change = process_coins(drink_cost, user_choice)
            if change>=0:
                print(f"Here is ${round(change,2)} in change.")
                print(f"Here is your {user_choice} ☕️. Enjoy!")
                deduct_resources(resources, MENU, user_choice)
                profit += drink_cost
            else:
                print(f"Sorry that's not enough money. Money refunded.")


