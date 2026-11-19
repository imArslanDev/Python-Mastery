"""
Question: Take a number as input. Using the ternary operator, print "Even" or "Odd" in a single line.
"""

# Solution:

num = int(input("Enter a number: "))

even_or_odd = "Even" if num % 2 == 0 else "Odd"

print(f"{num} is {even_or_odd} number")