randomList = ["Asim", "Ali", 56, 91.8120, 100, "Zoha"]

# Accessing List Elements
print(randomList[0]) # Give First Element "Asim"
print(randomList[-1]) # Give Last Element "Zoha"

length = len(randomList)
print(f"randomList Length: {length}")

print(f"Last Index Element: {randomList[len(randomList) - 1]}")

# print(randomList[100]) # IndexError: list index out of range