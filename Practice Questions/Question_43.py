"""
Question:  Write a function called absolute_value that takes a number and returns 
its absolute value without using the built-in abs() function.
"""

# Solution

def absolute_value(num):
    if num < 0:
        return - num
    return num

result = absolute_value(-100) 
print(result)