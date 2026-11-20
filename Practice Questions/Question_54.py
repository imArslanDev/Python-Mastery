"""
Question: Write a program that takes a list and a target number. Use a loop to determine if the target number exists in the list. Do not use the in operator.
"""

# Solution

my_list = [10, 20, 30, 40, 50]
target = 30
found = False

for item in my_list:
    if item == target:
        found = True
        break

if found:
    print(f"{target} exists in the list.")
else:
    print(f"{target} does not exist in the list.")