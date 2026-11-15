nums = [4, 7, 3, 8, 1, 1, 2, 10, 9, 6, 9, 1, 1, 1]

# Sort vs Sorted

# Sorted Returns a new list
new_list = sorted(nums)
print(f"new_list = {new_list}", id(new_list))

# Work on Existing List not return anything 
print(f"nums = {nums}", id(nums))
nums.sort(reverse=True)  # In place sorting
print(f"nums = {nums}", id(nums))
