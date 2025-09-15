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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


hi=True
while hi:
    choice=input("What would you like ? (espresso/latte/cappuccino): ").lower()
    if choice == "espresso":
        ingredients=MENU["espresso"]["ingredients"]
        cost=MENU["espresso"]["cost"]
        if resources["water"] - ingredients["water"]>0:
            resources["water"] -= ingredients["water"]
        if resources["coffee"] - ingredients["coffee"]>0:
            resources["coffee"] -= ingredients["coffee"]
        if resources["coffee"] - ingredients["coffee"]>0:
            resources["coffee"] -= ingredients["coffee"]
        elif resources["water"] - ingredients["water"]<0:
            print("sorry there is not enough water")
        elif resources["coffee"] - ingredients["coffee"]<0:
            print("sorry there is not enough coffee")
        print("Please insert coins")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        total=quarters*0.25+dimes*0.1+nickles*0.01+pennies*0.01
        if total>cost:
            print(f"Here is ${total-cost:.2f} in change")
            print("Here is your espresso enjoy")
        else:
            print("sorry there is not enough money.Money is refunded")
    elif choice == "latte":
        ingredients=MENU["latte"]["ingredients"]
        cost=MENU["latte"]["cost"]
        if resources["water"] - ingredients["water"]>0:
            resources["water"] -= ingredients["water"]
        if resources["milk"] - ingredients["milk"]>0:
            resources["milk"] -= ingredients["milk"]
        if resources["coffee"] - ingredients["coffee"]>0:
            resources["coffee"] -= ingredients["coffee"]
        elif resources["water"] - ingredients["water"]<0:
            print("sorry there is not enough water")
        elif resources["milk"] - ingredients["milk"]<0:
            print("sorry there is not enough milk")
        elif resources["coffee"] - ingredients["coffee"]<0:
            print("sorry there is not enough coffee")
        print("Please insert coins")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        total=quarters*0.25+dimes*0.1+nickles*0.01+pennies*0.01
        if total>cost:
            print(f"Here is ${total-cost:.2f} in change")
            print("Here is your latte enjoy")
        else:
            print("sorry there is not enough money.Money is refunded")
    elif choice == "cappuccino":
        ingredients=MENU["cappuccino"]["ingredients"]
        cost=MENU["cappuccino"]["cost"]
        if resources["water"] - ingredients["water"]>0:
            resources["water"] -= ingredients["water"]
        if resources["milk"] - ingredients["milk"]>0:
            resources["milk"] -= ingredients["milk"]
        if resources["coffee"] - ingredients["coffee"]>0:
            resources["coffee"] -= ingredients["coffee"]
        if resources["coffee"] - ingredients["coffee"]>0:
            resources["coffee"] -= ingredients["coffee"]
        elif resources["water"] - ingredients["water"]<0:
            print("sorry there is not enough water")
        elif resources["milk"] - ingredients["milk"]<0:
            print("sorry there is not enough milk")
        elif resources["coffee"] - ingredients["coffee"]<0:
            print("sorry there is not enough coffee")
        print("Please insert coins")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        total=quarters*0.25+dimes*0.1+nickles*0.01+pennies*0.01

        expense=total-cost

        if expense>0 :
            print(f"Here is ${expense} in change")
            print("Here is your cappuccino enjoy")
        else:
            print("sorry there is not enough money.Money is refunded")

    elif choice == "report":
        print(f"Water: resources[water]ml")
        print(f"Milk: resources[milk]ml")
        print(f"Coffee: resources[cofee]ml")
        print(f"Money:${expense}")
    elif choice=="off":
        hi=False









