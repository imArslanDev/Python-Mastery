# Shallow Copy

import copy

original = [1,2,3]

# Method 1 for creating shallow copy:
# shallow_copy = original.copy()

# Method 2 for creating shallow copy:
shallow_copy = copy.copy(original)





print(f"Original ID: {id(original)}")
print(f"Copy ID: {id(shallow_copy)}")


shallow_copy.append("500")

print(f"Original Array: {original}")
print(f"Copy Array: {shallow_copy}")
