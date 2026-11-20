"""
Question: Reverse a list without using the 
.reverse() method or list slicing ([::-1]).
Hint: Think about swapping elements from 
both ends of the list using a loop. 
Example: [1, 2, 3, 4, 5] → [5, 4, 3, 2, 1]
"""

# Solution

nums = [1, 2, 3, 4, 5]
reversed_list = nums.copy()

left = 0
right = len(reversed_list) - 1

while left < right:
    reversed_list[left], reversed_list[right] = reversed_list[right], reversed_list[left]
    left += 1
    right -= 1

print(reversed_list)  # [5, 4, 3, 2, 1]