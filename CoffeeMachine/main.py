# Todo: 1  test this
from typing import Dict

from machine import resources, MENU

machine_resource: dict[str, int] = resources


def print_report():
    print("--REPORT--")
    for k, v in resources.items():
        print(f"{k}, :  {v}")


def check_resources(drink: str):
    coffee_ingredients = MENU[drink]["ingredients"]
    # if drink == "espresso":
    #     coffee_ingredients = MENU["espresso"]["ingredients"]
    # elif drink == "latte":
    #     coffee_ingredients = MENU["latte"]["ingredients"]
    # elif drink == "cappuccino":
    #     coffee_ingredients = MENU["cappuccino"]["ingredients"]

    # Loop through and print ingredients

    for ingredient, amount in coffee_ingredients.items():
        if ingredient == "water" and amount > machine_resource["water"]:
            print("Sorry there is not enough water.")
            return False
        elif ingredient == "milk" and amount > machine_resource["milk"]:
            print("Sorry there is not enough milk.")

            return False
        elif ingredient == "coffee" and amount > machine_resource["coffee"]:
            print("Sorry there is not enough coffee.")

            return False

    return True


machine_off: bool = False

while not machine_off:
    prompt: str = input("☕ What would you like? (espresso/latte/cappuccino) ").lower()

    if prompt == "off":
        print("See you again")
        machine_off = True
    elif prompt == "report":
        print_report()
    else:
        if not check_resources(prompt):
            machine_off = True
        else:
            print("True")
