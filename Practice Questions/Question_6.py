"""
Question: Take two numbers as input. Without using *, calculate and print their product 
using += in a way that adds the first number to itself the second number of times.
"""

# Solution:
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

product = 0

for i in range(num2):
    product += num1

print(f"Product: {product}")