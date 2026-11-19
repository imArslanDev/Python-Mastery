"""
Question:  Take three numbers as input. Print the largest of the three without using any 
built-in function.
"""

# Solution:

num1 = int(input("Enter num 1: "))
num2 = int(input("Enter num 2: "))
num3 = int(input("Enter num 3: "))

if num1 >= num2 and num1 >= num3:
    print(f"{num1} is largest")
elif num2 >= num1 and num2 >= num3:
    print(f"{num2} is largest")
else:
    print(f"{num3} is largest")