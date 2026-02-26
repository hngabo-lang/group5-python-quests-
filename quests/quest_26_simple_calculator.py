#!/usr/bin/env python3

#quest 26 the simple calculator 

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
value1 = float(input("enter first value: "))
value2 = float(input("enter second value: "))

operation = input("enter operation (add, subtract, multiply, divide): ")

if operation == "add":
    print(f"answer: {add(value1, value2)}")

elif operation == "subtract":
    print(f"answer: {subtract(value1, value2)}")

elif operation == "multiply":
    print(f"answer: {multiply(value1, value2)}")

elif operation == "divide":
    print(f"answer: {divide(value1, value2)}")

else:
    print("invalid operation")

