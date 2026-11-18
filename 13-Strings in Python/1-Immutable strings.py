# Strings are immutable

name = "HM Arslan"
print(name[0])
print(name[-1])
print(name, id(name))

# Override
name = "Hafiz Muhammad Arslan"
print(name, id(name))

# name[0] = "Z" # Assignment Not Allowed But Override is allowed
# print(name)
