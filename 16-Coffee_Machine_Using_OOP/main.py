from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
menu = Menu()
coffee_maker = CoffeeMaker()
item_costs = {"latte":2.5,"espresso":1.90, "cappuccino":3.5}

is_on = True
while is_on:
    options = menu.get_items()
    user_choice = input(f"What would you like?: {options}: ").lower()

    if user_choice == "off":
        print("Exit...")
        is_on = False
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_choice)

        if drink != None:
            resources_sufficient = coffee_maker.is_resource_sufficient(drink)

            if resources_sufficient:
                drink_cost = item_costs[user_choice]
                payment = money_machine.make_payment(drink_cost)

                if payment:
                    coffee_maker.make_coffee(drink)

