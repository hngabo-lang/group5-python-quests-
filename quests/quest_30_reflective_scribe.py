# quest 4: town crier
# It attaches strings and variabes together for dynamic output
cty_name = "Kigali"
crt_year = 2026    # storing each data in variables
_name = "Henry"

# f-strings will handle non string data type and embed variables directly with in braces.
print(f"Welcome to {cty_name}! The year is {crt_year}, and our newest resident is {name}.")
# =============================================================================


# quest 9: Greedy Goblin
# Uses integer division and modulus operator //
gold_p = 27
friends = 4

# Integer division, divides the golds to friends finally we get the number of golds each friend got.
division = gold_p // friends   # 27 // 4 = 6

# Modulus operator, gives only the remainder got after division
remainder = gold_p % friends       # 27 % 4 = 3

print(f"Each friend of goblin got: {division} gold pieces")
print(f"The goblin keeps: {remainder} gold pieces of remainder")
# =============================================================================


# quest14: Logical Gatekeeper
age  = int(input("Enter your age "))
gold = int(input("How many gold coins do you have? "))

# The and operator means that both conditions will be True at the time, if one fails it goes to else.
if age >= 18 and gold >= 20:
    print("Welcome to the club! Enjoy your evening.")
else:
    # We check each condition separately to give specific reasons
    print("Sorry, you cannot enter.")
    if age < 18:
        print("You must be at least 18 years old.")
    if gold < 20:
        print("You need at least 20 gold coins.")
# ===============================================================================

# quest 20: Even number forager
# Uses if inside a for loop to filter
print("Even numbers between 1 and 20:")

# range(1, 21) generates numbers from 1 up to (but not including) 21.
# The for loop visits each number one at a time and stores it in 'number'.
for number in range(1, 21):
    # A number is even when divided by 2 then the remainder is 0.
    # Then putting if inside the loop makes the number to meet our condition.
    if number % 2 == 0:
        print(number)
