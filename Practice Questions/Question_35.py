"""
Question:  Write a function that ask a number from user and prints if that 
number is odd or even.
"""

# Solution

num = int(input("Enter a number:"))

def add_or_even(num):
    if(num % 2 == 0):
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")
        
add_or_even(num)