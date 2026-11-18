"""
Question: Take a number as input. Print the result of that raised to the power of 3 using **.
Also print what // 7 and % 7 give for the same number. 
"""

# Solution:
num = int(input("Enter a number:"))

cube = num ** 3
floor_division = num // 7
remainder = num % 7

print(f"Result of {num} ** 3 = {cube}")
print(f"Result of {num} // 7 = {floor_division}")
print(f"Result of {num} % 7  = {remainder}")