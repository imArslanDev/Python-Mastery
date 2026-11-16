my_tuple = (1,2,3,4,5,"Arslan", "Ali Zafar", True, 560)

length = len(my_tuple)

# Iterate using for loop
for i in range(0, length):
    print(my_tuple[i], end=" ")

print()

# Iterating using for-in loop
for elem in my_tuple:
    print(elem, end=" ")

print()

# Iterate using Enumerate
for idx, value in enumerate(my_tuple):
    print(f"{value} at index {idx}")