"""
Question: Create a list of numbers (e.g., [5, 2, 8, 1, 9, 3]). Print the list in ascending order and then in descending order using the sorted() function. 
After printing, verify and print the original list to confirm it remains unchanged.
"""

# Solution

nums = [5, 2, 8, 1, 9, 3]

print(f"Ascending Order: {sorted(nums)}")
print(f"Descending Order: {sorted(nums, reverse=True)}")
print(f"Original List: {nums}")