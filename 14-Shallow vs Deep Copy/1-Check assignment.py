original = [1,2,3]
copy = original

copy.append(500)

print(copy)
print(original)

print(id(copy))
print(id(original))

print(original is copy)
print(original == copy)