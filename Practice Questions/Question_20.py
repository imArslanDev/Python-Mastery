"""
Question: Take numbers as input from the user one by one. Skip negative
numbers and keep adding the positive ones. Stop when the user
enters 0 and print the total. (Uses both continue and break.)
"""

# Solution
total = 0

while True:
    num = int(input("Enter a number: (0 to stop): "))

    if num == 0:
        break

    if num < 0:
        continue

    total += num

print(f"Total: {total}")
