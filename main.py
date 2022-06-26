import coffeemachine_menu

print(coffeemachine_menu.logo)
run = True


def coffee_machine(run):
    while run:
        pick = input("What would you like to? (espresso/latte/cappuccino): ")

        if pick == 'off':
            run = False
            print('machine off')
            return run
        elif pick == 'report':
            print(f'Water: {coffeemachine_menu.resources["water"]}ml')
            print(f'Milk: {coffeemachine_menu.resources["milk"]}ml')
            print(f'coffee: {coffeemachine_menu.resources["coffee"]}ml')
            print(f'Money: ${coffeemachine_menu.bank}')
            coffee_machine(run)
        elif pick == 'espresso' or pick == 'latte' or pick == 'cappuccino':
            print(resources_validator(pick))

            if resources_validator(pick) != 'Please insert coins':
                coffee_machine(run)

            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            total = coin_adder(quarters, dimes, nickles, pennies)
            cost = coffeemachine_menu.menu[pick]["cost"]
            diff = str(round(total - cost, 2))

            if total < cost:
                print('Sorry that is not enough money. Money refunded')
                coffee_machine(run)
            elif total > cost:
                consumption(pick)
                coffeemachine_menu.bank += cost
                print(f'Here is ${diff} in change.')
                print(f'Here is your {pick}. Enjoy!')
                coffee_machine(run)
            else:
                consumption(pick)
                coffeemachine_menu.bank += cost
                print(f'Here is your {pick}. Enjoy!')
                coffee_machine(run)


def consumption(pick):
    coffeemachine_menu.resources["water"] -= coffeemachine_menu.menu[pick]["ingredients"]["water"]
    coffeemachine_menu.resources["milk"] -= coffeemachine_menu.menu[pick]["ingredients"]["milk"]
    coffeemachine_menu.resources["coffee"] -= coffeemachine_menu.menu[pick]["ingredients"]["coffee"]


def coin_adder(quarters, dimes, nickles, pennies):
    total = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    return total


def resources_validator(pick):
    if coffeemachine_menu.menu[pick]["ingredients"]["water"] > coffeemachine_menu.resources["water"]:
        return 'Sorry there is not enough water'
    elif coffeemachine_menu.menu[pick]["ingredients"]["milk"] > coffeemachine_menu.resources["milk"]:
        return 'Sorry there is not enough milk'
    elif coffeemachine_menu.menu[pick]["ingredients"]["coffee"] > coffeemachine_menu.resources["coffee"]:
        return 'Sorry there is not enough coffee'
    else:
        return 'Please insert coins'


coffee_machine(run)

