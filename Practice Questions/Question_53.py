"""
Question: Given a list of numbers, write Python code using a loop to find and print the largest element. Do not use the built-in max() function
"""

# Solution

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print(f"The largest element is: {largest}")