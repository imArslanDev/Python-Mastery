text = "Programming"

length = len(text)
vowels_count = 0

# Iterate using for loop
for i in range(0, length):
    vowels = ["a", "e", "i", "o", "u"]
    for j in range(0, len(vowels)):
        if vowels[j] == text[i] or vowels[j].upper() == text[i].upper() :
            vowels_count += 1


print(f"Vowels Count: {vowels_count}")

# Iterate using for in loop
for char in text:
    print(char, end="")

print()

# Iterate using enumerate
for idx, char in enumerate(text):
    print(f"ind = {idx} and ch = {char}")


# Iterate using while loop
i = 0
while i < length:
    print(text[i], end="")
    i += 1
