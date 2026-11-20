"""
Question: Write a function called min_of_three that takes three numbers and returns 
the smallest without using any built-in function.
"""

# Solution

def min_of_three(num1, num2, num3):
    smallest = num1 if num2 > num1 and num3 > num1 else num2 if num3 > num2 else num3
    return smallest

result = min_of_three(100, 90, 122)
print(result)