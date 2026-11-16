# my_tuple = (1, 2, 3, 4)
# my_tuple = 1, 2, 3, 4
# print(my_tuple, type(my_tuple))

# Store a single element in a tuple use comma:
single_tuple = 1,
print(type(single_tuple), single_tuple)

# This Procedure is called Unpacking
name, age, profession = "Arslan", 20, "Artist"
print(name, type(name))
print(age, type(age))
print(profession, type(profession))

a = 5
b = 10

a, b = (5, 10)
