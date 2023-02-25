# Global Variables----------------
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
    "water": 900,
    "milk": 200,
    "coffee": 100,
}

money = 0


# TODO: 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
def ask_user():
    answer = ""
    while answer != "espresso" and answer != "latte" and answer != "cappuccino" and answer != "report" and answer != "off":
        answer = input("What would you like? (espresso/latte/cappuccino): ")
    return answer


# TODO: 3. Print reporting function ☕
def report():
    print(f"water: {resources['water']}ml")
    print(f"milk: {resources['milk']}ml")
    print(f"coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


# TODO: 4. Check resources sufficient?
def check_resources(coffee_type):
    for ingredient in MENU[coffee_type]["ingredients"]:
        if resources[ingredient] < MENU[coffee_type]["ingredients"][ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True


# TODO: 5. Process coins.
def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    return total


# TODO: 6. check transaction
def check_transaction(coffee_type, total_money):
    if total_money > MENU[coffee_type]["cost"]:
        money_change = round(total_money - MENU[coffee_type]["cost"], 2)
        print(f"Here is ${money_change} in change")
        return True
    elif total_money == MENU[coffee_type]["cost"]:
        print("enough")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# TODO: 7. Make coffee
def make_coffee(coffee_type):
    for ingredient in MENU[coffee_type]["ingredients"]:
        resources[ingredient] -= MENU[coffee_type]["ingredients"][ingredient]
    print(f"Here is your {coffee_type} ☕. Enjoy!")
# TODO: 2. Turn off machine by entering "off" to the prompt


# Main program----------
should_continue = True
while should_continue:
    choice = ask_user()
    # Debug:
    # print(choice)
    if choice == "report":
        report()
    elif choice == "off":
        should_continue = False
    else:
        if check_resources(choice):
            user_money = process_coins()
            print(f"Total money: {user_money}")
            if check_transaction(choice, user_money):
                make_coffee(choice)
                money += MENU[choice]["cost"]
