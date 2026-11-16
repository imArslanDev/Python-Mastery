my_tuple = (1,2,3,4,5,"Arslan", "Ali Zafar", True, 560)
# Slicing ma new tuple mil rha ha naki existing tuple ma kuch change
reverse_values = my_tuple[::-1]

print(f"Original Tuple = {my_tuple}")
print(f"Reversed Tuple = {reverse_values}")
# Proof that they both are not same
print(True if my_tuple == reverse_values else False)
print(id(my_tuple))
print(id(reverse_values))
