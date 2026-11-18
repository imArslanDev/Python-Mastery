"""
Question: Take two numbers as input. Print whether it is even or odd using the % operator and a comparion operator
"""

# Solution:

num = int(input("Enter a number:"))

even = num % 2 == 0
odd = num % 2 != 0

print(f"{num} is Even: {even}")
print(f"{num} is Odd: {odd}")