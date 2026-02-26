age = int(input("Enter your age "))
gold = int(input("How many gold coins do you have? "))

if age >= 18 and gold >= 20:
    print("Welcome to the club! Enjoy your evening.")
else:
    print("Sorry, you can not enter.")
    if age < 18:
        print("You must be at least 18 years old.")
        if gold < 20:
            print("You need at least 20 gold coins.")
