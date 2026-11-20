"""
Question:  Find the largest and smallest number 
in a list without using built-in functions like 
max() or min().
Hint: Use a loop and a variable to track the 
current largest/smallest as you go through 
the list. Example: if the list is [3, 1, 4, 1, 5], 
the largest is 5 and smallest is 1
"""

# Solution

nums = [3, 1, 4, 1, 5]
largest = nums[0]
smallest = nums[0]

for num in nums:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print(f"Largest: {largest}, Smallest: {smallest}")