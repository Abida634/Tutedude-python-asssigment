# Assigment - 5

# TASK - 2

import re

num1 = "1 2 3 4 5 6 7 8 9 10"

numbers = re.findall(r"\d+", num1)
numbers = [int(n) for n in numbers]

first_five = []
temp_numbers = numbers.copy()

for i in range(5):
    first_five.append(temp_numbers.pop(0))

reversed_list = first_five.copy()
reversed_list.reverse()

print("Original list:", numbers)
print("Extracted first five elements:", first_five)
print("Reversed extracted elements:", reversed_list)





