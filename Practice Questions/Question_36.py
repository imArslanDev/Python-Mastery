"""
Question: Write a function that print all the factors of a number entered by user.
"""

# Solution

num = int(input("Enter a number:"))


def get_factors(num):
    i = 1
    for i in range(i, num):
        if(num % i == 0):
            print(i, end=" ")
            
get_factors(num)