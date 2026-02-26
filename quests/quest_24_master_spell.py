def ask_age():
    age = int(input("How old are you? "))
    return age

def can_vote(age):

    if age >= 18:
        print(f"At {age} years old, you can vote!")
    else:
        years_left = 18 - age
        print(f"At {age} years old, you cannot vote. {years_left} more year(s) to go!")

user_age = ask_age()

can_vote(user_age)

