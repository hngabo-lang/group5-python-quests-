# !/usr/bin/env python3
# Write a grading program. Ask for a score (0-100). Print "A" for 90+, "B" for 80-89, "C" for 70-79, and "Needs Improvement" otherwise.
score = int(input("Enter your score (0-100): "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("Needs Improvement")