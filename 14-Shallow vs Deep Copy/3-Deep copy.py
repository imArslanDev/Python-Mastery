import copy

# Look at the problem with shallow copy
original = [1, 2, 3, [10, 20, 30, 40], 4, 5, 6]

shallow_copy = copy.copy(original)

shallow_copy[3][0] = 1000
shallow_copy.append("500")

"""
Problem: Mane Shallow_copy ma change kia but wo orginal ma bhi chage hogya
reason: Shallow copy sirf outer Mutable object pr kam krta ha but for nested
you need to create deep coppy
"""

print(f"Original Array: {original}")
print(f"Copy Array: {shallow_copy}")


# Solution: Deep Copy
print("After Deep Copy:")

deep_copy = copy.deepcopy(original)

deep_copy[3][0] = 5000

print(f"Original Array: {original}")
print(f"Deep Copy: {deep_copy}")

# Now Copy ma jitna mrzi nested chala jau or kuch change krdu orignbal ma change nhi hoga

"""
Interview: Agr Muitable Object ke andr nested mutable object ya objects hoon
or unka bhi copy create krna ho to use kro deep copy ko.
"""