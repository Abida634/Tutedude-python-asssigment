#Assigment - 5

# TASK - 1

import re

students = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92}

name = input("Enter the student's name: ")


if re.search("[A-Z][a-z]+", name):
    if name in students:
        print(name + "'s marks:", students[name])
    else:
        print("Student not found.")
else:
    print("Invalid name format.")
