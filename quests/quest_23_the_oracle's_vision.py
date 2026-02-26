#!/usr/bin/env python3
#  Write a function calculate_area(length, width) that returns the area. Call it for two different rectangles and print the results.
def calculate_area(length, width):
    return length * width

area1 = calculate_area(5, 3)
area2 = calculate_area(10, 7)

print(f"Area of first rectangle: {area1}")
print(f"Area of second rectangle: {area2}")