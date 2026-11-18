"""
Question: Take two numbers as input from the user, Print their sum, difference, product and reminder
"""

# Solution:

num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
reminder = num1 % num2

print(f"Sum: {sum}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Remainder: {reminder}")