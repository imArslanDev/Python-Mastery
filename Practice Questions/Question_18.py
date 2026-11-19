"""
Question: Ask a number from the user, print the multiplication table upto 10.
"""

num = int(input("Enter a number: "))

# Solution:
i = 1
while(i <= 10):
    print(f"{num} X {i} = {i * num}")
    i += 1